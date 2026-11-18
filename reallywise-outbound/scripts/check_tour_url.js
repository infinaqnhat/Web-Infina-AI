const { chromium } = require('playwright');
const B='https://infinaqnhat.github.io/Web-Infina-AI/property-expert-demo-tour.html';
(async () => {
  const b = await chromium.launch();
  for (const suffix of ['', '#tour=1', '?agent=dashboard#tour=1']) {
    const ctx = await b.newContext({ viewport: { width: 1280, height: 800 } });
    const p = await ctx.newPage();
    await p.goto(B+suffix, { waitUntil: 'networkidle', timeout: 60000 }).catch(e=>console.log('goto',e.message));
    await p.waitForTimeout(3000);
    const state = await p.evaluate(() => {
      const t=[...document.querySelectorAll('[class*=tour],[class*=hob],[role=dialog]')].filter(e=>e.offsetParent!==null||getComputedStyle(e).position==='fixed').map(e=>(e.className||'').toString().slice(0,40)+'|'+(e.innerText||'').trim().replace(/\s+/g,' ').slice(0,90));
      return t.slice(0,6);
    });
    console.log('\n== suffix:', JSON.stringify(suffix)); console.log(state.join('\n'));
    if (suffix==='?agent=dashboard#tour=1') await p.screenshot({ path: 'build/tour_hash.png' });
    await ctx.close();
  }
  await b.close();
})();
