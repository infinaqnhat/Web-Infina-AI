import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { HelmetProvider } from "react-helmet-async";
import { BrowserRouter } from "react-router-dom";
import App from "./App";

// Harness entry. Provides the same runtime context PFA gives the landing
// pages — HelmetProvider (page <title>/meta) + BrowserRouter (Link/Outlet) —
// without pulling in any PFA app providers. Keeps the port verifiable in
// isolation before it syncs downstream.
createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <HelmetProvider>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </HelmetProvider>
  </StrictMode>,
);
