// Renders lead-capture-thumbnail.html to ../uploads/property-expert-lead-capture-thumbnail.jpg (node render-lead-thumbnail.cjs, needs ffmpeg)
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + path.join(__dirname, 'lead-capture-thumbnail.html')); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
  const png = path.join(__dirname, 'lead-thumb.png');
  await p.screenshot({ path: png }); await b.close();
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-i', png, '-q:v', '2', path.join(__dirname, '../uploads/property-expert-lead-capture-thumbnail.jpg')]);
  require('fs').unlinkSync(png);
})();
