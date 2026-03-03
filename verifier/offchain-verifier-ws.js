require("dotenv").config();
const WebSocket = require("ws");
const { ethers } = require("ethers");
const fs = require("fs");
const path = require("path");

const PORT = Number(process.env.VERIFIER_PORT || 8080);
const RECEIPT_BATCH_SIZE = Number(process.env.RECEIPT_BATCH_SIZE || 20);
const HALVING_INTERVAL = 10_000_000;
const MAX_REWARD = 0.5;

const artifactPath = path.resolve(__dirname, "../hardhat/artifacts/contracts/MycToken.sol/MycToken.json");
const artifact = fs.existsSync(artifactPath) ? JSON.parse(fs.readFileSync(artifactPath, "utf8")) : null;

const state = {
  verifiedPrompts: 0,
  baseRate: Number(process.env.MYC_BASE_RATE || 0.05),
  queue: []
};

const provider = process.env.RPC_URL ? new ethers.JsonRpcProvider(process.env.RPC_URL) : null;
const wallet = process.env.OWNER_PRIVATE_KEY && provider ? new ethers.Wallet(process.env.OWNER_PRIVATE_KEY, provider) : null;
const contract = process.env.MYC_TOKEN_ADDRESS && artifact && wallet
  ? new ethers.Contract(process.env.MYC_TOKEN_ADDRESS, artifact.abi, wallet)
  : null;

function computeReward(receipt) {
  const baseline = Number(receipt.baseline_flops);
  const actual = Number(receipt.actual_cost);
  const difficulty = Number(receipt.difficulty_factor || 1.0);

  if (!Number.isFinite(baseline) || baseline <= 0) return { reward: 0, sparrate: 0 };
  if (!Number.isFinite(actual) || actual < 0) return { reward: 0, sparrate: 0 };

  const sparrate = Math.max(0, (baseline - actual) / baseline);
  const reward = Math.min(MAX_REWARD, state.baseRate * sparrate * difficulty);
  return { reward, sparrate };
}

async function maybeHalveBaseRate() {
  if (state.verifiedPrompts > 0 && state.verifiedPrompts % HALVING_INTERVAL === 0) {
    state.baseRate = state.baseRate / 2;
    if (contract) {
      const tx = await contract.halveBaseRate();
      await tx.wait();
    }
    console.log(`[halving] Neue baseRate=${state.baseRate}`);
  }
}

async function flushMints() {
  if (!state.queue.length) return;
  const batch = state.queue.splice(0, RECEIPT_BATCH_SIZE);
  const recipients = batch.map((b) => b.wallet);
  const amounts = batch.map((b) => ethers.parseUnits(String(b.reward), 18));

  if (contract) {
    const tx = await contract.batchMint(recipients, amounts);
    await tx.wait();
    console.log(`[mint] ${batch.length} Rewards on-chain gemintet.`);
  } else {
    console.log(`[dry-run] ${batch.length} Rewards berechnet, kein Contract konfiguriert.`);
  }
}

const wss = new WebSocket.Server({ port: PORT }, () => {
  console.log(`Verifier WS läuft auf ws://0.0.0.0:${PORT}`);
});

wss.on("connection", (ws) => {
  ws.on("message", async (raw) => {
    try {
      const receipt = JSON.parse(raw.toString());
      const { reward, sparrate } = computeReward(receipt);
      state.verifiedPrompts += 1;
      await maybeHalveBaseRate();

      const enriched = {
        ...receipt,
        sparrate,
        reward,
        verified_at: new Date().toISOString()
      };

      if (reward > 0 && receipt.wallet) {
        state.queue.push(enriched);
      }

      if (state.queue.length >= RECEIPT_BATCH_SIZE) {
        await flushMints();
      }

      ws.send(JSON.stringify({ ok: true, ...enriched, verified_prompts: state.verifiedPrompts }));
    } catch (error) {
      ws.send(JSON.stringify({ ok: false, error: error.message }));
    }
  });
});

process.on("SIGINT", async () => {
  try {
    await flushMints();
  } finally {
    process.exit(0);
  }
});
