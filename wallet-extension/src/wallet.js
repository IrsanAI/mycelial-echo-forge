import React, { useMemo, useState } from "react";

const depthMap = {
  50: "Eco",
  80: "Balanced",
  100: "Full"
};

export function WalletApp() {
  const [depth, setDepth] = useState(80);
  const [balance] = useState(142.37);
  const [savedKwh] = useState(21.84);
  const [rewards] = useState([
    { id: 1, task: "Policy Draft", amount: 0.24 },
    { id: 2, task: "Code Refactor", amount: 0.11 },
    { id: 3, task: "Safety Audit", amount: 0.35 }
  ]);

  const avgReward = useMemo(
    () => rewards.reduce((acc, r) => acc + r.amount, 0) / rewards.length,
    [rewards]
  );

  return (
    <main className="wallet">
      <h1>🍄 MYC Wallet</h1>
      <section className="card">
        <h2>Mycel-Depth</h2>
        <input
          type="range"
          min="50"
          max="100"
          step="30"
          value={depth}
          onChange={(e) => setDepth(Number(e.target.value))}
        />
        <p>{depth}% · {depthMap[depth]}</p>
      </section>

      <section className="card stats">
        <p>Balance: <strong>{balance.toFixed(2)} MYC</strong></p>
        <p>Energy saved: <strong>{savedKwh.toFixed(2)} kWh</strong></p>
        <p>Avg reward: <strong>{avgReward.toFixed(2)} MYC</strong></p>
      </section>

      <section className="card">
        <h2>Recent rewards</h2>
        <ul>
          {rewards.map((r) => (
            <li key={r.id}>{r.task} <span>+{r.amount.toFixed(2)} MYC</span></li>
          ))}
        </ul>
      </section>
    </main>
  );
}
