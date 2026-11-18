const { chromium } = require('playwright');
const D = 'build/frames';  // create this folder first: mkdir -p build/frames
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 800 }, deviceScaleFactor: 1 });
  await p.goto('https://infinaqnhat.github.io/Web-Infina-AI/property-expert-demo-tour.html', { waitUntil: 'networkidle', timeout: 60000 });
  await p.addStyleTag({ content: '.hob-tip,.hob-btn{display:none !important}' });
  await p.waitForTimeout(1500);
  let n = 0;
  const shot = async () => { await p.screenshot({ path: `${D}/f${String(n).padStart(3,'0')}.png` }); n++; };
  const burst = async (count, gap) => { for (let i=0;i<count;i++){ await shot(); await p.waitForTimeout(gap);} };
  await burst(3, 300);
  await p.locator('button.follow-chip', { hasText: 'Any HVAC issues?' }).first().click();
  await burst(14, 300);
  await p.waitForTimeout(1200);
  await burst(2, 300);
  await p.locator('button.follow-chip', { hasText: 'Can I schedule a tour?' }).first().click();
  await burst(16, 300);
  await p.waitForTimeout(1500);
  await burst(4, 400);
  console.log('frames', n);
  await b.close();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
