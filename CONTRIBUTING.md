# Contributing

Danke für deinen Beitrag zu Mycelial-Echo-Forge.

## Setup
1. Python-Abhängigkeiten installieren: `pip install -r requirements.txt`
2. Hardhat Setup: `cd hardhat && npm install`
3. Verifier Setup: `cd verifier && npm install`

## Pull Request Flow
- Nutze feature branches.
- Führe lokale Checks aus:
  - `python -m py_compile mycelial_echo_forge_v0_5.py llm_proxy.py`
  - `cd hardhat && npx hardhat test`
- Beschreibe Security-Implikationen explizit im PR.

## Coding Standards
- Keine Platzhalter in produktiven Pfaden.
- Backwards-Kompatibilität mit v0.3 soweit möglich.
- Neue Features mit klaren Defaults und sicheren Fall-Backs.
