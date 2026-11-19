// Renders thumbnail.html to the poster images used by the promo video (node render-thumbnail.cjs)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + path.join(__dirname, 'thumbnail.html')); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
  await p.screenshot({ path: path.join(__dirname, '../../uploads/property-expert-promo-thumbnail.png') });
  await b.close();
})();
