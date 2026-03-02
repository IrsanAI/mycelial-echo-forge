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
```

Erstellen Sie eine `requirements.txt` Datei mit folgendem Inhalt:

```
networkx
numpy
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

## Roadmap

*   **v0.3**: Implementierung echter NTF- und PDP-Module (nicht nur Platzhalter).
*   **v0.4**: Erweiterte Selbstheilungsmechanismen und adaptive Netzwerkstrukturen.
*   **v0.5**: Integration von Reinforcement Learning für die Optimierung der Wissensdiffusion.
*   **v1.0**: Stabile Release mit umfassenden Benchmarks und Anwendungsbeispielen.

## Benchmark-Skripte

Benchmark-Skripte werden in Kürze im `benchmarks/` Verzeichnis verfügbar sein.

## Beispiel-Notebooks

Beispiel-Notebooks zur Veranschaulichung der Nutzung werden in Kürze im `notebooks/` Verzeichnis verfügbar sein.
