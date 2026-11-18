const { chromium } = require('playwright');
const B='https://infinaqnhat.github.io/Web-Infina-AI/property-expert-demo-tour.html';
(async () => {
  const b = await chromium.launch();
  for (const suffix of ['?agent=dashboard#tour=1','#tour=1']) {
    const ctx = await b.newContext({ viewport: { width: 1280, height: 800 } });
    const p = await ctx.newPage();
    p.on('framenavigated', f => { if (f===p.mainFrame()) console.log('  NAV ->', f.url()); });
    await p.goto(B+suffix, { waitUntil: 'networkidle', timeout: 60000 });
    await p.waitForTimeout(2000);
    console.log('\n== '+suffix);
    for (let i=0;i<12;i++) {
      const hasEnd = await p.locator('.tour-bubble.is-on button', { hasText: /Ask one for me/i }).count();
      if (hasEnd) { await p.locator('.tour-bubble.is-on button', { hasText: /Ask one for me/i }).click(); break; }
      const next = p.locator('.tour-bubble.is-on button', { hasText: /^(Next|Skip this step)/i }).last();
      if (!(await next.count())) break;
      await next.click().catch(()=>{}); await p.waitForTimeout(1500);
    }
    await p.waitForTimeout(6000);
    console.log('  URL after final step:', p.url());
    const txt = await p.evaluate(() => { const e=document.querySelector('.tour-bubble.is-on'); return e? e.innerText.trim().replace(/\s+/g,' ').slice(0,200):'(no bubble) title='+document.title; });
    console.log('  Now showing:', txt);
    if (suffix.startsWith('?agent')) await p.screenshot({ path: 'build/tour_after.png' });
    await ctx.close();
  }
  await b.close();
})().catch(e=>console.error('ERR',e.message));
