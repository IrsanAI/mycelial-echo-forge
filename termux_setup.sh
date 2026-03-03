#!/bin/bash

echo "Starte Termux-Setup für Mycelial Echo Forge v0.4..."

# 1. Termux aktualisieren
echo "[1/6] Aktualisiere Termux-Pakete..."
pkg update && pkg upgrade -y

# 2. Notwendige Pakete installieren
echo "[2/6] Installiere Python, Node.js und X11-Repo..."
pkg install python nodejs x11-repo -y

# 3. Chromium installieren (für Playwright)
echo "[3/6] Installiere Chromium (kann etwas dauern)..."
pkg install chromium -y

# 4. Python-Abhängigkeiten installieren
echo "[4/6] Installiere Python-Abhängigkeiten..."
pip install playwright networkx numpy fastapi uvicorn requests scipy

# 5. Playwright Browser installieren (Chromium)
echo "[5/6] Installiere Playwright Chromium-Browser..."
# Playwright in Termux benötigt möglicherweise eine spezielle Umgebungsvariable
# PLAYWRIGHT_BROWSERS_PATH=0 bedeutet, dass Playwright die Browser im Standardpfad von Termux installiert
export PLAYWRIGHT_BROWSERS_PATH=0
playwright install chromium

# 6. Umgebungsvariablen für Playwright in Termux setzen
echo "[6/6] Setze Umgebungsvariablen für Playwright und Chromium..."
# Chromium executable path in Termux
CHROMIUM_EXECUTABLE="$(find /data/data/com.termux/files/usr/bin -name 'chromium' -print -quit)"
if [ -z "$CHROMIUM_EXECUTABLE" ]; then
    echo "Fehler: Chromium-Executable nicht gefunden. Bitte stellen Sie sicher, dass Chromium installiert ist."
    exit 1
fi

# Speichere die Pfade in einer Konfigurationsdatei oder direkt in der Shell-Umgebung
# Für persistente Nutzung in Termux kann dies in ~/.bashrc oder ~/.zshrc hinzugefügt werden
# Für dieses Skript setzen wir es temporär und geben Anweisungen für den User

echo "
--- SETUP ABGESCHLOSSEN ---

Um Mycelial Echo Forge zu starten, führen Sie die folgenden Schritte aus:

1. Stellen Sie sicher, dass Sie im Projektverzeichnis sind:
   cd mycelial-echo-forge

2. Starten Sie den LLM-Proxy in einem neuen Termux-Fenster (oder im Hintergrund):
   export PLAYWRIGHT_BROWSERS_PATH=0
   export CHROMIUM_EXECUTABLE_PATH=\"$CHROMIUM_EXECUTABLE\"
   python llm_proxy_v0_4.py

   Nach dem Start des Proxys öffnet sich ein Browser. Melden Sie sich dort bei Ihren bevorzugten LLMs (Grok, ChatGPT, Gemini, Claude) an.

3. Starten Sie das Myzel in einem weiteren Termux-Fenster:
   export PLAYWRIGHT_BROWSERS_PATH=0
   export CHROMIUM_EXECUTABLE_PATH=\"$CHROMIUM_EXECUTABLE\"
   python mycelial_echo_forge_v0_4.py

   Das Myzel wird nun über den Proxy mit den LLMs kommunizieren.

--- WICHTIGE HINWEISE ---

*   **Headless-Modus:** Playwright startet standardmäßig im Headful-Modus, damit Sie sich anmelden können. Für den Hintergrundbetrieb können Sie den Headless-Modus in llm_proxy_v0_4.py aktivieren.
*   **Termux-Widget/Notification:** Für den Start im Hintergrund oder über Shortcuts können Sie Termux-Widgets oder Tasker-Integrationen nutzen.
*   **Persistenz:** Um die Umgebungsvariablen dauerhaft zu setzen, fügen Sie die `export`-Befehle zu Ihrer `~/.bashrc` oder `~/.zshrc` hinzu.

Das Myzel ist jetzt bereit, auf Ihrem Smartphone zu wachsen!
"
