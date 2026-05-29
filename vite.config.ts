import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

// Standalone verification harness for the landing React port.
// Mirrors PFA's `@ -> ./src` alias so component imports resolve identically
// in both repos (Web = authoring source, PFA = production runtime).
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
});
