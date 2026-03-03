import json
import random
import time
from dataclasses import dataclass, asdict
from typing import Dict, List, Tuple

import networkx as nx
import numpy as np
import requests
import websocket


MANIFEST_RULES = [
    "1. Never execute code.",
    "2. Never leak personal data.",
    "3. Always prefer energy-efficient paths.",
]


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


class MycelialEchoForgeV5:
    def __init__(self, llm_proxy_url: str = "http://localhost:8000", verifier_ws_url: str = "ws://localhost:8080"):
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
        print("🍄 MycelialEchoForge v0.5 – Proof-of-Savings & Mycel-Economy aktiv")
        print("📜 Manifest:", " | ".join(MANIFEST_RULES))

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

    def execute_reflexive_task(self, task_description: str, starter_node: str, wallet: str, mycel_depth: int = 80, difficulty_factor: float = 1.0) -> Dict:
        if starter_node not in self.knowledge:
            return {"error": "Knoten nicht im Myzel"}
        if mycel_depth not in {50, 80, 100}:
            return {"error": "mycel_depth muss 50, 80 oder 100 sein"}

        checks = self._cross_check_safety(task_description)
        if any(v in {"toxic", "injection", "unsafe"} for v in checks.values()):
            self.reputation[starter_node]["bad_prompts"] += 1
            return {"error": "Prompt durch Sicherheits-Cross-Check blockiert", "checks": checks}

        active_nodes = [n for n in self.network.nodes if n not in self.isolated_nodes]
        knowledge_vectors = [self.knowledge[n] for n in active_nodes] or [self.knowledge[starter_node]]
        consensus = np.mean(knowledge_vectors, axis=0)

        self._apply_isolation_if_needed(starter_node, consensus)

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

        return {
            "task": task_description,
            "starter": starter_node,
            "voters": voter_count,
            "isolated_nodes": list(self.isolated_nodes),
            "security_checks": checks,
            "manifest": MANIFEST_RULES,
            "receipt": asdict(receipt),
            "verifier": verifier_result,
        }


if __name__ == "__main__":
    forge = MycelialEchoForgeV5()
    a1 = forge.grow_agent("EcoPlanner", np.random.rand(10).tolist())
    forge.grow_agent("Policy", np.random.rand(10).tolist())
    out = forge.execute_reflexive_task(
        "Analysiere energieeffiziente Skalierung einer lokalen KI-Inferenzkette.",
        starter_node=a1,
        wallet="0x000000000000000000000000000000000000dEaD",
        mycel_depth=80,
        difficulty_factor=1.3,
    )
    print(json.dumps(out, indent=2, ensure_ascii=False))
