
import asyncio
from playwright.async_api import async_playwright, Page
from fastapi import FastAPI, Request
import uvicorn
import json
import os

app = FastAPI()

# Global Playwright browser context and page
browser_context = None
llm_page: Page = None

# --- Configuration for LLM URLs and selectors ---
LLM_CONFIG = {
    "grok": {
        "url": "https://grok.x.ai/",
        "input_selector": "textarea[data-testid=\"text-input\"]",
        "send_button_selector": "button[data-testid=\"send-button\"]",
        "response_selector": ".message-content", # This might need adjustment
        "login_check_selector": "a[href=\"/settings\"]" # Example: a common element after login
    },
    "chatgpt": {
        "url": "https://chat.openai.com/",
        "input_selector": "textarea[id=\"prompt-textarea\"]",
        "send_button_selector": "button[data-testid=\"send-button\"]",
        "response_selector": ".markdown", # This might need adjustment
        "login_check_selector": "a[href=\"/c/\"]" # Example: a common element after login
    },
    "gemini": {
        "url": "https://gemini.google.com/",
        "input_selector": "div[contenteditable=\"true\"][aria-label=\"Prompt\"]",
        "send_button_selector": "button[aria-label=\"Send message\"]",
        "response_selector": ".model-response-text", # This might need adjustment
        "login_check_selector": "img[aria-label=\"Google Account\"]" # Example: a common element after login
    },
    "claude": {
        "url": "https://claude.ai/chats",
        "input_selector": "div[contenteditable=\"true\"][data-placeholder=\"Ask Claude anything..."]",
        "send_button_selector": "button[aria-label=\"Send message\"]",
        "response_selector": ".ProseMirror", # This might need adjustment
        "login_check_selector": "a[href=\"/settings\"]" # Example: a common element after login
    }
}

async def init_browser():
    global browser_context, llm_page
    if browser_context is None:
        p = await async_playwright().start()
        browser = await p.chromium.launch(headless=False) # Run in headful mode for user login
        browser_context = await browser.new_context()
        print("🌐 Playwright Browser gestartet. Bitte melden Sie sich in den gewünschten LLMs an.")

async def get_llm_response(llm_name: str, prompt: str) -> str:
    global llm_page
    config = LLM_CONFIG.get(llm_name.lower())
    if not config:
        return f"Unbekannter LLM: {llm_name}"

    if llm_page is None or llm_page.url != config["url"]:
        print(f"Navigiere zu {config['url']} für {llm_name}...")
        llm_page = await browser_context.new_page()
        await llm_page.goto(config["url"])
        await llm_page.wait_for_selector(config["login_check_selector"], timeout=60000) # Wait for login
        print(f"✅ Erfolgreich bei {llm_name} angemeldet (oder bereits eingeloggt).")

    print(f"Sende Prompt an {llm_name}: {prompt[:50]}...")
    await llm_page.fill(config["input_selector"], prompt)
    await llm_page.click(config["send_button_selector"])
    
    # Wait for response - this is a generic wait, might need more specific logic for each LLM
    await llm_page.wait_for_selector(config["response_selector"], state=\"visible\", timeout=120000) # Wait up to 2 minutes
    response_elements = await llm_page.query_selector_all(config["response_selector"])
    
    # Get the last response element
    if response_elements:
        response_text = await response_elements[-1].inner_text()
        print(f"Antwort von {llm_name} erhalten: {response_text[:100]}...")
        return response_text
    else:
        return "Keine Antwort vom LLM erhalten."

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(init_browser())

@app.post("/ask_llm")
async def ask_llm(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    llm_name = data.get("llm_name", "chatgpt") # Default to ChatGPT if not specified
    
    if not prompt:
        return {"error": "Prompt ist erforderlich"}

    response_text = await get_llm_response(llm_name, prompt)
    return {"response": response_text}

# --- Ein-Klick-Skript für Chrome/Android/iOS (via Termux oder ähnlich) ---
# Dieses Skript ist nur eine Anleitung und muss manuell auf dem Zielgerät ausgeführt werden.
# Es ist nicht Teil des Python-Proxys, sondern eine separate Anweisung für den User.
# Der User muss Playwright manuell installieren und den Browser starten.
# Beispiel für Termux (Android):
# pkg install python nodejs
# pip install playwright fastapi uvicorn
# playwright install chromium
# python llm_proxy.py
# Dann im Browser des Android-Geräts die LLMs manuell anmelden.

if __name__ == "__main__":
    # This part is for local testing/running the proxy directly
    # In the actual MycelialEchoForge, it will connect to this running proxy.
    uvicorn.run(app, host="0.0.0.0", port=8000)
