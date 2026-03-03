// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MycToken is ERC20, Ownable {
    uint256 public immutable maxSupply;
    uint256 public baseRate;

    event BaseRateUpdated(uint256 newBaseRate);
    event BaseRateHalved(uint256 newBaseRate);
    event BatchMint(address indexed caller, uint256 recipients, uint256 totalMinted);

    constructor(uint256 _initialBaseRate) ERC20("Mycelial Credit", "MYC") Ownable(msg.sender) {
        maxSupply = 1_000_000_000 ether;
        baseRate = _initialBaseRate;
    }

    function setBaseRate(uint256 _newBaseRate) external onlyOwner {
        baseRate = _newBaseRate;
        emit BaseRateUpdated(_newBaseRate);
    }

    function halveBaseRate() external onlyOwner {
        require(baseRate > 0, "baseRate already zero");
        baseRate = baseRate / 2;
        emit BaseRateHalved(baseRate);
    }

    function batchMint(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "length mismatch");
        require(recipients.length > 0, "empty batch");

        uint256 totalMint;
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "zero recipient");
            totalMint += amounts[i];
        }

        require(totalSupply() + totalMint <= maxSupply, "max supply exceeded");

        for (uint256 i = 0; i < recipients.length; i++) {
            _mint(recipients[i], amounts[i]);
        }

        emit BatchMint(msg.sender, recipients.length, totalMint);
    }

    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
