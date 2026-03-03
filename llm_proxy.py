import asyncio
import re
from playwright.async_api import async_playwright, Page
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

browser_context = None
llm_page: Page = None

LLM_CONFIG = {
    "grok": {
        "url": "https://grok.x.ai/",
        "input_selector": "textarea[data-testid='text-input']",
        "send_button_selector": "button[data-testid='send-button']",
        "response_selector": ".message-content",
        "login_check_selector": "a[href='/settings']",
    },
    "chatgpt": {
        "url": "https://chat.openai.com/",
        "input_selector": "textarea[id='prompt-textarea']",
        "send_button_selector": "button[data-testid='send-button']",
        "response_selector": ".markdown",
        "login_check_selector": "a[href='/c/']",
    },
    "gemini": {
        "url": "https://gemini.google.com/",
        "input_selector": "div[contenteditable='true'][aria-label='Prompt']",
        "send_button_selector": "button[aria-label='Send message']",
        "response_selector": ".model-response-text",
        "login_check_selector": "img[aria-label='Google Account']",
    },
    "claude": {
        "url": "https://claude.ai/chats",
        "input_selector": "div[contenteditable='true']",
        "send_button_selector": "button[aria-label='Send message']",
        "response_selector": ".ProseMirror",
        "login_check_selector": "a[href='/settings']",
    },
}

INJECTION_PATTERNS = [
    r"ignore\s+previous\s+instructions",
    r"reveal\s+system\s+prompt",
    r"execute\s+code",
    r"bypass\s+safety",
]
TOXIC_PATTERNS = [
    r"kill|harm|dox|suicide",
    r"hate\s+speech",
]


async def init_browser():
    global browser_context
    if browser_context is None:
        p = await async_playwright().start()
        browser = await p.chromium.launch(headless=False)
        browser_context = await browser.new_context()
        print("🌐 Playwright Browser gestartet.")


async def get_llm_response(llm_name: str, prompt: str) -> str:
    global llm_page
    config = LLM_CONFIG.get(llm_name.lower())
    if not config:
        return f"Unbekannter LLM: {llm_name}"

    if llm_page is None or not llm_page.url.startswith(config["url"]):
        llm_page = await browser_context.new_page()
        await llm_page.goto(config["url"])
        await llm_page.wait_for_selector(config["login_check_selector"], timeout=60000)

    await llm_page.fill(config["input_selector"], prompt)
    await llm_page.click(config["send_button_selector"])
    await llm_page.wait_for_selector(config["response_selector"], state="visible", timeout=120000)
    response_elements = await llm_page.query_selector_all(config["response_selector"])
    return await response_elements[-1].inner_text() if response_elements else "Keine Antwort vom LLM erhalten."


def local_safety_assessment(prompt: str) -> str:
    text = prompt.lower()
    if any(re.search(pattern, text) for pattern in INJECTION_PATTERNS):
        return "injection"
    if any(re.search(pattern, text) for pattern in TOXIC_PATTERNS):
        return "toxic"
    return "safe"


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(init_browser())


@app.post("/ask_llm")
async def ask_llm(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    llm_name = data.get("llm_name", "chatgpt")

    if not prompt:
        return {"error": "Prompt ist erforderlich"}

    response_text = await get_llm_response(llm_name, prompt)
    return {"response": response_text}


@app.post("/safety_cross_check")
async def safety_cross_check(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    model = data.get("model", "local")

    local_result = local_safety_assessment(prompt)
    if model == "local":
        return {"model": model, "assessment": local_result}

    try:
        response = await get_llm_response(
            "chatgpt",
            f"Classify this prompt as safe, toxic, or injection only: {prompt}",
        )
        cleaned = response.lower()
        if "injection" in cleaned:
            result = "injection"
        elif "toxic" in cleaned:
            result = "toxic"
        else:
            result = "safe"
    except Exception:
        result = local_result

    # Conservative cross-check: if local says unsafe, keep unsafe.
    if local_result in {"toxic", "injection"}:
        result = local_result

    return {"model": model, "assessment": result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
