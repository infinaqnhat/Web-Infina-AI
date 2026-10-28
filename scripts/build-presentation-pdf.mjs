// Builds uploads/AI-Property-Product-Presentation.pdf from product-presentation.html.
// Each page is a sharp picture of one slide as it prints (16:9, interactive slides replaced
// by the "See it live" page), with its links laid back on top so they stay clickable.
// Pictures look the same in every PDF viewer, whatever fonts or effects it supports.
// Needs Playwright with Chromium on this machine: npm run pdf
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

// CommonJS resolution, so a globally installed Playwright (NODE_PATH) is found too
const { chromium } = createRequire(import.meta.url)('playwright');

const root = fileURLToPath(new URL('..', import.meta.url));
const types = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.jpg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml', '.webp': 'image/webp', '.woff2': 'font/woff2' };
const W = 1280, H = 720;

const server = createServer(async (req, res) => {
  const path = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)).replace(/^([/\\])+/, '');
  try {
    const body = await readFile(join(root, path || 'index.html'));
    res.writeHead(200, { 'content-type': types[extname(path)] || 'application/octet-stream' });
    res.end(body);
  } catch {
    res.writeHead(404); res.end();
  }
}).listen(0);
const port = server.address().port;

const browser = await chromium.launch();

// 1. Picture every printed slide at twice the size, and note where its links are
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
await page.goto(`http://localhost:${port}/product-presentation.html`, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.evaluate(() => window.__preparePrint());
await page.emulateMedia({ media: 'print' });
await page.waitForTimeout(800);
const cards = page.locator('.slide:not(.no-print) > .card');
const count = await cards.count();
const pages = [];
for (let i = 0; i < count; i++) {
  const card = cards.nth(i);
  await card.scrollIntoViewIfNeeded();
  const shot = await card.screenshot({ type: 'jpeg', quality: 88 });
  const links = await card.evaluate((el) => {
    const box = el.getBoundingClientRect();
    return [...el.querySelectorAll('a[href^="http"]')].map((a) => {
      const r = a.getBoundingClientRect();
      return { href: a.href, x: (r.left - box.left) / box.width, y: (r.top - box.top) / box.height, w: r.width / box.width, h: r.height / box.height };
    });
  });
  pages.push({ img: shot.toString('base64'), links });
}

// 2. One PDF page per picture, with the links on top
const esc = (s) => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
const html = `<!doctype html><html><head><meta charset="utf-8"><title>AI Property · Product Presentation · Infina AI</title><style>
@page { size:${W}px ${H}px; margin:0; }
html, body { margin:0; padding:0; }
.p { position:relative; width:${W}px; height:${H}px; break-after:page; overflow:hidden; }
.p:last-child { break-after:auto; }
.p img { display:block; width:${W}px; height:${H}px; }
.p a { position:absolute; display:block; }
</style></head><body>${pages.map((p) => `<div class="p"><img src="data:image/jpeg;base64,${p.img}">${p.links.map((l) =>
  `<a href="${esc(l.href)}" style="left:${(l.x * 100).toFixed(3)}%;top:${(l.y * 100).toFixed(3)}%;width:${(l.w * 100).toFixed(3)}%;height:${(l.h * 100).toFixed(3)}%"></a>`).join('')}</div>`).join('')}</body></html>`;
const doc = await browser.newPage({ viewport: { width: W, height: H } });
await doc.setContent(html, { waitUntil: 'load' });
const out = join(root, 'uploads', 'AI-Property-Product-Presentation.pdf');
await doc.pdf({ path: out, width: `${W}px`, height: `${H}px`, printBackground: true, preferCSSPageSize: true });

await browser.close();
server.close();
console.log(`Wrote ${out} (${count} pages)`);
