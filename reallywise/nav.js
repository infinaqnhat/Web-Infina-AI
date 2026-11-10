(function () {
  if (customElements.get('rw-nav')) return;

  // ReallyWise site navigation. Attributes:
  //   cta-text, cta-href   primary button (navy)
  //   links                JSON array of { text, href, slide } shown in the centre and in the mobile panel
  //   logo-href            where the logo points (default "./")
  //   transparent-until-scroll, transparent-until="#selector"
  //                        sit transparent over a photo hero until the page scrolls past that element, then become a white bar
  var CSS = [
    'rw-nav { display: contents; }',
    'nav.rw-nav { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(255,255,255,.9); -webkit-backdrop-filter: blur(20px); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border-light, #E7EBF4); transition: background .3s, border-color .3s; }',
    'nav.rw-nav.is-transparent { background: transparent; -webkit-backdrop-filter: none; backdrop-filter: none; border-bottom-color: transparent; }',
    '.rw-nav .nav-inner { display: flex; align-items: center; justify-content: space-between; gap: 24px; height: 72px; max-width: 1200px; margin: 0 auto; padding: 0 32px; }',
    '.rw-nav .logo { display: flex; align-items: center; flex-shrink: 0; }',
    '.rw-nav .logo-img { height: 44px; width: auto; display: block; }',
    '.rw-nav .nav-center { display: flex; align-items: center; gap: 8px; }',
    '.rw-nav .nav-center a { font-family: var(--font-body, "DM Sans", system-ui, sans-serif); font-size: 14px; font-weight: 600; color: var(--fg-secondary, #4E5878); padding: 9px 16px; border-radius: 10px; border: 1px solid var(--border, #DCE1EC); background: var(--surface, #F5F7FB); text-decoration: none; transition: background .2s, color .2s, border-color .2s; }',
    '.rw-nav .nav-center a:hover { border-color: var(--accent, #071843); color: var(--accent, #071843); }',
    '.rw-nav .nav-center a.is-active { color: #fff; background: var(--accent, #071843); border-color: var(--accent, #071843); }',
    '.rw-nav.is-transparent .nav-center a { color: #fff; background: rgba(255,255,255,.14); border-color: rgba(255,255,255,.4); -webkit-backdrop-filter: blur(6px); backdrop-filter: blur(6px); }',
    '.rw-nav.is-transparent .nav-center a:hover { background: rgba(255,255,255,.26); color: #fff; border-color: rgba(255,255,255,.4); }',
    '.rw-nav.is-transparent .nav-center a.is-active { color: var(--accent, #071843); background: #fff; border-color: #fff; }',
    '.rw-nav.is-transparent .nav-toggle { color: #fff; }',
    '.rw-nav .nav-cta { font-family: var(--font-body, "DM Sans", system-ui, sans-serif); background: var(--accent, #071843); color: #fff !important; padding: 12px 20px; border-radius: 10px; font-size: 14px; font-weight: 600; text-decoration: none; white-space: nowrap; transition: background .2s; }',
    '.rw-nav .nav-cta:hover { background: var(--accent-dark, #050F2B); }',
    '.rw-nav .nav-toggle { display: none; background: none; border: none; cursor: pointer; padding: 8px; color: var(--accent, #071843); }',
    '.rw-nav .nav-toggle svg { width: 24px; height: 24px; display: block; }',
    '.rw-nav .nav-mobile-panel { display: none; }',
    '@media (max-width: 768px) {',
    '  .rw-nav .nav-center, .rw-nav .nav-cta { display: none; }',
    '  .rw-nav .logo-img { height: 44px; }',
    '  .rw-nav .nav-toggle { display: block; }',
    '  .rw-nav .nav-mobile-panel { display: flex; flex-direction: column; position: fixed; top: 72px; left: 0; right: 0; background: #fff; padding: 8px 24px 20px; border-bottom: 1px solid var(--border, #DCE1EC); box-shadow: 0 6px 20px rgba(7,24,67,.08); transform: translateY(-8px); opacity: 0; visibility: hidden; transition: transform .25s, opacity .25s, visibility .25s; }',
    '  body.nav-open .rw-nav .nav-mobile-panel { transform: translateY(0); opacity: 1; visibility: visible; }',
    '  .rw-nav .nav-mobile-panel a { font-family: var(--font-body, "DM Sans", system-ui, sans-serif); display: block; padding: 14px 6px; font-size: 16px; font-weight: 600; color: var(--fg, #071843); border-bottom: 1px solid var(--border-light, #E7EBF4); text-decoration: none; }',
    '  .rw-nav .nav-mobile-panel a.is-active { color: var(--green-700, #067A43); }',
    '  .rw-nav .nav-mobile-panel a.nav-mobile-cta { margin-top: 14px; text-align: center; background: var(--accent, #071843); color: #fff; padding: 14px 24px; border-radius: 10px; border: none; }',
    '  body.nav-open { overflow: hidden; }',
    '  .rw-nav .nav-inner { padding: 0 16px; }',
    '}',
    '@media (prefers-reduced-motion: reduce) { .rw-nav .nav-mobile-panel { transition: none; } }'
  ].join('\n');

  var HAMBURGER = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';

  function esc(str) { return String(str).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  class RwNav extends HTMLElement {
    connectedCallback() {
      if (!document.getElementById('rw-nav-styles')) {
        var s = document.createElement('style');
        s.id = 'rw-nav-styles';
        s.textContent = CSS;
        document.head.appendChild(s);
      }

      var ctaText = this.getAttribute('cta-text') || 'Get started';
      var ctaHref = this.getAttribute('cta-href') || '#';
      var logoHref = this.getAttribute('logo-href') || './';
      var links = [];
      try { links = JSON.parse(this.getAttribute('links') || '[]'); } catch (e) {}

      function linkHtml(l) {
        return '<a href="' + esc(l.href || '#') + '"' + (l.slide !== undefined ? ' data-slide="' + esc(l.slide) + '"' : '') + '>' + esc(l.text) + '</a>';
      }

      var transparentUntilScroll = this.hasAttribute('transparent-until-scroll');
      var nav = document.createElement('nav');
      nav.className = 'rw-nav' + (transparentUntilScroll ? ' is-transparent' : '');
      nav.setAttribute('aria-label', 'Main');
      nav.innerHTML =
        '<div class="nav-inner">' +
          '<a href="' + esc(logoHref) + '" class="logo"><img src="brand/Really_Wise_Logo.svg" alt="ReallyWise" class="logo-img"></a>' +
          '<div class="nav-center">' + links.map(linkHtml).join('') + '</div>' +
          '<a href="' + esc(ctaHref) + '" class="nav-cta">' + esc(ctaText) + '</a>' +
          '<button type="button" class="nav-toggle" aria-label="Menu" aria-expanded="false">' + HAMBURGER + '</button>' +
        '</div>' +
        '<div class="nav-mobile-panel" aria-hidden="true">' +
          links.map(linkHtml).join('') +
          '<a href="' + esc(ctaHref) + '" class="nav-mobile-cta">' + esc(ctaText) + '</a>' +
        '</div>';

      this.parentNode.insertBefore(nav, this);

      var toggle = nav.querySelector('.nav-toggle');
      var panel = nav.querySelector('.nav-mobile-panel');
      var setOpen = function (open) {
        document.body.classList.toggle('nav-open', open);
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        panel.setAttribute('aria-hidden', open ? 'false' : 'true');
      };
      toggle.addEventListener('click', function (e) { e.stopPropagation(); setOpen(!document.body.classList.contains('nav-open')); });
      panel.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
      document.addEventListener('click', function (e) {
        if (!document.body.classList.contains('nav-open')) return;
        if (panel.contains(e.target) || toggle.contains(e.target)) return;
        setOpen(false);
      });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && document.body.classList.contains('nav-open')) setOpen(false); });
      window.addEventListener('resize', function () { if (window.innerWidth > 768 && document.body.classList.contains('nav-open')) setOpen(false); });

      if (transparentUntilScroll) {
        var untilSelector = this.getAttribute('transparent-until');
        var update = function () {
          var threshold = window.innerHeight * 0.7;
          var untilEl = untilSelector && document.querySelector(untilSelector);
          if (untilEl) threshold = untilEl.getBoundingClientRect().bottom + window.scrollY - 80;
          nav.classList.toggle('is-transparent', window.scrollY < threshold);
        };
        update();
        window.addEventListener('scroll', update, { passive: true });
        window.addEventListener('resize', update);
      }

      this.remove();
    }
  }

  customElements.define('rw-nav', RwNav);
})();
