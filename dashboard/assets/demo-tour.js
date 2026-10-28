// Realisa, the guide for the agent dashboard demo.
// One tour that walks across several dashboard pages: Chats, one chat, Pipeline, Buyers, Insights.
// The step to show travels in the URL hash (#tour=N), so moving to the next page keeps the tour going.
// Pages load this file with <script src="<relative>/assets/demo-tour.js" defer></script>.
(function () {
  if (window.__realisaTour) return;
  window.__realisaTour = true;

  var script = document.currentScript || document.querySelector('script[src*="demo-tour.js"]');
  var ROOT = script.src.replace(/assets\/demo-tour\.js.*$/, '');   // .../dashboard/
  var here = location.href.split('#')[0].split('?')[0].replace(ROOT, '').replace(/\/$/, '/index.html');
  if (here === '' ) here = 'index.html';
  var SEEN_KEY = 'realisa-dash-tour-done';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var narrow = window.matchMedia('(max-width: 760px)');

  // ===== Helpers to find things in the static pages =====
  function q(sel) { return document.querySelector(sel); }
  function visible(el) {
    if (!el) return false;
    var r = el.getBoundingClientRect();
    return r.width > 4 && r.height > 4 && getComputedStyle(el).visibility !== 'hidden';
  }
  function byText(sel, text) {
    var all = document.querySelectorAll(sel);
    for (var i = 0; i < all.length; i++) if (all[i].textContent.indexOf(text) > -1 && visible(all[i])) return all[i];
    return null;
  }
  function firstVisible(sels) {
    for (var i = 0; i < sels.length; i++) { var el = q(sels[i]); if (visible(el)) return el; }
    return null;
  }

  // ===== The tour =====
  var STEPS = [
    { page: 'chats/index.html', target: function () { return firstVisible(['ul[aria-label="Chats"]']); },
      title: 'Every buyer chat, in one inbox',
      text: 'Chats from your listings, your own page and your clients land here. Your assistant answers them for you, day and night.' },
    { page: 'chats/index.html', target: function () { return byText('section[aria-label="Chats"] button', 'Needs you'); },
      title: 'Know who needs you',
      text: 'Most chats need nothing from you. When a buyer is ready, or the assistant has a question, the chat is marked <b>Needs you</b>.' },
    { page: 'chats/index.html', target: function () { var ul = q('ul[aria-label="Chats"]'); return ul && ul.querySelector('li'); },
      title: 'Open a chat',
      text: 'Megan and Chris Lee found a home from its yard sign. Let\'s see what they talked about.',
      nextLabel: 'Open the chat' },
    { page: 'chats/listing/p1/c1/index.html', target: function () { return firstVisible(['section[aria-label^="Chat with"] ol[aria-label="Chat"]', 'section[aria-label^="Chat with"]']); },
      title: 'The whole conversation',
      text: 'Everything the buyers sent, from voice notes to a pre-approval letter, and every answer the assistant gave, with its source.' },
    { page: 'chats/listing/p1/c1/index.html', target: function () { return firstVisible(['section[aria-label="The assistant asked you"]']); },
      title: 'It asks instead of guessing',
      text: 'The buyers asked for a credit for the old water heater. The assistant did not make up an answer: it asked you, once.' },
    { page: 'chats/listing/p1/c1/index.html', target: function () { var t = q('#agent-message'); return t && (t.closest('form') || t); },
      title: 'Jump in any time',
      text: 'Write to the buyers yourself whenever you want. The assistant steps back while you talk.' },
    { page: 'chats/listing/p1/c1/index.html', target: function () { return firstVisible(['aside[aria-label="Details"]']); },
      skipIf: function () { return !visible(q('aside[aria-label="Details"]')); },
      title: 'A quick read on the buyer',
      text: 'Budget, timeline, financing, worries and the next step, summarised from the chat so you can act fast.' },
    { page: 'index.html', target: function () { return firstVisible(['section[data-testid="pipeline-tiles"]']); },
      title: 'Your pipeline at a glance',
      text: 'Open deals, pipeline value and commission in play, always up to date.' },
    { page: 'index.html', target: function () {
        // desktop: the whole board; phone: the stage that is showing
        var s = q('section[data-stage-section]');
        if (s && visible(s.parentElement)) return s.parentElement;
        var shown = [].filter.call(document.querySelectorAll('main section'), function (el) {
          return visible(el) && el.querySelector('ul') && !el.matches('[aria-label="Summary"]');
        });
        return shown.length ? shown[0] : null;
      },
      title: 'Deals move on their own',
      text: 'One card per buyer and home. The assistant moves deals to <b>Engaged</b> and <b>Showing booked</b> from the chats. You move the rest.' },
    { page: 'buyers/index.html', target: function () { return firstVisible(['ul[aria-label="People who left contact"]']); },
      title: 'A next step for every buyer',
      text: 'Everyone who left a contact, with their stage and what to do next. Nobody slips through.' },
    { page: 'insights/index.html', target: function () {
        var h = q('section[data-testid="insights-headline"]');
        return h ? [h, h.nextElementSibling].filter(visible) : null;
      },
      title: 'What the AI did for you',
      text: 'How many people visited your homes, chatted with the AI, left a contact and asked to see the home.' },
    { page: 'insights/index.html', target: null,
      title: 'That\'s the agent side',
      text: 'Buyers get answers around the clock. You get warm leads with the full story. Tap me any time to take this tour again.',
      nextLabel: 'Done' }
  ];
  var TOTAL = STEPS.length;

  // ===== Styles =====
  var css = [
    '.rl-btn{position:fixed;right:22px;bottom:96px;z-index:2147483000;width:58px;height:58px;border:0;border-radius:50%;background:#fff;box-shadow:0 10px 28px -8px rgba(0,20,60,.5),0 0 0 1px rgba(0,20,60,.06);display:flex;align-items:center;justify-content:center;padding:0;cursor:pointer;transition:transform .2s}',
    '.rl-btn:hover{transform:translateY(-2px)}',
    '.rl-btn svg{width:42px;height:42px}',
    '.rl-btn.is-nudge::before{content:"";position:absolute;inset:-5px;border-radius:50%;border:2px solid #1863dc;animation:rl-ping 1.8s ease-out infinite}',
    '@keyframes rl-ping{0%{transform:scale(.92);opacity:1}100%{transform:scale(1.25);opacity:0}}',
    '.rl-tip{position:fixed;right:92px;bottom:110px;z-index:2147483000;padding:9px 14px;border:0;border-radius:12px;background:#001F5C;color:#fff;font:700 13px/1.3 "Be Vietnam Pro",-apple-system,system-ui,sans-serif;box-shadow:0 10px 24px -8px rgba(0,20,60,.5);cursor:pointer}',
    '.rl-tip::after{content:"";position:absolute;right:-6px;top:50%;width:12px;height:12px;background:#001F5C;transform:translateY(-50%) rotate(45deg);border-radius:2px}',
    '.rl-tip[hidden],.rl-spot[hidden],.rl-block[hidden],.rl-bubble[hidden]{display:none}',
    '.rl-spot{position:fixed;z-index:2147483001;border-radius:16px;box-shadow:0 0 0 100vmax rgba(8,18,46,.58);pointer-events:none}',
    '.rl-spot.is-anim{transition:left .32s cubic-bezier(.22,1,.36,1),top .32s cubic-bezier(.22,1,.36,1),width .32s cubic-bezier(.22,1,.36,1),height .32s cubic-bezier(.22,1,.36,1)}',
    '.rl-spot.has-ring::after{content:"";position:absolute;inset:-3px;border-radius:inherit;border:2px solid #fff;opacity:.9}',
    '.rl-block{position:fixed;inset:0;z-index:2147483002;background:transparent}',
    '.rl-bubble{position:fixed;z-index:2147483003;width:min(340px,calc(100vw - 24px));padding:16px 16px 14px;border-radius:18px;background:#fff;color:#1a1f2e;font-family:"Be Vietnam Pro",-apple-system,system-ui,sans-serif;box-shadow:0 24px 60px -14px rgba(0,20,60,.55),0 0 0 1px rgba(0,20,60,.06);opacity:0;transform:translateY(8px);transition:opacity .22s ease,transform .3s cubic-bezier(.22,1,.36,1);text-align:left}',
    '.rl-bubble.is-on{opacity:1;transform:none}',
    '.rl-bubble.is-docked{left:12px!important;right:12px;width:auto;top:auto!important;bottom:12px}',
    '.rl-head{display:flex;align-items:center;gap:9px;margin-bottom:10px}',
    '.rl-head svg{width:30px;height:30px;flex-shrink:0}',
    '.rl-head b{font-size:13.5px;font-weight:800;color:#001F5C}',
    '.rl-count{margin-left:auto;font-size:11.5px;font-weight:700;color:#64748b}',
    '.rl-x{flex-shrink:0;width:28px;height:28px;border:0;border-radius:50%;background:rgba(0,20,60,.06);color:#334155;display:flex;align-items:center;justify-content:center;cursor:pointer}',
    '.rl-x:hover{background:rgba(0,20,60,.12)}',
    '.rl-title{font-size:16px;font-weight:800;line-height:1.3;color:#001F5C}',
    '.rl-text{margin:6px 0 0;font-size:13.5px;line-height:1.55;color:#334155}',
    '.rl-text b{color:#1a1f2e}',
    '.rl-dots{display:flex;gap:5px;margin-top:12px}',
    '.rl-dots i{width:6px;height:6px;border-radius:50%;background:rgba(0,31,92,.16)}',
    '.rl-dots i.is-done{background:rgba(24,99,220,.5)}',
    '.rl-dots i.is-now{width:18px;border-radius:999px;background:#1863dc}',
    '.rl-actions{display:flex;align-items:center;gap:10px;margin-top:12px}',
    '.rl-skip{border:0;background:none;padding:6px 2px;font:700 12.5px/1 inherit;font-family:inherit;color:#64748b;text-decoration:underline;text-underline-offset:2px;cursor:pointer}',
    '.rl-skip:hover{color:#1a1f2e}',
    '.rl-spacer{flex:1}',
    '.rl-back{border:0;background:rgba(24,99,220,.08);color:#1863dc;padding:10px 14px;border-radius:999px;font:800 13.5px/1 inherit;font-family:inherit;cursor:pointer}',
    '.rl-back:hover{background:rgba(24,99,220,.16)}',
    '.rl-back[hidden]{display:none}',
    '.rl-next{border:0;background:#001F5C;color:#fff;padding:10px 18px;border-radius:999px;font:800 13.5px/1 inherit;font-family:inherit;cursor:pointer;white-space:nowrap}',
    '.rl-next:hover{background:#001340}',
    '.rl-arrow{position:absolute;width:12px;height:12px;background:#fff;border-radius:2px;transform:rotate(45deg)}',
    '.rl-bubble.is-docked .rl-arrow{display:none}',
    '@media (max-width:1023px){.rl-btn{bottom:88px;right:14px;width:48px;height:48px}.rl-btn svg{width:34px;height:34px}.rl-tip{bottom:96px;right:72px}}',
    '@media (prefers-reduced-motion:reduce){.rl-spot.is-anim,.rl-bubble{transition:none;transform:none}.rl-btn.is-nudge::before{animation:none}}'
  ].join('\n');
  var style = document.createElement('style'); style.textContent = css; document.head.appendChild(style);

  var REALISA_SVG = '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 4L44 20v22a4 4 0 01-4 4H8a4 4 0 01-4-4V20z" fill="#001F5C"/><circle cx="17" cy="29" r="4.6" fill="#fff"/><circle cx="31" cy="29" r="4.6" fill="#fff"/><circle cx="17.6" cy="29.4" r="2" fill="#001F5C"/><circle cx="31.6" cy="29.4" r="2" fill="#001F5C"/><path d="M19 38.5q5 3.6 10 0" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/><circle cx="38" cy="8" r="3.6" fill="#f5a623"/></svg>';

  function make(tag, cls) { var n = document.createElement(tag); if (cls) n.className = cls; return n; }

  // Launcher and tip
  var btn = make('button', 'rl-btn'); btn.type = 'button'; btn.setAttribute('aria-label', 'Take a tour with Realisa'); btn.innerHTML = REALISA_SVG;
  var tip = make('button', 'rl-tip'); tip.type = 'button'; tip.textContent = 'New here? Take a 1-minute tour'; tip.hidden = true;
  document.body.appendChild(tip); document.body.appendChild(btn);

  // Tour layers
  var spot = make('div', 'rl-spot'); spot.hidden = true;
  var block = make('div', 'rl-block'); block.hidden = true;
  var bubble = make('div', 'rl-bubble'); bubble.hidden = true;
  bubble.setAttribute('role', 'dialog'); bubble.setAttribute('aria-label', 'Tour with Realisa');
  bubble.innerHTML = '<div class="rl-head">' + REALISA_SVG + '<b>Realisa</b><span class="rl-count"></span><button type="button" class="rl-x" aria-label="Close the tour"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>' +
    '<div class="rl-title"></div><p class="rl-text" aria-live="polite"></p><div class="rl-dots"></div>' +
    '<div class="rl-actions"><button type="button" class="rl-skip">Skip tour</button><span class="rl-spacer"></span><button type="button" class="rl-back">Back</button><button type="button" class="rl-next">Next</button></div><span class="rl-arrow"></span>';
  document.body.appendChild(spot); document.body.appendChild(block); document.body.appendChild(bubble);
  var elCount = bubble.querySelector('.rl-count'), elTitle = bubble.querySelector('.rl-title'), elText = bubble.querySelector('.rl-text');
  var elDots = bubble.querySelector('.rl-dots'), elNext = bubble.querySelector('.rl-next'), elBack = bubble.querySelector('.rl-back'), elArrow = bubble.querySelector('.rl-arrow');

  var cur = -1, active = false;

  function stepUrl(i) { return ROOT + STEPS[i].page + '#tour=' + i; }
  function isHere(i) { return STEPS[i].page === here; }

  function rectOf(t) {
    var els = Array.isArray(t) ? t : [t];
    var r = null;
    els.forEach(function (el) {
      var b = el.getBoundingClientRect();
      if (!r) r = { left: b.left, top: b.top, right: b.right, bottom: b.bottom };
      else { r.left = Math.min(r.left, b.left); r.top = Math.min(r.top, b.top); r.right = Math.max(r.right, b.right); r.bottom = Math.max(r.bottom, b.bottom); }
    });
    if (!r) return null;
    // keep the spotlight inside the window
    var pad = 6;
    r.left = Math.max(4, r.left - pad); r.top = Math.max(4, r.top - pad);
    r.right = Math.min(innerWidth - 4, r.right + pad); r.bottom = Math.min(innerHeight - 4, r.bottom + pad);
    r.width = r.right - r.left; r.height = r.bottom - r.top;
    return r;
  }

  function resolveTarget(s) {
    var t = typeof s.target === 'function' ? s.target() : null;
    if (Array.isArray(t)) { t = t.filter(visible); return t.length ? t : null; }
    return visible(t) ? t : null;
  }

  function place() {
    if (!active) return;
    var s = STEPS[cur], t = resolveTarget(s);
    var r = t ? rectOf(t) : null;
    if (r && r.width > 0 && r.height > 0) {
      spot.hidden = false; spot.classList.add('has-ring');
      spot.style.left = r.left + 'px'; spot.style.top = r.top + 'px';
      spot.style.width = r.width + 'px'; spot.style.height = r.height + 'px';
    } else {
      // nothing to point at: dim the page and centre the bubble
      spot.hidden = false; spot.classList.remove('has-ring');
      spot.style.left = (innerWidth / 2) + 'px'; spot.style.top = (innerHeight / 2) + 'px';
      spot.style.width = '0px'; spot.style.height = '0px';
    }
    var bw = bubble.offsetWidth, bh = bubble.offsetHeight, gap = 16;
    bubble.classList.remove('is-docked');
    elArrow.style.cssText = '';
    if (narrow.matches) {
      bubble.classList.add('is-docked');
      // dock away from the target
      if (r && r.top + r.height / 2 > innerHeight / 2) { bubble.style.bottom = 'auto'; bubble.style.setProperty('top', '12px', 'important'); }
      else { bubble.style.top = ''; bubble.style.bottom = '12px'; }
      return;
    }
    bubble.style.bottom = '';
    var x, y, side;
    if (!r || !r.width) { x = (innerWidth - bw) / 2; y = (innerHeight - bh) / 2; side = null; }
    else if (innerWidth - r.right > bw + gap + 8) { side = 'right'; x = r.right + gap; y = r.top + Math.min(r.height, 220) / 2 - bh / 2; }
    else if (r.left > bw + gap + 8) { side = 'left'; x = r.left - gap - bw; y = r.top + Math.min(r.height, 220) / 2 - bh / 2; }
    else if (innerHeight - r.bottom > bh + gap + 8) { side = 'bottom'; y = r.bottom + gap; x = r.left + r.width / 2 - bw / 2; }
    else if (r.top > bh + gap + 8) { side = 'top'; y = r.top - gap - bh; x = r.left + r.width / 2 - bw / 2; }
    else { side = null; x = r.left + r.width / 2 - bw / 2; y = innerHeight - bh - 20; }
    x = Math.max(12, Math.min(innerWidth - bw - 12, x));
    y = Math.max(12, Math.min(innerHeight - bh - 12, y));
    bubble.style.left = x + 'px'; bubble.style.top = y + 'px';
    if (side === 'right' || side === 'left') {
      var ay = Math.max(16, Math.min(bh - 28, (r.top + Math.min(r.height, 220) / 2) - y - 6));
      elArrow.style.top = ay + 'px'; elArrow.style[side === 'right' ? 'left' : 'right'] = '-6px';
    } else if (side === 'bottom' || side === 'top') {
      var ax = Math.max(16, Math.min(bw - 28, (r.left + r.width / 2) - x - 6));
      elArrow.style.left = ax + 'px'; elArrow.style[side === 'bottom' ? 'top' : 'bottom'] = '-6px';
    } else elArrow.style.display = 'none';
  }

  function show(i) {
    // skip steps that make no sense on this screen size
    while (i < TOTAL && isHere(i) && STEPS[i].skipIf && STEPS[i].skipIf()) i++;
    if (i >= TOTAL) { end(true); return; }
    if (!isHere(i)) { go(i); return; }
    cur = i; active = true;
    var s = STEPS[i];
    try { history.replaceState(null, '', location.pathname + location.search + '#tour=' + i); } catch (e) {}
    tip.hidden = true; btn.classList.remove('is-nudge');
    var t = resolveTarget(s);
    var first = Array.isArray(t) ? t[0] : t;
    if (first) first.scrollIntoView({ block: 'center', inline: 'nearest', behavior: reduce ? 'auto' : 'smooth' });
    elCount.textContent = (i + 1) + ' of ' + TOTAL;
    elTitle.textContent = s.title;
    elText.innerHTML = s.text;
    elDots.innerHTML = '';
    for (var k = 0; k < TOTAL; k++) elDots.appendChild(make('i', k < i ? 'is-done' : (k === i ? 'is-now' : '')));
    elNext.textContent = s.nextLabel || 'Next';
    elBack.hidden = i === 0;
    bubble.querySelector('.rl-skip').hidden = i === TOTAL - 1;
    spot.classList.toggle('is-anim', !reduce && !spot.hidden);
    block.hidden = false; bubble.hidden = false;
    place();
    requestAnimationFrame(function () { bubble.classList.add('is-on'); });
    // the smooth scroll moves the target: follow it
    setTimeout(place, 120); setTimeout(place, 450);
    elNext.focus({ preventScroll: true });
  }

  function go(i) {
    // the next step is on another page
    active = false;
    location.href = stepUrl(i);
  }

  function end(done) {
    active = false;
    bubble.classList.remove('is-on');
    spot.hidden = true; block.hidden = true; bubble.hidden = true;
    try { localStorage.setItem(SEEN_KEY, '1'); } catch (e) {}
    try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
    btn.focus({ preventScroll: true });
  }

  elNext.addEventListener('click', function () { if (cur === TOTAL - 1) end(true); else show(cur + 1); });
  elBack.addEventListener('click', function () {
    var i = cur - 1;
    while (i > 0 && isHere(i) && STEPS[i].skipIf && STEPS[i].skipIf()) i--;
    if (i >= 0) show(i);
  });
  bubble.querySelector('.rl-skip').addEventListener('click', function () { end(false); });
  bubble.querySelector('.rl-x').addEventListener('click', function () { end(false); });
  document.addEventListener('keydown', function (e) {
    if (!active) return;
    if (e.key === 'Escape') end(false);
    else if (e.key === 'ArrowRight') elNext.click();
    else if (e.key === 'ArrowLeft' && !elBack.hidden) elBack.click();
  });
  window.addEventListener('resize', place);
  window.addEventListener('scroll', place, true);

  function start() {
    // start from the first step on this page, else from the beginning
    for (var i = 0; i < TOTAL; i++) if (isHere(i)) { show(i); return; }
    go(0);
  }
  btn.addEventListener('click', function () { if (!active) start(); });
  tip.addEventListener('click', function () { if (!active) start(); });

  // Arrived with #tour=N: carry on. Otherwise, nudge first-time visitors.
  var m = location.hash.match(/tour=(\d+)/);
  if (m && +m[1] < TOTAL) {
    setTimeout(function () { show(+m[1]); }, 450);
  } else {
    var seen = false; try { seen = localStorage.getItem(SEEN_KEY) === '1'; } catch (e) {}
    if (!seen) setTimeout(function () {
      if (active) return;
      btn.classList.add('is-nudge'); tip.hidden = false;
      setTimeout(function () { btn.classList.remove('is-nudge'); tip.hidden = true; }, 20000);
    }, 1500);
  }
})();
