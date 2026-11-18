// Shared player for the ReallyWise explainer videos (used by product-tour/; lead-capture-video.html has its own copy).
//
// A page lays out a 1920x1080 #stage and describes its timeline in "design seconds" with data attributes:
//   data-in / data-out     show and hide times, data-d / data-od the fade lengths
//   data-fx                fade | up | down | left | right | zoom | pop | ripple
//   data-type="s,e"        types data-text between s and e
//   data-count="s,d,n"     counts up to n, data-bar="s,d,w" grows a bar to w (0..1)
//   data-target="#id"      on a ripple: centered on that element when it appears
// window.VIDEO = { duration, cursor: [[time, '#selector'], ...], press: [[from, to], ...], hideSubsAfter }
// subtitles.js (from voiceover.py) adds SUBTITLES, TIMEWARP (design -> real anchors) and VO_DURATION.
(function () {
  const V = window.VIDEO || {};
  const DESIGN = V.duration || 60;
  const DURATION = window.VO_DURATION || DESIGN;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const easeOut = p => 1 - Math.pow(1 - p, 3);
  const easeInOut = p => p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2;
  const back = p => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(p - 1, 3) + c1 * Math.pow(p - 1, 2); };

  function toDesign(t) {   // real time -> design time
    const w = window.TIMEWARP;
    if (!w || w.length < 2) return t;
    for (let i = 1; i < w.length; i++) {
      const [d0, r0] = w[i - 1], [d1, r1] = w[i];
      if (t <= r1) return r1 === r0 ? d1 : d0 + (d1 - d0) * (t - r0) / (r1 - r0);
    }
    return t - w[w.length - 1][1] + w[w.length - 1][0];
  }

  // QR code for https://reallywise.ai/l/123-main
  const QR_D = window.QR_PATH || '';
  if (QR_D) document.querySelectorAll('.qr').forEach(q => q.innerHTML = '<svg viewBox="-2 -2 37 37" shape-rendering="crispEdges"><path stroke="currentColor" d="' + QR_D + '"/></svg>');

  const anim = [...document.querySelectorAll('[data-in]')].map(el => ({
    el, a: +el.dataset.in, b: el.dataset.out ? +el.dataset.out : 1e9,
    d: el.dataset.d ? +el.dataset.d : 0.5, od: el.dataset.od ? +el.dataset.od : 0.45, fx: el.dataset.fx || 'fade'
  }));
  const types = [...document.querySelectorAll('[data-type]')].map(el => { const [s, e] = el.dataset.type.split(',').map(Number); return { el, s, e, text: el.dataset.text }; });
  const counts = [...document.querySelectorAll('[data-count]')].map(el => { const [s, d, n] = el.dataset.count.split(',').map(Number); return { el, s, d, n, dec: (el.dataset.count.split(',')[2].split('.')[1] || '').length, suf: el.dataset.suffix || '' }; });
  const bars = [...document.querySelectorAll('[data-bar]')].map(el => { const [s, d, w] = el.dataset.bar.split(',').map(Number); return { el, s, d, w }; });

  function applyAnim(o, t) {
    const { el, a, b, d, od, fx } = o;
    const vis = t >= a && t < b + od;
    el.style.display = vis ? '' : 'none';
    if (!vis) return;
    const raw = clamp((t - a) / d), pin = easeOut(raw), pout = easeInOut(clamp((t - b) / od));
    let op = pin * (1 - pout), tr = 'none', sc = 'none';
    if (fx === 'up') tr = `0 ${(1 - pin) * 36}px`;
    else if (fx === 'down') tr = `0 ${-(1 - pin) * 36}px`;
    else if (fx === 'left') tr = `${-(1 - pin) * 50}px 0`;
    else if (fx === 'right') tr = `${(1 - pin) * 60}px 0`;
    else if (fx === 'zoom') sc = `${0.94 + 0.06 * pin}`;
    else if (fx === 'pop') sc = `${0.4 + 0.6 * back(raw)}`;
    else if (fx === 'ripple') { sc = `${0.3 + raw * 1.2}`; op = (1 - raw) * (1 - pout); }
    el.style.opacity = op; el.style.translate = tr; el.style.scale = sc;
  }

  let CUR = [];
  function cursorAt(t) {
    const c = document.getElementById('cursor');
    if (!c || CUR.length < 2 || t < CUR[0][0] || t > CUR[CUR.length - 1][0]) { if (c) c.style.display = 'none'; return; }
    let i = 0; while (i < CUR.length - 2 && t > CUR[i + 1][0]) i++;
    const [t0, x0, y0] = CUR[i], [t1, x1, y1] = CUR[i + 1];
    if (x0 == null || x1 == null) { c.style.display = 'none'; return; }
    c.style.display = '';
    const p = easeInOut(clamp((t - t0) / Math.max(0.001, t1 - t0)));
    c.style.left = (x0 + (x1 - x0) * p - 8) + 'px'; c.style.top = (y0 + (y1 - y0) * p - 4) + 'px';
    c.style.scale = (V.press || []).some(([a, b]) => t > a && t < b) ? '0.85' : '1';
    c.style.opacity = Math.min(1, (t - CUR[0][0]) / 0.3, (CUR[CUR.length - 1][0] - t) / 0.3);
  }

  const SHOW_SUBS = !new URLSearchParams(location.search).has('nosubs');
  function subsAt(tReal, tDesign) {
    const box = document.getElementById('subs'); if (!box) return;
    const span = box.firstElementChild;
    const cue = SHOW_SUBS && tDesign < (V.hideSubsAfter || 1e9) && (window.SUBTITLES || []).find(c => tReal >= c[0] && tReal < c[1]);
    if (!cue) { box.style.display = 'none'; return; }
    box.style.display = '';
    if (span.textContent !== cue[2]) span.textContent = cue[2];
    box.style.opacity = Math.min(1, (tReal - cue[0]) / 0.15, (cue[1] - tReal) / 0.15);
  }

  function seekDesign(t) {
    for (const o of anim) applyAnim(o, t);
    for (const o of types) {
      const n = Math.round(o.text.length * clamp((t - o.s) / (o.e - o.s)));
      o.el.textContent = o.text.slice(0, n);
      o.el.classList.toggle('typing', t >= o.s && t < o.e + 0.4);
    }
    for (const o of counts) {
      const v = o.n * easeOut(clamp((t - o.s) / o.d));
      o.el.textContent = (o.dec ? v.toFixed(o.dec) : Math.round(v).toLocaleString('en-US')) + o.suf;
    }
    for (const o of bars) o.el.style.width = (o.w * 100 * easeOut(clamp((t - o.s) / o.d))) + '%';
    document.querySelectorAll('.dots').forEach(d => [...d.children].forEach((i, k) => { i.style.translate = `0 ${-Math.max(0, Math.sin(t * 7 - k * 0.9)) * 5}px`; }));
    cursorAt(t);
    if (V.onSeek) V.onSeek(t);
  }
  window.seek = tr => { const td = toDesign(tr); seekDesign(td); subsAt(tr, td); };
  window.DURATION = DURATION;

  function centerOf(el, ref) { const r = el.getBoundingClientRect(), q = ref.getBoundingClientRect(); return [r.left - q.left + r.width / 2, r.top - q.top + r.height / 2]; }
  function measure() {
    const stage = document.getElementById('stage');
    document.querySelectorAll('[data-target]').forEach(rp => {
      seekDesign(+rp.dataset.in + 0.01);
      const tg = document.querySelector(rp.dataset.target), ref = rp.offsetParent || stage;
      if (!tg) return console.error('no target', rp.dataset.target);
      const [x, y] = centerOf(tg, ref); rp.style.left = x + 'px'; rp.style.top = y + 'px';
    });
    CUR = (V.cursor || []).map(([t, sel]) => {
      if (!sel) return [t, null, null];
      seekDesign(t); const el = document.querySelector(sel);
      if (!el) { console.error('no cursor target', sel); return [t, null, null]; }
      return [t, ...centerOf(el, stage)];
    });
  }

  const params = new URLSearchParams(location.search);
  const RENDER = params.has('render');
  function fit() {
    const s = Math.min(innerWidth / 1920, innerHeight / 1080), st = document.getElementById('stage');
    st.style.transform = `scale(${s})`; st.style.left = (innerWidth - 1920 * s) / 2 + 'px'; st.style.top = (innerHeight - 1080 * s) / 2 + 'px';
  }
  document.fonts.ready.then(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))).then(() => {
    measure();
    if (RENDER) { window.seek(+(params.get('t') || 0)); window.READY = true; return; }
    fit(); addEventListener('resize', fit);
    const vo = document.getElementById('vo'), hud = document.getElementById('hud');
    let start = performance.now() - (+(params.get('t') || 0)) * 1000;
    addEventListener('click', () => { start = performance.now(); if (vo) { vo.currentTime = 0; vo.play().catch(() => {}); } });
    const loop = now => {
      const t = (now - start) / 1000;
      if (t >= DURATION) { start = now; if (vo) vo.pause(); }
      window.seek(Math.min(t, DURATION - 0.001));
      if (hud) hud.textContent = t.toFixed(2) + 's';
      requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);
  });
})();
