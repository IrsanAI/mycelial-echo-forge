
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
        print(f"🔄 Task gestartet bei {starter_node}: '{task_description}'")
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
