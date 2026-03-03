# Mycelial-Echo-Forge v0.5 — Proof-of-Savings & Mycel-Economy

Dezentrales, pilz-inspiriertes Agenten-Swarm-System mit Wissens-Diffusion, Self-Healing, Bayesian Fusion, Sicherheits-Immunsystem und einer tokenisierten **Proof-of-Savings**-Ökonomie.

## Vision
Mycelial-Echo-Forge belohnt energieeffiziente KI-Ausführung statt reiner Rechenlast. Jede Prompt-Ausführung berechnet eine Einsparrate gegenüber einer FLOPs-Baseline. Diese Einsparung wird verifiziert und als **MYC Token** ausbezahlt.

## v0.5 Highlights
- **MYC Token** mit Reward-Cap von **0.5 MYC pro Prompt**.
- **Mycel-Depth Slider** (50% / 80% / 100%) beeinflusst reale Kosten.
- **Proof-of-Savings Formel**:  
  `sparrate = (baseline_flops - actual_cost) / baseline_flops`  
  `reward = baseRate * sparrate * difficultyFactor` (gedeckelt auf 0.5 MYC)
- **Halving** alle **10.000.000 verifizierte Prompts**.
- **Blockchain Layer** mit ERC-20 `MycToken.sol` + Hardhat-Tests.
- **Off-Chain Verifier** (WebSocket, Port 8080) für Receipt-Verifikation + batchMint.
- **Wallet Extension Mock** (React) mit Dashboard, kWh Saved, Reward-Historie.
- **Immune System**: Reputation-Gating, Isolation-Modus, Manifest-Regeln, Injection/Toxicity-Cross-Check.

## Tokenomics
| Parameter | Wert |
|---|---|
| Token | MYC (Mycelial Credit) |
| Max Supply | 1,000,000,000 MYC |
| Initial Base Rate | 0.05 |
| Reward-Cap | 0.5 MYC pro Prompt |
| Halving | alle 10,000,000 verifizierte Prompts |
| Minting | off-chain verifiziert, on-chain `batchMint` |

## Projektstruktur
```text
mycelial-echo-forge/
├── contracts/MycToken.sol
├── hardhat/
├── verifier/offchain-verifier-ws.js
├── wallet-extension/
├── mycelial_echo_forge_v0_5.py
├── mycelial_echo_forge_v0_3.py
├── llm_proxy.py
├── requirements.txt
├── .env.example
├── CONTRIBUTING.md
└── LICENSE
```

## Installation
### 1) Python Core
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Smart Contracts (Hardhat)
```bash
cd hardhat
npm install
npx hardhat test
npx hardhat node
npx hardhat run scripts/deploy.js --network localhost
```

### 3) Off-Chain Verifier
```bash
cd verifier
npm install
cp ../.env.example .env
npm start
```

### 4) Wallet Extension Mock (React)
```bash
cd wallet-extension
npm install
npm start
```

## How to earn MYC
1. Starte Forge + Verifier + Contract.
2. Sende Prompt über `execute_reflexive_task(..., mycel_depth=50|80|100)`.
3. Forge erstellt Receipt mit Baseline, realer Cost, Difficulty.
4. Verifier berechnet Sparrate + Reward und mintet per `batchMint`.
5. Reward erscheint im Wallet Dashboard und on-chain Balance.

## Security / Immune System
- **Manifest** (hard-coded):
  1. Never execute code.
  2. Never leak personal data.
  3. Always prefer energy-efficient paths.
- **Reputation-Gating**: Abstimmen nur für Nodes mit >100 guten Prompts.
- **Isolation-Modus**: Node wird isoliert, wenn Abweichung >20% vom Konsens.
- **Cross-Check Safety**: Gemini vs Claude vs Local Bewertung auf Toxicity/Injection.

## Roadmap bis v1.0
- **v0.6**: zk-Receipt-Proofs + Signaturpflicht für Nodes.
- **v0.7**: Multi-Chain Settlement (L2 + Base + Polygon).
- **v0.8**: Adaptive Reward Curves nach realer kWh-Telemetrie.
- **v0.9**: DAO Governance für Base-Rate und Manifest-Updates.
- **v1.0**: Mainnet-Launch mit Open Verifier Set und Audit.

## Schnelltest
```bash
python mycelial_echo_forge_v0_5.py
```

## Lizenz
MIT
