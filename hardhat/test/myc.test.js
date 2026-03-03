const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("MycToken", function () {
  async function setup() {
    const [owner, alice, bob] = await ethers.getSigners();
    const baseRate = ethers.parseEther("0.05");
    const token = await ethers.deployContract("MycToken", [baseRate]);
    await token.waitForDeployment();
    return { token, owner, alice, bob, baseRate };
  }

  it("setzt Metadaten, maxSupply und baseRate", async function () {
    const { token, baseRate } = await setup();
    expect(await token.name()).to.equal("Mycelial Credit");
    expect(await token.symbol()).to.equal("MYC");
    expect(await token.maxSupply()).to.equal(ethers.parseEther("1000000000"));
    expect(await token.baseRate()).to.equal(baseRate);
  });

  it("erlaubt owner-only batchMint", async function () {
    const { token, alice, bob } = await setup();
    await expect(
      token.batchMint([alice.address, bob.address], [ethers.parseEther("1"), ethers.parseEther("2")])
    )
      .to.emit(token, "BatchMint");

    expect(await token.balanceOf(alice.address)).to.equal(ethers.parseEther("1"));
    expect(await token.balanceOf(bob.address)).to.equal(ethers.parseEther("2"));
  });

  it("blockiert batchMint für non-owner", async function () {
    const { token, alice } = await setup();
    await expect(
      token.connect(alice).batchMint([alice.address], [ethers.parseEther("1")])
    ).to.be.revertedWithCustomError(token, "OwnableUnauthorizedAccount");
  });

  it("limitiert maxSupply", async function () {
    const { token, owner } = await setup();
    await expect(
      token.batchMint([owner.address], [ethers.parseEther("1000000001")])
    ).to.be.revertedWith("max supply exceeded");
  });

  it("kann baseRate setzen und halving ausführen", async function () {
    const { token } = await setup();
    await token.setBaseRate(ethers.parseEther("0.1"));
    expect(await token.baseRate()).to.equal(ethers.parseEther("0.1"));

    await token.halveBaseRate();
    expect(await token.baseRate()).to.equal(ethers.parseEther("0.05"));
  });

  it("burn reduziert Kontostand und totalSupply", async function () {
    const { token, owner } = await setup();
    await token.batchMint([owner.address], [ethers.parseEther("3")]);
    await token.burn(ethers.parseEther("1"));

    expect(await token.balanceOf(owner.address)).to.equal(ethers.parseEther("2"));
    expect(await token.totalSupply()).to.equal(ethers.parseEther("2"));
  });
});
