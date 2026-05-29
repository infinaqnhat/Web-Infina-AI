// Mirrors the committed `uploads/` assets into the harness `public/` dir at the
// canonical absolute URL the landing components reference:
//   /landing-html/uploads/<file>   (matches PFA public/landing-html/)
//
// Keeps `public/` out of git (it is a regenerable mirror of `uploads/`) while
// guaranteeing `npm run dev|build` resolve every image on a fresh clone.
// No third-party deps — runs on any Node >= 16.7 (fs.cpSync).
import { cpSync, existsSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const src = resolve(root, "uploads");

if (!existsSync(src)) {
  console.error(`[harness-assets] source not found: ${src}`);
  process.exit(1);
}

const dest = resolve(root, "public/landing-html/uploads");
mkdirSync(dest, { recursive: true });
cpSync(src, dest, { recursive: true });
console.log(`[harness-assets] mirrored uploads -> ${dest}`);
