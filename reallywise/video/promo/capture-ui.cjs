// Captures the real ReallyWise UI (buyer demo, admin demo, dashboard export, landing page) as stills
// for the promo video. Run from this folder: node capture-ui.cjs   (Playwright with Chromium needed)
const { chromium } = require('playwright');
const path = require('path');
const R = path.resolve(__dirname, '../..') + '/';
const OUT = path.join(__dirname, 'shots');
const wait = ms => new Promise(r => setTimeout(r, ms));

async function open(b, file, vp = { width: 1440, height: 900 }, dpr = 2) {
  const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: dpr });
  const pg = await ctx.newPage();
  await pg.route('**/demo-tour.js', r => r.abort());          // the dashboard's "Take a 6-step tour" overlay
  await pg.goto('file://' + R + file); await wait(1200);
  return pg;
}
const REG = {};
// shot(): saves the PNG and the boxes (CSS px, 1440x900 page) of the texts we zoom to or highlight
async function shot(pg, name, texts = []) {
  await pg.screenshot({ path: path.join(OUT, name + '.png') }); console.log(name);
  REG[name] = {};
  for (const t of texts) {
    const loc = typeof t === 'string' ? pg.getByText(t, { exact: false }).first() : pg.locator(t.css).first();
    const key = typeof t === 'string' ? t : t.key;
    try { const bb = await loc.boundingBox({ timeout: 1500 }); if (bb) REG[name][key] = [bb.x, bb.y, bb.width, bb.height].map(Math.round); } catch (e) { console.log('  no box for', key); }
  }
}
async function skipTour(pg) {
  const s = pg.locator('.tour-skip').first(); if (await s.count() && await s.isVisible()) { await s.click(); await wait(500); }
  // hide the floating "take a tour" launcher in the bottom corner (a demo-only helper, not part of the product)
  await pg.addStyleTag({ content: '.tour-bubble{display:none!important}' });
  await pg.evaluate(() => document.querySelectorAll('body *').forEach(el => {
    const cs = getComputedStyle(el); if (cs.position !== 'fixed') return;
    const r = el.getBoundingClientRect();
    if (r.top > innerHeight * 0.6 && r.left > innerWidth * 0.55 && r.width < 420) el.style.display = 'none';
  }));
}
async function ask(pg, q, ms = 2600) { await pg.locator(`.follow-chip[data-q="${q}"]:visible`).first().click(); await wait(ms); }

(async () => {
  const b = await chromium.launch();
  // buyer demo, desktop
  let pg = await open(b, 'property-expert-demo-tour.html');
  await skipTour(pg); await shot(pg, 'buyer-start');
  await ask(pg, 'Are there any known issues with this property?'); await shot(pg, 'buyer-issues', [{ key: 'answer', css: '.msg-bot >> nth=-1' }, 'Online, replies instantly', 'Key insights']);
  await ask(pg, "What's the HOA like?"); await shot(pg, 'buyer-hoa');
  await ask(pg, 'Can I schedule a tour?'); await shot(pg, 'buyer-tour');
  const slot = pg.locator('.slot-btn:visible').nth(1);
  if (await slot.count()) { await slot.click(); await wait(2600); await shot(pg, 'buyer-booked', ['Request a private showing', 'works for me', "I've sent your request"]); }
  await wait(6500); await shot(pg, 'buyer-lead-toast', ['New lead: ready to tour', 'Click to view']);
  await pg.close();
  // buyer demo, phone
  pg = await open(b, 'property-expert-demo-tour.html', { width: 390, height: 844 }, 3);
  await skipTour(pg); await shot(pg, 'phone-start');
  await ask(pg, 'Are there any known issues with this property?').catch(() => console.log('no phone chip'));
  await shot(pg, 'phone-issues');
  await pg.close();
  // admin demo
  pg = await open(b, 'property-expert-admin-demo-tour.html');
  await skipTour(pg); await shot(pg, 'admin-chat', ['How close they are', 'What they told us', 'Needs you', 'Ready to tour: I', 'Next step']);
  await pg.close();
  // landing page: create a Property Expert from a listing link
  pg = await open(b, 'reallywise.html#listing-agent');
  const box = pg.locator('#qr-create-btn');
  await box.scrollIntoViewIfNeeded(); await pg.evaluate(() => scrollBy(0, -160)); await wait(600);
  await pg.fill('#url-qr', 'https://www.zillow.com/homedetails/123-Main-St-Austin-TX-78703/'); await shot(pg, 'landing-paste', [{ key: 'form', css: '#url-qr' }, { key: 'btn', css: '#qr-create-btn' }]);
  await box.click(); await wait(900); await shot(pg, 'landing-creating');
  await wait(3500); await shot(pg, 'landing-live', ['Your Property Expert is live.', 'Download QR code', 'Paste link to your listing']);
  await pg.close();
  // dashboard
  for (const [file, name] of [
    ['dashboard/home/index.html', 'dash-home'], ['dashboard/index.html', 'dash-pipeline'],
    ['dashboard/chats/listing/p1/c1/index.html', 'dash-chat'], ['dashboard/insights/index.html', 'dash-insights'],
    ['dashboard/properties/kit_elm/index.html', 'dash-listing'], ['dashboard/properties/kit_elm/knowledge/index.html', 'dash-knowledge'],
    ['dashboard/properties/kit_elm/kit/index.html', 'dash-printkit'], ['dashboard/properties/kit_elm/report/seller/index.html', 'dash-seller-report'],
    ['dashboard/properties/kit_elm/showings/index.html', 'dash-showings'], ['dashboard/properties/kit_elm/review/index.html', 'dash-review'],
    ['dashboard/assistant/index.html', 'dash-realisa'],
  ]) {
    const texts = { 'dash-insights': ['Chatted with the AI', 'Asked to see the home', 'Visitors came to your'], 'dash-seller-report': ['people viewed the listing page', 'asked the AI assistant questions', 'Counts only.'],
      'dash-knowledge': ['What the assistant knows', 'TDS, p. 3', 'Waiting on the seller', 'Approve'], 'dash-chat': ['Thanks, Jordan', 'Needs you'], 'dash-home': ['Assistant on for'] }[name] || [];
    pg = await open(b, file);
    // the export predates the rename of the agent's assistant: show it under its current name, Realisa
    await pg.evaluate(() => { const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n;
      while ((n = w.nextNode())) if (/\bHob\b/.test(n.nodeValue)) n.nodeValue = n.nodeValue.replace(/\bHob\b/g, 'Realisa');
      document.querySelectorAll('[placeholder]').forEach(i => i.placeholder = i.placeholder.replace(/\bHob\b/g, 'Realisa')); });
    await shot(pg, name, texts); await pg.close();
  }
  require('fs').writeFileSync(path.join(OUT, 'regions.js'), '// Boxes (CSS px on a 1440x900 page) of UI elements in each capture, written by capture-ui.cjs\nwindow.REGIONS = ' + JSON.stringify(REG) + ';\n');
  // the PNGs are converted to JPG afterwards: for f in shots/*.png; do ffmpeg -i "$f" -q:v 3 "${f%.png}.jpg"; done
  await b.close();
})();
