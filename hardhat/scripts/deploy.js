const hre = require("hardhat");

async function main() {
  const baseRate = hre.ethers.parseUnits(process.env.MYC_BASE_RATE || "0.05", 18);
  const myc = await hre.ethers.deployContract("MycToken", [baseRate]);
  await myc.waitForDeployment();

  console.log("MycToken deployed to:", await myc.getAddress());
  console.log("BaseRate:", (await myc.baseRate()).toString());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
