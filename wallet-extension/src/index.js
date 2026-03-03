import React from "react";
import { createRoot } from "react-dom/client";
import { WalletApp } from "./wallet";
import "./wallet.css";

createRoot(document.getElementById("root")).render(<WalletApp />);
