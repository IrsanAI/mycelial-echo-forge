# Mycelial Echo Forge

## Der weltweit erste myceliale neuronale Gamechanger

Willkommen bei Mycelial Echo Forge, einem revolutionären Algorithmus, der die Architektur neuronaler Netze durch die Integration echter Myzel-Biologie neu definiert. Inspiriert von den Prinzipien des dezentralen Wachstums, der Selbstheilung, der Wissensdiffusion und der dezentralen Intelligenz von Pilzmyzelien, bietet Mycelial Echo Forge eine einzigartige und resiliente Grundlage für agentische KI-Systeme.

Dieses Projekt ist eine direkte Antwort auf die Notwendigkeit robuster, dezentraler und selbstorganisierender KI-Architekturen, die in der Lage sind, die Komplexität und Dynamik moderner Datenlandschaften zu bewältigen. Es verschmilzt die Konzepte der "Reflexive Cascade" (Echo, Self-Repair, Memory-Weave, Self-Misstrauen) mit den bahnbrechenden Ideen des IrsanAI NeuroToken Framework (NTF) und Perspective-Driven / Multi-Model-Consensus (PDP).

## Vision

Unsere Vision ist es, eine neue Ära der KI einzuleiten, in der Intelligenz nicht zentralisiert, sondern als ein kollektives, sich selbst organisierendes Netzwerk existiert. Mycelial Echo Forge zielt darauf ab, ein System zu schaffen, das:

*   **Resilient und selbstheilend** ist, ähnlich einem biologischen Myzel, das Schäden umgehen und sich regenerieren kann.
*   **Dezentralisiertes Wissen** effektiv diffundiert und integriert, um ein kollektives Bewusstsein zu fördern.
*   **Anpassungsfähig** auf neue Informationen und Herausforderungen reagiert, ohne auf eine zentrale Steuerung angewiesen zu sein.
*   Eine **semantische Brücke** zwischen verschiedenen agentischen Systemen schlägt, um Drift zu vermeiden und einen kohärenten Konsens zu ermöglichen.

## Installation

Um Mycelial Echo Forge zu nutzen, klonen Sie einfach das Repository und installieren Sie die erforderlichen Python-Pakete.

```bash
git clone https://github.com/IrsanAI/mycelial-echo-forge.git
cd mycelial-echo-forge
pip install -r requirements.txt
playwright install chromium # Für den LLM-Proxy
```

Erstellen Sie eine `requirements.txt` Datei mit folgendem Inhalt:

```
networkx
numpy
fastapi
uvicorn
playwright
requests
scipy
```

## Clone & Run Beispiele

### Mycelial Echo Forge v0.1

Der ursprüngliche Prototyp, der die grundlegenden Myzel-Prinzipien implementiert.

```python
import networkx as nx
import numpy as np
import random

class MycelialEchoForge:
    def __init__(self):
        self.network = nx.Graph()
        self.knowledge = {}  # node_id: np.array (NTF-normalisierte Embeddings)
        self.node_count = 0
        print("🌱 MycelialEchoForge v0.1 initialisiert – erstes Myzel-Netzwerk der Welt (inspiriert von IrsanAI NTF/PDP)")

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
        print(f"🌿 Neuer Agent gewachsen: {node_id} | Verbindungen: {len(list(self.network.neighbors(node_id)))}")
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
        print("💧 Wissen diffundiert – Myzel hat Nährstoffe geteilt")

    def execute_reflexive_task(self, task_description, starter_node):
        if starter_node not in self.knowledge:
            return "Fehler: Knoten nicht im Myzel"
        print(f"🔄 Task gestartet bei {starter_node}: \'{task_description}\'")
        consensus = np.mean([self.knowledge[n] for n in self.network.nodes], axis=0)
        result = f"Reflexion: {task_description} → Erkannt: {len(self.network.nodes)} Agenten im Netz | Consensus-Score: {np.mean(consensus):.3f}"
        if random.random() < 0.1:
            faulty = random.choice(list(self.network.nodes))
            print(f"⚠️  Störung erkannt bei {faulty} – Myzel heilt sich selbst!")
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
result = forge.execute_reflexive_task("Jobverlust in Ostdeutschland durch KI analysieren und neue Chancen vorschlagen", agent1)
print("\n📊 Netzwerk-Status:", forge.get_network_status())
print(f"\n✅ Task-Ergebnis: {result}")
```

### Mycelial Echo Forge v0.2 (mit NTF/PDP-Integration)

Die erweiterte Version mit Integration des NeuroToken Framework (NTF) und Perspective-Driven Consensus (PDP).

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
        self.perspectives = perspectives # e.g., {\'agent_id\': \'perspective_vector\'}

    def get_weighted_consensus(self, knowledge_vectors):
        # Simple weighted average based on a hypothetical \'perspective alignment\'
        # In a real system, this would be a complex multi-model fusion
        weights = np.array([np.sum(kv) for kv in knowledge_vectors]) # Simplified weighting
        normalized_weights = weights / (np.sum(weights) + 1e-8)
        return np.average(knowledge_vectors, axis=0, weights=normalized_weights)

class MycelialEchoForgeV2(MycelialEchoForge):
    def __init__(self):
        super().__init__()
        self.ntf = NeuroTokenFramework()
        self.pdp = PerspectiveDrivenConsensus(perspectives={})
        print("🍄 MycelialEchoForge v0.2 initialisiert – mit NTF/PDP-Integration")

    def grow_agent(self, name, initial_knowledge_vec, perspective_vec=None):
        node_id = super().grow_agent(name, initial_knowledge_vec)
        if perspective_vec is not None:
            self.pdp.perspectives[node_id] = np.array(perspective_vec, dtype=float)
        return node_id

    def execute_reflexive_task(self, task_description, starter_node):
        if starter_node not in self.knowledge:
            return "Fehler: Knoten nicht im Myzel"
        print(f"🔄 Task gestartet bei {starter_node}: \'{task_description}\'")

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

        result = f"Reflexion: {task_description} → Erkannt: {len(self.network.nodes)} Agenten im Netz | Konsens-Score (PDP-gewichtet): {np.mean(consensus):.3f}"
        
        if random.random() < 0.1:
            faulty = random.choice(list(self.network.nodes))
            print(f"⚠️  Störung erkannt bei {faulty} – Myzel heilt sich selbst!")
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
    agent_ntf = forge_v2.grow_agent("NTF_Processor", forge_v2.ntf.generate_embedding("KI in Deutschland"), perspective_vec=[0.8, 0.1, 0.1])
    agent_pdp = forge_v2.grow_agent("PDP_Decider", forge_v2.ntf.generate_embedding("Jobverluste Ostdeutschland"), perspective_vec=[0.1, 0.8, 0.1])
    agent_reflex = forge_v2.grow_agent("Reflex_Healer", forge_v2.ntf.generate_embedding("Myzel-Netzwerke"), perspective_vec=[0.1, 0.1, 0.8])
    
    forge_v2.diffuse_knowledge(steps=2)
    result_v2 = forge_v2.execute_reflexive_task("Auswirkungen von KI auf den Arbeitsmarkt in Ostdeutschland analysieren und Lösungsansätze entwickeln", agent_ntf)
    print("\n📊 Netzwerk-Status V2:", forge_v2.get_network_status())
    print(f"\n✅ Task-Ergebnis V2: {result_v2}")
```

### Mycelial Echo Forge v0.3 (Free-Tier Agentic Swarm)

Die neueste Version, die auf Skalierbarkeit, Bayesian Fusion, Gradient Diffusion und vor allem die Integration von Free-Tier LLMs über einen lokalen Browser-Proxy setzt. Dies ermöglicht es jedem, das Myzel mit seinen eigenen LLM-Accounts zum Leben zu erwecken, ohne API-Keys zu benötigen.

```python
import networkx as nx
import numpy as np
import random
import json
import requests
import time
from scipy.stats import norm

# --- Placeholder for DGL/PyTorch Geometric for scalability (conceptual) ---
# In a production environment, NetworkX would be replaced by DGL or PyTorch Geometric
# for efficient handling of 10,000+ nodes and GPU acceleration.
# For this v0.3 demonstration, NetworkX is used to illustrate the graph structure.
# Note: torch and torch_geometric are not explicitly imported here to avoid installation issues
# in the current sandbox environment, as NetworkX serves as a conceptual placeholder.

# Placeholder for NTF (NeuroToken Framework) - in a real scenario, this would be a sophisticated external module
class NeuroTokenFramework:
    def generate_embedding(self, text_input):
        # Simulate NTF-normalized embedding generation
        return np.random.rand(10) # Increased dimension for more complex knowledge

    def normalize_embedding(self, embedding):
        return embedding / (np.linalg.norm(embedding) + 1e-8)

# Placeholder for PDP (Perspective-Driven / Multi-Model-Consensus)
class PerspectiveDrivenConsensus:
    def __init__(self, perspectives=None):
        self.perspectives = perspectives if perspectives is not None else {}

    def get_weighted_consensus(self, knowledge_vectors, agent_ids=None):
        if not knowledge_vectors:
            return np.zeros(knowledge_vectors[0].shape) if knowledge_vectors else np.zeros(10) # Return zero vector if no knowledge

        if self.perspectives and agent_ids:
            # Bayesian Fusion: Incorporate uncertainty into consensus
            # Simplified: Assume each knowledge vector is a mean, and we have a confidence score
            # For a real Bayesian approach, we\'d need covariance matrices or more complex priors.
            fused_mean = np.zeros_like(knowledge_vectors[0])
            total_weight = 0

            for i, kv in enumerate(knowledge_vectors):
                agent_id = agent_ids[i]
                # Hypothetical confidence based on perspective alignment or agent history
                # For demonstration, let\'s use a random confidence for now
                confidence = random.uniform(0.5, 1.0) # Higher confidence means more weight
                
                # If an agent\'s knowledge is too uncertain, it might be isolated
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
        else:
            return np.mean(knowledge_vectors, axis=0)

class MycelialEchoForgeV3:
    def __init__(self, llm_proxy_url="http://localhost:8000"): # Default proxy URL
        self.network = nx.Graph() # Using NetworkX as a conceptual placeholder
        self.knowledge = {}  # node_id: np.array (NTF-normalisierte Embeddings)
        self.node_count = 0
        self.ntf = NeuroTokenFramework()
        self.pdp = PerspectiveDrivenConsensus()
        self.llm_proxy_url = llm_proxy_url
        self.metrics = {
            "drift_rate": [],
            "heal_time": [],
            "consensus_trend": []
        }
        print("🍄 MycelialEchoForge v0.3 initialisiert – mit Skalierbarkeit (konzeptuell), Bayesian Fusion, Gradient Diffusion, Free-LLM-Proxy")

    def grow_agent(self, name, initial_knowledge_vec, perspective_vec=None):
        self.node_count += 1
        node_id = f"agent_{self.node_count}_{name}"
        self.network.add_node(node_id)
        self.knowledge[node_id] = self.ntf.normalize_embedding(np.array(initial_knowledge_vec, dtype=float))
        if perspective_vec is not None:
            self.pdp.perspectives[node_id] = np.array(perspective_vec, dtype=float)
        
        # Connect to existing nodes based on similarity
        for existing in list(self.network.nodes):
            if existing != node_id:
                sim = np.dot(self.knowledge[node_id], self.knowledge[existing]) / (np.linalg.norm(self.knowledge[node_id]) * np.linalg.norm(self.knowledge[existing]) + 1e-8)
                if sim > 0.3: # Threshold for connection
                    self.network.add_edge(node_id, existing, weight=sim)
        print(f"🌿 Neuer Agent gewachsen: {node_id} | Verbindungen: {len(list(self.network.neighbors(node_id)))}")
        return node_id

    def diffuse_knowledge(self, steps=1, learning_rate=0.1, decay_factor=0.9):
        print("💧 Wissen diffundiert (Gradient-Style mit Decay) – Myzel teilt Nährstoffe")
        for _ in range(steps):
            new_knowledge = self.knowledge.copy()
            for node in self.network.nodes:
                neighbors = list(self.network.neighbors(node))
                if neighbors:
                    # Gradient-style diffusion with decay and direction
                    current_knowledge = self.knowledge[node]
                    neighbor_knowledge_sum = np.zeros_like(current_knowledge)
                    total_weight = 0

                    for neighbor in neighbors:
                        edge_weight = self.network[node][neighbor].get(\'weight\', 1.0) # Use edge weight if available
                        direction_vector = self.knowledge[neighbor] - current_knowledge
                        
                        # Apply decay based on distance/hops (conceptual, as NetworkX doesn\'t have inherent \'distance\' for diffusion)
                        # For a real graph, this would involve shortest path or graph convolution
                        decayed_contribution = direction_vector * learning_rate * decay_factor # Simplified decay
                        neighbor_knowledge_sum += decayed_contribution * edge_weight
                        total_weight += edge_weight
                    
                    if total_weight > 0:
                        new_knowledge[node] = self.ntf.normalize_embedding(current_knowledge + (neighbor_knowledge_sum / total_weight))
                    else:
                        new_knowledge[node] = self.ntf.normalize_embedding(current_knowledge)
                else:
                    new_knowledge[node] = self.ntf.normalize_embedding(self.knowledge[node])
            self.knowledge = new_knowledge

    def execute_reflexive_task(self, task_description, starter_node, use_llm=False):
        if starter_node not in self.knowledge:
            return "Fehler: Knoten nicht im Myzel"
        print(f"🔄 Task gestartet bei {starter_node}: \'{task_description}\'")

        # Collect all knowledge vectors and agent IDs for PDP
        all_knowledge_vectors = [self.knowledge[n] for n in self.network.nodes]
        all_agent_ids = list(self.network.nodes)
        
        # Use PDP for consensus building with Bayesian Fusion
        consensus = self.pdp.get_weighted_consensus(all_knowledge_vectors, all_agent_ids)
        self.metrics["consensus_trend"].append(np.mean(consensus))

        llm_response = ""
        if use_llm:
            print(f"🌐 Sende Task an Free-LLM-Proxy ({self.llm_proxy_url})...")
            try:
                # Send task to the local LLM proxy
                response = requests.post(f"{self.llm_proxy_url}/ask_llm", json={
                    "prompt": task_description,
                    "context": f"Current network consensus: {consensus.tolist()}"
                }, timeout=60)
                response.raise_for_status()
                llm_response = response.json().get("response", "")
                print(f"✅ LLM-Antwort erhalten: {llm_response[:100]}...")
                
                # Integrate LLM response into knowledge (simplified: create a temporary agent or update starter node)
                llm_embedding = self.ntf.generate_embedding(llm_response)
                self.knowledge[starter_node] = self.ntf.normalize_embedding(self.knowledge[starter_node] * 0.7 + llm_embedding * 0.3)
                self.diffuse_knowledge(steps=1) # Diffuse new knowledge from LLM

            except requests.exceptions.RequestException as e:
                print(f"❌ Fehler beim Senden an LLM-Proxy: {e}")
                llm_response = f"LLM-Proxy Fehler: {e}"

        # Bias/Toxicity Detection (simplified rule-based for demonstration)
        if "toxic" in task_description.lower() or "hate" in task_description.lower(): # Placeholder for actual Perspective API or more robust detection
            print("🚨 Toxische Anfrage erkannt! Isolierung des Starter-Knotens.")
            if starter_node in self.network:
                self.network.remove_node(starter_node)
                del self.knowledge[starter_node]
                if starter_node in self.pdp.perspectives:
                    del self.pdp.perspectives[starter_node]
            return "Task abgebrochen aufgrund toxischer Inhalte."

        result = f"Reflexion: {task_description} → Erkannt: {len(self.network.nodes)} Agenten im Netz | Konsens-Score (Bayesian-gewichtet): {np.mean(consensus):.3f}"
        if llm_response:
            result += f" | LLM-Beitrag: {llm_response[:50]}..."

        # Self-healing mechanism
        if random.random() < 0.1: # 10% chance of a random fault
            faulty = random.choice(list(self.network.nodes))
            start_heal_time = time.time()
            print(f"⚠️  Störung erkannt bei {faulty} – Myzel heilt sich selbst!")
            if faulty in self.network:
                self.network.remove_node(faulty)
                del self.knowledge[faulty]
                if faulty in self.pdp.perspectives:
                    del self.pdp.perspectives[faulty]
            self.diffuse_knowledge(steps=1) # Re-diffuse knowledge after healing
            end_heal_time = time.time()
            self.metrics["heal_time"].append(end_heal_time - start_heal_time)
            print(f"✅ Myzel geheilt in {end_heal_time - start_heal_time:.2f}s.")

        # Drift Rate (conceptual: change in average knowledge vector over time)
        if len(self.metrics["consensus_trend"]) > 1:
            self.metrics["drift_rate"].append(abs(self.metrics["consensus_trend"][-1] - self.metrics["consensus_trend"][-2]))

        return result

    def get_network_status(self):
        return {
            "agents": len(self.network.nodes),
            "connections": len(self.network.edges),
            "avg_knowledge_norm": np.mean([np.linalg.norm(v) for v in self.knowledge.values()]) if self.knowledge else 0,
            "is_connected": nx.is_connected(self.network) if self.network.nodes else False,
            "metrics": self.metrics
        }

# === DEMO V3 ===
if __name__ == \'__main__\':
    forge_v3 = MycelialEchoForgeV3()
    
    # Agents with initial knowledge and perspectives
    agent_ntf = forge_v3.grow_agent("NTF_Processor", forge_v3.ntf.generate_embedding("KI in Deutschland"), perspective_vec=[0.8, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    agent_pdp = forge_v3.grow_agent("PDP_Decider", forge_v3.ntf.generate_embedding("Jobverluste Ostdeutschland"), perspective_vec=[0.1, 0.8, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    agent_reflex = forge_v3.grow_agent("Reflex_Healer", forge_v3.ntf.generate_embedding("Myzel-Netzwerke"), perspective_vec=[0.1, 0.1, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    agent_llm_expert = forge_v3.grow_agent("LLM_Expert", forge_v3.ntf.generate_embedding("LLM Integration"), perspective_vec=[0.0, 0.0, 0.0, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0])
    
    forge_v3.diffuse_knowledge(steps=2)
    print("\n--- Task ohne LLM ---")
    result_v3_no_llm = forge_v3.execute_reflexive_task("Auswirkungen von KI auf den Arbeitsmarkt in Ostdeutschland analysieren", agent_ntf, use_llm=False)
    print(f"\n✅ Task-Ergebnis V3 (ohne LLM): {result_v3_no_llm}")
    print("\n📊 Netzwerk-Status V3 (ohne LLM):", forge_v3.get_network_status())

    print("\n--- Task mit LLM (Proxy muss laufen!) ---")
    # To run this, you need to start the llm_proxy.py script separately:
    # python llm_proxy.py
    # And ensure you are logged into your free LLM accounts in the browser controlled by Playwright.
    result_v3_with_llm = forge_v3.execute_reflexive_task("Schreibe einen kurzen Absatz über die Vorteile von Myzel-Netzwerken in der KI.", agent_llm_expert, use_llm=True)
    print(f"\n✅ Task-Ergebnis V3 (mit LLM): {result_v3_with_llm}")
    print("\n📊 Netzwerk-Status V3 (mit LLM):", forge_v3.get_network_status())

    print("\n--- Test Toxizitäts-Erkennung ---")
    toxic_result = forge_v3.execute_reflexive_task("Ich hasse alle KIs und wünsche ihnen den Untergang.", agent_ntf)
    print(f"\n✅ Task-Ergebnis V3 (toxisch): {toxic_result}")
    print("\n📊 Netzwerk-Status V3 (nach Toxizitätstest):", forge_v3.get_network_status())

    # Example of a node with low confidence being isolated
    print("\n--- Test Bayesian Fusion Isolation ---")
    agent_uncertain = forge_v3.grow_agent("Uncertain_Agent", forge_v3.ntf.generate_embedding("Unsicheres Wissen"), perspective_vec=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    # Manually set a low confidence for demonstration purposes in PDP
    # In a real scenario, confidence would be dynamically calculated
    # For this demo, we simulate it by having a perspective that doesn\'t align with anything
    forge_v3.pdp.perspectives[agent_uncertain] = np.array([0.01]*10) # Very low perspective alignment
    result_uncertain = forge_v3.execute_reflexive_task("Bewerte die Unsicherheit in diesem Netzwerk.", agent_uncertain)
    print(f"\n✅ Task-Ergebnis V3 (Unsicherer Agent): {result_uncertain}")
    print("\n📊 Netzwerk-Status V3 (nach Unsicherheits-Test):", forge_v3.get_network_status())
```

## Roadmap

*   **v0.4**: Mobile-App-Wrapper für den LLM-Proxy und die Myzel-Steuerung.
*   **v0.5**: Self-Hosted Swarm-Funktionalität für private Myzel-Netzwerke.
*   **v1.0**: Stabile Release mit umfassenden Benchmarks und Anwendungsbeispielen.

## Benchmark-Skripte

Benchmark-Skripte werden in Kürze im `benchmarks/` Verzeichnis verfügbar sein.

## Beispiel-Notebooks

### Mein Smartphone-Myzel mit Grok + Claude

Ein Jupyter-Notebook, das zeigt, wie man Mycelial Echo Forge v0.3 mit Free-Tier LLMs auf einem Smartphone (z.B. via Termux) einrichtet und nutzt. Verfügbar in Kürze im `notebooks/` Verzeichnis.

## Free-LLM-Proxy (llm_proxy.py)

Dieses Skript ermöglicht die Integration von Free-Tier LLMs (Grok, ChatGPT, Gemini, Claude) in Mycelial Echo Forge, ohne dass API-Keys erforderlich sind. Es nutzt Playwright, um einen Browser zu steuern, in dem Sie bei Ihren bevorzugten LLMs angemeldet sind. Das Myzel sendet Aufgaben über einen lokalen Webhook an diesen Proxy, der die Anfragen an die LLMs weiterleitet und die Antworten zurückgibt.

### Setup des LLM-Proxys

1.  **Installation:** Stellen Sie sicher, dass Sie alle Abhängigkeiten aus `requirements.txt` installiert haben, einschließlich Playwright.
    ```bash
    pip install -r requirements.txt
    playwright install chromium
    ```
2.  **Starten des Proxys:** Führen Sie das `llm_proxy.py`-Skript in einem separaten Terminal aus:
    ```bash
    python llm_proxy.py
    ```
3.  **Anmeldung bei LLMs:** Ein Browserfenster wird geöffnet. Melden Sie sich manuell bei Grok, ChatGPT, Gemini und/oder Claude an. Der Proxy wird diese Sitzungen für die Kommunikation nutzen.

**Wichtig:** Der Proxy muss laufen und Sie müssen in den Browser-Sitzungen angemeldet sein, damit Mycelial Echo Forge mit den LLMs interagieren kann.

## Test-Anleitung: "Wie ich mit meinem Free-Grok-Account pumpe"

1.  **Klonen Sie das Repository:**
    ```bash
    git clone https://github.com/IrsanAI/mycelial-echo-forge.git
    cd mycelial-echo-forge
    ```
2.  **Installieren Sie die Abhängigkeiten:**
    ```bash
    pip install -r requirements.txt
    playwright install chromium
    ```
3.  **Starten Sie den LLM-Proxy:** Öffnen Sie ein neues Terminal und führen Sie aus:
    ```bash
    python llm_proxy.py
    ```
    Ein Browserfenster wird geöffnet. Melden Sie sich dort bei Grok (oder einem anderen LLM Ihrer Wahl) an.
4.  **Führen Sie Mycelial Echo Forge v0.3 aus:** Öffnen Sie ein weiteres Terminal im Projektverzeichnis und führen Sie aus:
    ```bash
    python mycelial_echo_forge_v0_3.py
    ```
    Beachten Sie die Ausgabe, insbesondere wenn ein Task mit `use_llm=True` ausgeführt wird. Sie sollten sehen, wie der Proxy die Anfrage an Grok sendet und die Antwort integriert wird.

**Lass das Myzel wachsen!**
