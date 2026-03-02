
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
        self.perspectives = perspectives # e.g., {'agent_id': 'perspective_vector'}

    def get_weighted_consensus(self, knowledge_vectors):
        # Simple weighted average based on a hypothetical 'perspective alignment'
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
        print(f"🔄 Task gestartet bei {starter_node}: '{task_description}'")

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
if __name__ == '__main__':
    forge_v2 = MycelialEchoForgeV2()
    
    # Agents with initial knowledge and perspectives
    agent_ntf = forge_v2.grow_agent("NTF_Processor", forge_v2.ntf.generate_embedding("KI in Deutschland"), perspective_vec=[0.8, 0.1, 0.1])
    agent_pdp = forge_v2.grow_agent("PDP_Decider", forge_v2.ntf.generate_embedding("Jobverluste Ostdeutschland"), perspective_vec=[0.1, 0.8, 0.1])
    agent_reflex = forge_v2.grow_agent("Reflex_Healer", forge_v2.ntf.generate_embedding("Myzel-Netzwerke"), perspective_vec=[0.1, 0.1, 0.8])
    
    forge_v2.diffuse_knowledge(steps=2)
    result_v2 = forge_v2.execute_reflexive_task("Auswirkungen von KI auf den Arbeitsmarkt in Ostdeutschland analysieren und Lösungsansätze entwickeln", agent_ntf)
    print("\n📊 Netzwerk-Status V2:", forge_v2.get_network_status())
    print(f"\n✅ Task-Ergebnis V2: {result_v2}")
