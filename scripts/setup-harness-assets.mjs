// Mirrors committed static assets into the harness `public/` dir at the
// canonical absolute URLs the landing components reference:
//   uploads/<file>            -> /landing-html/uploads/<file>   (matches PFA public/landing-html/)
//   realsalex-mockups/<file>  -> /realsalex-mockups/<file>      (sample Deal Room / dashboard)
//
// Keeps `public/` out of git (it is a regenerable mirror) while guaranteeing
// `npm run dev|build` resolve every asset on a fresh clone.
// No third-party deps — runs on any Node >= 16.7 (fs.cpSync).
import { cpSync, existsSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");

/** [source dir relative to repo root, destination dir relative to public/] */
const MIRRORS = [
  ["uploads", "landing-html/uploads"],
  ["realsalex-mockups", "realsalex-mockups"],
];

for (const [from, to] of MIRRORS) {
  const src = resolve(root, from);
  if (!existsSync(src)) {
    console.error(`[harness-assets] source not found: ${src}`);
    process.exit(1);
  }
  const dest = resolve(root, "public", to);
  mkdirSync(dest, { recursive: true });
  cpSync(src, dest, { recursive: true });
  console.log(`[harness-assets] mirrored ${from} -> ${dest}`);
}
