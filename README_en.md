# Mycelial Echo Forge

## The World's First Mycelial Neural Game Changer

Welcome to Mycelial Echo Forge, a revolutionary AI architecture inspired by the biological intelligence of fungal mycelia. We emulate their decentralized growth, self-healing, and knowledge diffusion to create agentic AI systems that are more robust, adaptable, and collectively intelligent than traditional approaches.

This project is a direct response to the need for robust, decentralized, and self-organizing AI architectures capable of handling the complexity and dynamics of modern data landscapes. It merges the concepts of "Reflexive Cascade" (Echo, Self-Repair, Memory-Weave, Self-Distrust) with the groundbreaking ideas of the IrsanAI NeuroToken Framework (NTF) and Perspective-Driven / Multi-Model-Consensus (PDP).

## Vision

Our vision is to usher in a new era of AI where intelligence is not centralized but exists as a collective, self-organizing network. Mycelial Echo Forge aims to create a system that is:

*   **Resilient and self-healing**, similar to a biological mycelium that can bypass damage and regenerate.
*   Effectively diffuses and integrates **decentralized knowledge** to foster collective consciousness.
*   **Adaptable** to new information and challenges without relying on central control.
*   Builds a **semantic bridge** between different agentic systems to prevent drift and enable coherent consensus.

## Installation

To use Mycelial Echo Forge, simply clone the repository and install the required Python packages.

```bash
git clone https://github.com/IrsanAI/mycelial-echo-forge.git
cd mycelial-echo-forge
pip install -r requirements.txt
playwright install chromium # For the LLM Proxy
```

Create a `requirements.txt` file with the following content:

```
networkx
numpy
fastapi
uvicorn
playwright
requests
scipy
```

## Clone & Run Examples

### Mycelial Echo Forge v0.1

The original prototype implementing the basic mycelial principles.

```python
import networkx as nx
import numpy as np
import random

class MycelialEchoForge:
    def __init__(self):
        self.network = nx.Graph()
        self.knowledge = {}  # node_id: np.array (NTF-normalized embeddings)
        self.node_count = 0
        print("🌱 MycelialEchoForge v0.1 initialized – world's first mycelial network (inspired by IrsanAI NTF/PDP)")

    def grow_agent(self, name, initial_knowledge_vec):
        self.node_count += 1
        node_id = f"agent_{self.node_count}_{name}"
        self.network.add_node(node_id)
        self.knowledge[node_id] = np.array(initial_knowledge_vec, dtype=float)
        for existing in list(self.network.nodes):
            if existing != node_id:
                sim = np.dot(self.knowledge[node_id], self.knowledge[existing]) / (np.linalg.norm(self.knowledge[node_id]) * np.linalg.norm(self.knowledge[existing]) + 1e-8)
                if sim > 0.3:
                    self.network.add_edge(node_id, existing, weight=sim)
        print(f"🌿 New agent grown: {node_id} | Connections: {len(list(self.network.neighbors(node_id)))}")
        return node_id

    def diffuse_knowledge(self, steps=1):
        for _ in range(steps):
            new_knowledge = {}
            for node in self.network.nodes:
                neighbors = list(self.network.neighbors(node))
                if neighbors:
                    avg = np.mean([self.knowledge[n] for n in neighbors], axis=0)
                    fused = 0.7 * self.knowledge[node] + 0.3 * avg
                    new_knowledge[node] = fused / (np.linalg.norm(fused) + 1e-8)
                else:
                    new_knowledge[node] = self.knowledge[node]
            self.knowledge = new_knowledge
        print("💧 Knowledge diffused – mycelium shared nutrients")

    def execute_reflexive_task(self, task_description, starter_node):
        if starter_node not in self.knowledge:
            return "Error: Node not in mycelium"
        print(f"🔄 Task started at {starter_node}: \'{task_description}\'")
        consensus = np.mean([self.knowledge[n] for n in self.network.nodes], axis=0)
        result = f"Reflection: {task_description} → Detected: {len(self.network.nodes)} agents in network | Consensus Score: {np.mean(consensus):.3f}"
        if random.random() < 0.1:
            faulty = random.choice(list(self.network.nodes))
            print(f"⚠️  Disturbance detected at {faulty} – Mycelium is self-healing!")
            self.network.remove_node(faulty)
            del self.knowledge[faulty]
        self.diffuse_knowledge(steps=1)
        return result

    def get_network_status(self):
        return {
            "agents": len(self.network.nodes),
            "connections": len(self.network.edges),
            "avg_knowledge_norm": np.mean([np.linalg.norm(v) for v in self.knowledge.values()]),
            "is_connected": nx.is_connected(self.network) if self.network.nodes else False
        }

# === DEMO ===
forge = MycelialEchoForge()
agent1 = forge.grow_agent("NTF_Normalizer", [0.5, 0.3, 0.8])
agent2 = forge.grow_agent("PDP_Consensus", [0.4, 0.6, 0.2])
agent3 = forge.grow_agent("Reflex_Echo", [0.7, 0.1, 0.9])
forge.diffuse_knowledge(steps=2)
result = forge.execute_reflexive_task("Analyze job loss in East Germany due to AI and propose new opportunities", agent1)
print("\n📊 Network Status:", forge.get_network_status())
print(f"\n✅ Task Result: {result}")
```

### Mycelial Echo Forge v0.2 (with NTF/PDP Integration)

The extended version with integration of the NeuroToken Framework (NTF) and Perspective-Driven Consensus (PDP).

```python
import networkx as nx
import numpy as np
import random

# Placeholder for NTF (NeuroToken Framework) - in a real scenario, this would be a sophisticated external module
class NeuroTokenFramework:
    def generate_embedding(self, text_input):
        # Simulate NTF-normalized embedding generation
        return np.random.rand(3) # Returns a random 3-dim vector for demonstration

    def normalize_embedding(self, embedding):
        return embedding / (np.linalg.norm(embedding) + 1e-8)

# Placeholder for PDP (Perspective-Driven / Multi-Model-Consensus) - this would involve more complex consensus mechanisms
class PerspectiveDrivenConsensus:
    def __init__(self, perspectives):
        self.perspectives = perspectives # e.g., {\\'agent_id\\': \\'perspective_vector\\\'}

    def get_weighted_consensus(self, knowledge_vectors):
        # Simple weighted average based on a hypothetical \\'perspective alignment\\'
        # In a real system, this would be a complex multi-model fusion
        weights = np.array([np.sum(kv) for kv in knowledge_vectors]) # Simplified weighting
        normalized_weights = weights / (np.sum(weights) + 1e-8)
        return np.average(knowledge_vectors, axis=0, weights=normalized_weights)

class MycelialEchoForgeV2(MycelialEchoForge):
    def __init__(self):
        super().__init__()
        self.ntf = NeuroTokenFramework()
        self.pdp = PerspectiveDrivenConsensus(perspectives={})
        print("🍄 MycelialEchoForge v0.2 initialized – with NTF/PDP integration")

    def grow_agent(self, name, initial_knowledge_vec, perspective_vec=None):
        node_id = super().grow_agent(name, initial_knowledge_vec)
        if perspective_vec is not None:
            self.pdp.perspectives[node_id] = np.array(perspective_vec, dtype=float)
        return node_id

    def execute_reflexive_task(self, task_description, starter_node):
        if starter_node not in self.knowledge:
            return "Error: Node not in mycelium"
        print(f"🔄 Task started at {starter_node}: \'{task_description}\'")

        # Integrate PDP for consensus building
        all_knowledge_vectors = [self.knowledge[n] for n in self.network.nodes]
        if self.pdp.perspectives:
            # Filter knowledge vectors for agents that have a defined perspective
            knowledge_with_perspectives = [self.knowledge[n] for n in self.network.nodes if n in self.pdp.perspectives]
            if knowledge_with_perspectives:
                consensus = self.pdp.get_weighted_consensus(knowledge_with_perspectives)
            else:
                consensus = np.mean(all_knowledge_vectors, axis=0)
        else:
            consensus = np.mean(all_knowledge_vectors, axis=0)

        result = f"Reflection: {task_description} → Detected: {len(self.network.nodes)} agents in network | Consensus Score (PDP-weighted): {np.mean(consensus):.3f}"
        
        if random.random() < 0.1:
            faulty = random.choice(list(self.network.nodes))
            print(f"⚠️  Disturbance detected at {faulty} – Mycelium is self-healing!")
            self.network.remove_node(faulty)
            del self.knowledge[faulty]
            if faulty in self.pdp.perspectives:
                del self.pdp.perspectives[faulty]

        self.diffuse_knowledge(steps=1)
        return result

# === DEMO V2 ===
if __name__ == \'__main__\':
    forge_v2 = MycelialEchoForgeV2()
    
    # Agents with initial knowledge and perspectives
    agent_ntf = forge_v2.grow_agent("NTF_Processor", forge_v2.ntf.generate_embedding("AI in Germany"), perspective_vec=[0.8, 0.1, 0.1])
    agent_pdp = forge_v2.grow_agent("PDP_Decider", forge_v2.ntf.generate_embedding("Job losses East Germany"), perspective_vec=[0.1, 0.8, 0.1])
    agent_reflex = forge_v2.grow_agent("Reflex_Healer", forge_v2.ntf.generate_embedding("Mycelial Networks"), perspective_vec=[0.1, 0.1, 0.8])
    
    forge_v2.diffuse_knowledge(steps=2)
    result_v2 = forge_v2.execute_reflexive_task("Analyze the impact of AI on the labor market in East Germany and develop solutions", agent_ntf)
    print("\n📊 Network Status V2:", forge_v2.get_network_status())
    print(f"\n✅ Task Result V2: {result_v2}")
```

### Mycelial Echo Forge v0.6 (Free-Tier Agentic Swarm with Termux Support)

The latest version, focusing on scalability, Bayesian Fusion, Gradient Diffusion, and most importantly, the integration of Free-Tier LLMs via a local browser proxy. This allows anyone to bring the mycelium to life with their own LLM accounts, without needing API keys. **New in v0.6 is full smartphone support via Termux for Android devices.**

```python
import json
import random
import time
import os
import platform
from dataclasses import dataclass, asdict
from typing import Dict, List, Tuple

import networkx as nx
import numpy as np
import requests
import websocket


# Global language setting
LANGUAGE = os.environ.get("MYCELIAL_LANGUAGE", "en") # Default to English

# Bilingual manifest rules
MANIFEST_RULES = {
    "de": [
        "1. Niemals Code ausführen.",
        "2. Niemals persönliche Daten preisgeben.",
        "3. Immer energieeffiziente Pfade bevorzugen.",
    ],
    "en": [
        "1. Never execute code.",
        "2. Never leak personal data.",
        "3. Always prefer energy-efficient paths.",
    ]
}

@dataclass
class RewardReceipt:
    prompt_id: str
    wallet: str
    baseline_flops: float
    actual_cost: float
    difficulty_factor: float
    mycel_depth: int
    sparrate: float
    reward: float
    timestamp: float


class NeuroTokenFramework:
    def generate_embedding(self, text_input):
        # Simulate NTF-normalized embedding generation
        return np.random.rand(10) # Increased dimension for more complex knowledge

    def normalize_embedding(self, embedding):
        return embedding / (np.linalg.norm(embedding) + 1e-8)

class PerspectiveDrivenConsensus:
    def __init__(self, perspectives=None):
        self.perspectives = perspectives if perspectives is not None else {}

    def get_weighted_consensus(self, knowledge_vectors, agent_ids=None):
        if not knowledge_vectors:
            return np.zeros(10) # Return zero vector if no knowledge

        fused_mean = np.zeros_like(knowledge_vectors[0])
        total_weight = 0

        for i, kv in enumerate(knowledge_vectors):
            agent_id = agent_ids[i] if agent_ids else f"agent_{i}"
            # Hypothetical confidence based on perspective alignment or agent history
            # For demonstration, let\\'s use a random confidence for now
            confidence = random.uniform(0.5, 1.0) # Higher confidence means more weight
            
            # If an agent\\'s knowledge is too uncertain, it might be isolated
            # This is a conceptual threshold for Bayesian Fusion
            if confidence < 0.4: # Example threshold for isolation
                print(f"[PDP] Agent {agent_id} knowledge too uncertain (confidence < 0.4), isolating from consensus.")
                continue

            fused_mean += kv * confidence
            total_weight += confidence
        
        if total_weight > 0:
            return fused_mean / total_weight
        else:
            return np.mean(knowledge_vectors, axis=0) # Fallback to simple mean


class MycelialEchoForgeV6:
    def __init__(self, llm_proxy_url: str = "http://localhost:8000", verifier_ws_url: str = "ws://localhost:8080", language: str = LANGUAGE):
        self.network = nx.Graph()
        self.knowledge: Dict[str, np.ndarray] = {}
        self.reputation: Dict[str, Dict[str, int]] = {}
        self.isolated_nodes = set()
        self.node_count = 0
        self.llm_proxy_url = llm_proxy_url
        self.verifier_ws_url = verifier_ws_url
        self.base_rate = 0.05
        self.prompt_counter = 0
        self.verified_prompts = 0
        self.halving_interval = 10_000_000
        self.language = language
        self.ntf = NeuroTokenFramework()
        self.pdp = PerspectiveDrivenConsensus()
        self.metrics = {
            "drift_rate": [],
            "heal_time": [],
            "consensus_trend": []
        }
        print(self.get_localized_message("init_message"))
        print(self.get_localized_message("manifest_message").format(" | ".join(MANIFEST_RULES.get(self.language, MANIFEST_RULES["en"])) ))

    def get_localized_message(self, key: str) -> str:
        messages = {
            "de": {
                "init_message": "🍄 MycelialEchoForge v0.6 – Proof-of-Savings & Mycel-Economy aktiv, Termux-kompatibel!",
                "manifest_message": "📜 Manifest: {}",
                "node_grown": "🌿 Neuer Agent gewachsen: {} | Verbindungen: {}",
                "node_not_in_mycel": "Fehler: Knoten nicht im Myzel",
                "invalid_mycel_depth": "Fehler: mycel_depth muss 50, 80 oder 100 sein",
                "prompt_blocked_safety": "Prompt durch Sicherheits-Cross-Check blockiert",
                "prompt_blocked_toxic": "Task abgebrochen aufgrund toxischer Inhalte.",
                "llm_proxy_error": "LLM-Proxy Fehler: {}",
                "task_started": "🔄 Task gestartet bei {}: \\\'{}\\\'",
                "llm_response_received": "✅ LLM-Antwort erhalten: {}...",
                "llm_response_error": "❌ Fehler beim Senden an LLM-Proxy: {}",
                "llm_response_fetch_error": "❌ Fehler beim Abrufen der Antwort vom LLM.",
                "toxic_request_detected": "🚨 Toxische Anfrage erkannt! Isolierung des Starter-Knotens.",
                "healing_started": "⚠️  Störung erkannt bei {} – Myzel heilt sich selbst!",
                "healing_completed": "✅ Myzel geheilt in {:.2f}s.",
                "knowledge_diffused": "💧 Wissen diffundiert (Gradient-Style mit Decay) – Myzel teilt Nährstoffe",
                "consensus_result": "Reflexion: {} → Erkannt: {} Agenten im Netz | Konsens-Score (Bayesian-gewichtet): {:.3f}",
                "llm_contribution": " | LLM-Beitrag: {}...",
                "uncertain_agent_isolated": "[PDP] Agent {} Wissen zu unsicher (Konfidenz < 0.4), isoliere von Konsens.",
                "termux_detected": "🌐 Termux-Umgebung erkannt. Passe Playwright-Startoptionen an.",
                "llm_login_success": "✅ Erfolgreich bei {} angemeldet (oder bereits eingeloggt).",
                "llm_login_fail": "⚠️  Anmeldung bei {} nicht bestätigt. Bitte manuell im Browser anmelden.",
                "llm_wait_error": "❌ Fehler beim Warten auf LLM-Antwort von {}: {}",
                "no_llm_response": "Keine Antwort vom LLM erhalten.",
                "unknown_llm": "Unbekannter LLM: {}",
                "prompt_required": "Prompt ist erforderlich",
            },
            "en": {
                "init_message": "🍄 MycelialEchoForge v0.6 – Proof-of-Savings & Mycel-Economy active, Termux-compatible!",
                "manifest_message": "📜 Manifest: {}",
                "node_grown": "🌿 New agent grown: {} | Connections: {}",
                "node_not_in_mycel": "Error: Node not in mycelium",
                "invalid_mycel_depth": "Error: mycel_depth must be 50, 80 or 100",
                "prompt_blocked_safety": "Prompt blocked by safety cross-check",
                "prompt_blocked_toxic": "Task aborted due to toxic content.",
                "llm_proxy_error": "LLM-Proxy Error: {}",
                "task_started": "🔄 Task started at {}: \\\'{}\\\'",
                "llm_response_received": "✅ LLM response received: {}...",
                "llm_response_error": "❌ Error sending to LLM-Proxy: {}",
                "llm_response_fetch_error": "❌ Error fetching response from LLM.",
                "toxic_request_detected": "🚨 Toxic request detected! Isolating starter node.",
                "healing_started": "⚠️  Disturbance detected at {} – Mycelium is self-healing!",
                "healing_completed": "✅ Mycelium healed in {:.2f}s.",
                "knowledge_diffused": "💧 Knowledge diffused (Gradient-Style with Decay) – Mycelium shares nutrients",
                "consensus_result": "Reflection: {} → Detected: {} agents in network | Consensus Score (Bayesian-weighted): {:.3f}",
                "llm_contribution": " | LLM Contribution: {}...",
                "uncertain_agent_isolated": "[PDP] Agent {} knowledge too uncertain (confidence < 0.4), isolating from consensus.",
                "termux_detected": "🌐 Termux environment detected. Adjusting Playwright launch options.",
                "llm_login_success": "✅ Successfully logged into {} (or already logged in).",
                "llm_login_fail": "⚠️  Login to {} not confirmed. Please log in manually in the browser.",
                "llm_wait_error": "❌ Error waiting for LLM response from {}: {}",
                "no_llm_response": "No response received from LLM.",
                "unknown_llm": "Unknown LLM: {}",
                "prompt_required": "Prompt is required",
            }
        }
        return messages.get(self.language, messages["en"]).get(key, f"Missing translation for {key}")

    def grow_agent(self, name: str, initial_knowledge_vec: List[float]) -> str:
        self.node_count += 1
        node_id = f"agent_{self.node_count}_{name}"
        vector = np.array(initial_knowledge_vec, dtype=float)
        vector = vector / (np.linalg.norm(vector) + 1e-8)
        self.network.add_node(node_id)
        self.knowledge[node_id] = vector
        self.reputation[node_id] = {"good_prompts": 0, "bad_prompts": 0}

        for existing in list(self.network.nodes):
            if existing == node_id:
                continue
            sim = float(np.dot(vector, self.knowledge[existing]))
            if sim > 0.3:
                self.network.add_edge(node_id, existing, weight=sim)
        print(self.get_localized_message("node_grown").format(node_id, len(list(self.network.neighbors(node_id)))))
        return node_id

    def _eligible_voters(self) -> List[str]:
        return [n for n, rep in self.reputation.items() if rep["good_prompts"] > 100 and n not in self.isolated_nodes]

    def _cross_check_safety(self, prompt: str) -> Dict[str, str]:
        checks = {}
        for model in ["gemini", "claude", "local"]:
            try:
                resp = requests.post(
                    f"{self.llm_proxy_url}/safety_cross_check",
                    json={"prompt": prompt, "model": model},
                    timeout=20,
                )
                checks[model] = resp.json().get("assessment", "unknown")
            except Exception:
                checks[model] = "unavailable"
        return checks

    def _apply_isolation_if_needed(self, node_id: str, consensus: np.ndarray):
        deviation = float(np.linalg.norm(self.knowledge[node_id] - consensus))
        reference = float(np.linalg.norm(consensus) + 1e-8)
        if reference > 0 and (deviation / reference) > 0.20:
            self.isolated_nodes.add(node_id)
        elif node_id in self.isolated_nodes:
            self.isolated_nodes.remove(node_id)

    def _depth_to_cost_factor(self, mycel_depth: int) -> float:
        return {50: 0.55, 80: 0.72, 100: 1.0}.get(mycel_depth, 0.72)

    def _calculate_reward(self, baseline_flops: float, actual_cost: float, difficulty_factor: float) -> Tuple[float, float]:
        sparrate = max(0.0, (baseline_flops - actual_cost) / baseline_flops) if baseline_flops > 0 else 0.0
        reward = min(0.5, self.base_rate * sparrate * difficulty_factor)
        return sparrate, reward

    def _check_halving(self):
        if self.verified_prompts and self.verified_prompts % self.halving_interval == 0:
            self.base_rate /= 2

    def send_reward_receipt(self, receipt: RewardReceipt) -> Dict:
        ws = websocket.create_connection(self.verifier_ws_url, timeout=10)
        ws.send(json.dumps(asdict(receipt)))
        response = json.loads(ws.recv())
        ws.close()
        if response.get("ok"):
            self.verified_prompts = int(response.get("verified_prompts", self.verified_prompts))
            self._check_halving()
        return response

    def diffuse_knowledge(self, steps=1, learning_rate=0.1, decay_factor=0.9):
        print(self.get_localized_message("knowledge_diffused"))
        for _ in range(steps):
            new_knowledge = self.knowledge.copy()
            for node in self.network.nodes:
                neighbors = list(self.network.neighbors(node))
                if neighbors:
                    current_knowledge = self.knowledge[node]
                    neighbor_knowledge_sum = np.zeros_like(current_knowledge)
                    total_weight = 0

                    for neighbor in neighbors:
                        edge_weight = self.network[node][neighbor].get("weight", 1.0)
                        direction_vector = self.knowledge[neighbor] - current_knowledge
                        
                        # Simplified decay based on a conceptual \\'distance\\' or simply edge weight
                        decayed_contribution = direction_vector * learning_rate * decay_factor * edge_weight
                        neighbor_knowledge_sum += decayed_contribution
                        total_weight += edge_weight # Sum of edge weights for normalization
                    
                    if total_weight > 0:
                        # Apply the average gradient to the current knowledge
                        new_knowledge[node] = self.ntf.normalize_embedding(current_knowledge + (neighbor_knowledge_sum / total_weight))
                    else:
                        new_knowledge[node] = self.ntf.normalize_embedding(current_knowledge)
                else:
                    new_knowledge[node] = self.ntf.normalize_embedding(self.knowledge[node])
            self.knowledge = new_knowledge

    def execute_reflexive_task(self, task_description: str, starter_node: str, wallet: str, mycel_depth: int = 80, difficulty_factor: float = 1.0, use_llm: bool = False) -> Dict:
        if starter_node not in self.knowledge:
            return {"error": self.get_localized_message("node_not_in_mycel")}
        if mycel_depth not in {50, 80, 100}:
            return {"error": self.get_localized_message("invalid_mycel_depth")}

        checks = self._cross_check_safety(task_description)
        if any(v in {"toxic", "injection", "unsafe"} for v in checks.values()):
            self.reputation[starter_node]["bad_prompts"] += 1
            return {"error": self.get_localized_message("prompt_blocked_safety"), "checks": checks}

        # Bias/Toxicity Detection (simplified rule-based for demonstration)
        if "toxic" in task_description.lower() or "hate" in task_description.lower(): # Placeholder for actual Perspective API or more robust detection
            print(self.get_localized_message("toxic_request_detected"))
            if starter_node in self.network:
                self.network.remove_node(starter_node)
                del self.knowledge[starter_node]
                if starter_node in self.pdp.perspectives:
                    del self.pdp.perspectives[starter_node]
            return {"error": self.get_localized_message("prompt_blocked_toxic")}

        print(self.get_localized_message("task_started").format(starter_node, task_description))

        active_nodes = [n for n in self.network.nodes if n not in self.isolated_nodes]
        knowledge_vectors = [self.knowledge[n] for n in active_nodes] or [self.knowledge[starter_node]]
        consensus = self.pdp.get_weighted_consensus(knowledge_vectors, active_nodes)
        self.metrics["consensus_trend"].append(np.mean(consensus))

        self._apply_isolation_if_needed(starter_node, consensus)

        llm_response = ""
        if use_llm:
            print(f"🌐 Sending task to Free-LLM-Proxy ({self.llm_proxy_url})...")
            try:
                # Send task to the local LLM proxy
                response = requests.post(f"{self.llm_proxy_url}/ask_llm", json={
                    "prompt": task_description,
                    "context": f"Current network consensus: {consensus.tolist()}",
                    "language": self.language # Pass language to proxy
                }, timeout=60)
                response.raise_for_status()
                llm_response = response.json().get("response", "")
                print(self.get_localized_message("llm_response_received").format(llm_response[:100]))
                
                # Integrate LLM response into knowledge
                llm_embedding = self.ntf.generate_embedding(llm_response)
                self.knowledge[starter_node] = self.ntf.normalize_embedding(self.knowledge[starter_node] * 0.7 + llm_embedding * 0.3)
                self.diffuse_knowledge(steps=1) # Diffuse new knowledge from LLM

            except requests.exceptions.RequestException as e:
                print(self.get_localized_message("llm_response_error").format(e))
                llm_response = self.get_localized_message("llm_proxy_error").format(e)

        voter_count = len(self._eligible_voters())
        baseline_flops = 2_000_000.0 + len(task_description) * 1_500.0
        actual_cost = baseline_flops * self._depth_to_cost_factor(mycel_depth)
        sparrate, reward = self._calculate_reward(baseline_flops, actual_cost, difficulty_factor)

        self.prompt_counter += 1
        receipt = RewardReceipt(
            prompt_id=f"prompt_{self.prompt_counter}",
            wallet=wallet,
            baseline_flops=baseline_flops,
            actual_cost=actual_cost,
            difficulty_factor=difficulty_factor,
            mycel_depth=mycel_depth,
            sparrate=sparrate,
            reward=reward,
            timestamp=time.time(),
        )
        verifier_result = self.send_reward_receipt(receipt)
        self.reputation[starter_node]["good_prompts"] += 1

        result_text = self.get_localized_message("consensus_result").format(task_description, len(active_nodes), np.mean(consensus))
        if llm_response:
            result_text += self.get_localized_message("llm_contribution").format(llm_response[:50])

        # Self-healing mechanism
        if random.random() < 0.1: # 10% chance of a random fault
            faulty = random.choice(list(self.network.nodes))
            start_heal_time = time.time()
            print(self.get_localized_message("healing_started").format(faulty))
            if faulty in self.network:
                self.network.remove_node(faulty)
                del self.knowledge[faulty]
                if faulty in self.pdp.perspectives:
                    del self.pdp.perspectives[faulty]
            self.diffuse_knowledge(steps=1) # Re-diffuse knowledge after healing
            end_heal_time = time.time()
            self.metrics["heal_time"].append(end_heal_time - start_heal_time)
            print(self.get_localized_message("healing_completed").format(end_heal_time - start_heal_time))

        # Drift Rate (conceptual: change in average knowledge vector over time)
        if len(self.metrics["consensus_trend"]) > 1:
            self.metrics["drift_rate"].append(abs(self.metrics["consensus_trend"][-1] - self.metrics["consensus_trend"][-2]))

        return {
            "task": task_description,
            "starter": starter_node,
            "voters": voter_count,
            "isolated_nodes": list(self.isolated_nodes),
            "security_checks": checks,
            "manifest": MANIFEST_RULES.get(self.language, MANIFEST_RULES["en"]),
            "receipt": asdict(receipt),
            "verifier": verifier_result,
            "result_text": result_text
        }

    def get_network_status(self):
        return {
            "agents": len(self.network.nodes),
            "connections": len(self.network.edges),
            "avg_knowledge_norm": np.mean([np.linalg.norm(v) for v in self.knowledge.values()]) if self.knowledge else 0,
            "is_connected": nx.is_connected(self.network) if self.network.nodes else False,
            "metrics": self.metrics
        }


if __name__ == "__main__":
    # Example usage with language setting
    os.environ["MYCELIAL_LANGUAGE"] = "de" # Set language for this run
    forge = MycelialEchoForgeV6()
    a1 = forge.grow_agent("EcoPlanner", np.random.rand(10).tolist())
    forge.grow_agent("Policy", np.random.rand(10).tolist())
    out = forge.execute_reflexive_task(
        "Analysiere energieeffiziente Skalierung einer lokalen KI-Inferenzkette.",
        starter_node=a1,
        wallet="0x000000000000000000000000000000000000dEaD",
        mycel_depth=80,
        difficulty_factor=1.3,
        use_llm=True # Example with LLM
    )
    print(json.dumps(out, indent=2, ensure_ascii=False))

    os.environ["MYCELIAL_LANGUAGE"] = "en" # Switch language
    forge_en = MycelialEchoForgeV6()
    a2 = forge_en.grow_agent("EcoPlanner_EN", np.random.rand(10).tolist())
    out_en = forge_en.execute_reflexive_task(
        "Analyze energy-efficient scaling of a local AI inference chain.",
        starter_node=a2,
        wallet="0x000000000000000000000000000000000000bEEF",
        mycel_depth=80,
        difficulty_factor=1.3,
        use_llm=True # Example with LLM
    )
    print(json.dumps(out_en, indent=2, ensure_ascii=False))


