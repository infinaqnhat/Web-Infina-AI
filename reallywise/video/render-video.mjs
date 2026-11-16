// Renders lead-capture-video.html to MP4, frame by frame (deterministic, no dropped frames).
// Usage:
//   node render-video.mjs                    -> ../uploads/property-expert-lead-capture.mp4 (1920x1080, 30 fps)
//   node render-video.mjs --stills 3,10,20   -> PNG stills in ./stills for review
// Needs Playwright with Chromium and ffmpeg on PATH.
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import { spawn } from 'node:child_process';
import { mkdirSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const FPS = +opt('--fps', 30);
const OUT = path.resolve(here, opt('--out', '../uploads/property-expert-lead-capture.mp4'));
const stills = opt('--stills', null);

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(path.join(here, 'lead-capture-video.html')).href + '?render');
await page.waitForFunction(() => window.READY === true, null, { timeout: 60000 });

if (stills) {
  mkdirSync(path.join(here, 'stills'), { recursive: true });
  for (const t of stills.split(',').map(Number)) {
    await page.evaluate(t => window.seek(t), t);
    await page.screenshot({ path: path.join(here, 'stills', `t${String(t).padStart(5, '0')}.png`) });
  }
  await browser.close();
  process.exit(0);
}

const duration = await page.evaluate(() => window.DURATION);
const total = Math.round(duration * FPS);
const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '20', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', OUT], { stdio: ['pipe', 'inherit', 'inherit'] });
for (let f = 0; f < total; f++) {
  await page.evaluate(t => window.seek(t), f / FPS);
  const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (f % (FPS * 5) === 0) process.stdout.write(`frame ${f}/${total}\n`);
}
ff.stdin.end();
await new Promise(r => ff.on('close', r));
await browser.close();
console.log('wrote', OUT);
