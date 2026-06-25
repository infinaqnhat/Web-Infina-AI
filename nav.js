(function () {
  if (customElements.get('infina-nav')) return;

  var CSS = [
    'infina-nav { display: contents; }',
    'nav.infina-nav { position: fixed; top: 0; left: 0; right: 0; background: rgba(255,255,255,.9); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border-light, rgba(0,0,0,.08)); z-index: 1000; }',
    '.nav-inner { display: flex; align-items: center; justify-content: space-between; height: 72px; max-width: 1200px; margin: 0 auto; padding: 0 32px; }',
    '.logo { display: flex; align-items: center; gap: 10px; font-size: 22px; font-weight: 600; letter-spacing: -0.03em; }',
    '.logo-img { height: 23px; width: auto; display: block; }',
    '.nav-center { display: flex; align-items: center; gap: 40px; }',
    '.nav-center a { font-size: 15px; font-weight: 500; color: var(--fg-secondary, #6b7280); transition: color .2s; position: relative; text-decoration: none; }',
    '.nav-center a.active { color: var(--fg, #111827); }',
    '.nav-center a::after { content: ""; position: absolute; bottom: -4px; left: 0; width: 0; height: 2px; background: var(--accent, #001F5C); transition: width .3s; }',
    '.nav-center a.active::after, .nav-center a:hover::after { width: 100%; }',
    '.nav-cta { background: var(--accent, #001F5C); color: #fff !important; padding: 11px 22px; border-radius: 9999px; font-size: 14px; font-weight: 500; transition: all .3s; text-decoration: none; }',
    '.nav-cta:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,.2); }',
    '.nav-cta::after { display: none !important; }',
    '.nav-dropdown { position: relative; }',
    '.nav-dropdown-toggle { font-size: 15px; font-weight: 500; color: var(--fg-secondary, #6b7280); transition: color .2s; position: relative; cursor: pointer; display: flex; align-items: center; gap: 4px; user-select: none; }',
    '.nav-dropdown-toggle.active { color: var(--fg, #111827); }',
    '.nav-dropdown-toggle::after { content: ""; position: absolute; bottom: -4px; left: 0; width: 0; height: 2px; background: var(--accent, #001F5C); transition: width .3s; }',
    '.nav-dropdown:hover .nav-dropdown-toggle::after { width: calc(100% - 16px); }',
    '.nav-dropdown-toggle svg { transition: transform .2s; flex-shrink: 0; }',
    '.nav-dropdown:hover .nav-dropdown-toggle svg { transform: rotate(180deg); }',
    '.nav-dropdown-menu { position: absolute; top: calc(100% + 16px); left: 50%; transform: translateX(-50%) translateY(-4px); background: #fff; border: 1px solid var(--border, rgba(0,0,0,.1)); border-radius: 12px; box-shadow: 0 12px 40px rgba(0,0,0,.1); padding: 6px; min-width: 200px; opacity: 0; visibility: hidden; transition: opacity .2s, visibility .2s, transform .2s; }',
    '.nav-dropdown:hover .nav-dropdown-menu { opacity: 1; visibility: visible; transform: translateX(-50%) translateY(0); }',
    '.nav-dropdown-menu a { display: block; padding: 10px 14px; font-size: 14px; font-weight: 500; color: var(--fg-secondary, #6b7280); border-radius: 8px; transition: background .15s, color .15s; white-space: nowrap; text-decoration: none; }',
    '.nav-dropdown-menu a::after { display: none !important; }',
    '.nav-dropdown-menu a:hover, .nav-dropdown-menu a.active { background: var(--accent-light, rgba(24,99,220,.08)); color: var(--accent, #001F5C); }',
    '.nav-toggle { display: none; background: none; border: none; cursor: pointer; padding: 8px; color: var(--fg-secondary, #6b7280); transition: color .2s; }',
    '.nav-toggle:hover { color: var(--accent, #001F5C); }',
    '.nav-toggle svg { width: 24px; height: 24px; display: block; }',
    '.nav-mobile-panel { display: none; }',
    '@media (max-width: 768px) {',
    '  nav.infina-nav .nav-center { display: none; }',
    '  nav.infina-nav .nav-cta { display: none; }',
    '  .nav-toggle { display: block; }',
    '  .nav-mobile-panel { display: flex; flex-direction: column; position: fixed; top: 72px; left: 0; right: 0; background: rgba(255,255,255,.98); backdrop-filter: blur(20px); padding: 8px 24px 20px; gap: 0; border-bottom: 1px solid var(--border-light, rgba(0,0,0,.08)); box-shadow: 0 10px 30px rgba(0,0,0,.06); transform: translateY(-12px); opacity: 0; visibility: hidden; transition: transform .25s ease, opacity .25s ease, visibility .25s ease; z-index: 999; }',
    '  body.nav-open .nav-mobile-panel { transform: translateY(0); opacity: 1; visibility: visible; }',
    '  .nav-mobile-panel a { padding: 14px 6px; font-size: 16px; font-weight: 500; color: var(--fg-secondary, #6b7280); border-bottom: 1px solid var(--border-light, rgba(0,0,0,.08)); text-decoration: none; display: block; }',
    '  .nav-mobile-panel a:last-child { border-bottom: none; }',
    '  .nav-mobile-group { border-bottom: 1px solid var(--border-light, rgba(0,0,0,.08)); }',
    '  .nav-mobile-group-row { display: flex; align-items: center; justify-content: space-between; }',
    '  .nav-mobile-group-row a { border-bottom: none; flex: 1; }',
    '  .nav-mobile-chevron { background: none; border: none; cursor: pointer; padding: 14px 6px; color: var(--fg-secondary, #6b7280); display: flex; align-items: center; transition: color .2s; }',
    '  .nav-mobile-chevron svg { width: 16px; height: 16px; transition: transform .25s; }',
    '  .nav-mobile-chevron.open svg { transform: rotate(180deg); }',
    '  .nav-mobile-children { display: none; background: var(--surface, #f9fafb); border-top: 1px solid var(--border-light, rgba(0,0,0,.08)); }',
    '  .nav-mobile-children.open { display: block; }',
    '  .nav-mobile-children a { padding: 11px 6px 11px 28px; font-size: 14px; font-weight: 400; color: var(--muted, #9ca3af); border-bottom: 1px solid var(--border-light, rgba(0,0,0,.08)); }',
    '  .nav-mobile-children a:last-child { border-bottom: none; }',
    '  .nav-mobile-children a.active { color: var(--accent, #001F5C); font-weight: 500; }',
    '  .nav-mobile-panel a.nav-mobile-cta { margin-top: 14px; text-align: center; background: var(--accent, #001F5C); color: #fff; padding: 14px 24px; border-radius: 9999px; border: none; font-weight: 600; }',
    '  body.nav-open { overflow: hidden; }',
    '  .nav-inner { padding: 0 16px; }',
    '}'
  ].join('\n');

  var LOGO_SVG = '<img src="uploads/infina-ai-logo-web-329e3857.png" alt="Infina AI" class="logo-img">';
  var CHEVRON = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>';
  var HAMBURGER = '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';

  class InfinaNav extends HTMLElement {
    connectedCallback() {
    if (!document.getElementById('infina-nav-styles')) {
      var s = document.createElement('style');
      s.id = 'infina-nav-styles';
      s.textContent = CSS;
      document.head.appendChild(s);
    }

    var active = this.getAttribute('active') || '';
    var isInside = active === 'inside';
    var isWork = active === 'work';
    var isFocus = active === 'focus-alignment';
    var isWorkGroup = isWork || isFocus;
    var isPersonal = active === 'personal';
    var isAbout = active === 'about';
    var isSalesX = active === 'salesx';

    var nav = document.createElement('nav');
    nav.className = 'infina-nav';

    var toggleClass = 'nav-dropdown-toggle' + (isWorkGroup ? ' active' : '');
    nav.innerHTML =
      '<div class="nav-inner">' +
        '<a href="home.html" class="logo">' + LOGO_SVG + '</a>' +
        '<div class="nav-center">' +
          '<a href="inside.html"' + (isInside ? ' class="active"' : '') + '>AI Inside</a>' +
          '<a href="work.html"' + (isWork ? ' class="active"' : '') + '>AI Work</a>' +
          '<a href="personal.html"' + (isPersonal ? ' class="active"' : '') + '>AI Personal</a>' +
          '<a href="salesx.html"' + (isSalesX ? ' class="active"' : '') + '>AI SalesX</a>' +
        '</div>' +
        '<a href="#demo" class="nav-cta">Book a demo</a>' +
      '</div>';

    this.parentNode.insertBefore(nav, this);

    var navInner = nav.querySelector('.nav-inner');

    var toggle = document.createElement('button');
    toggle.className = 'nav-toggle';
    toggle.setAttribute('aria-label', 'Menu');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.innerHTML = HAMBURGER;
    navInner.appendChild(toggle);

    var panel = document.createElement('div');
    panel.className = 'nav-mobile-panel';
    panel.setAttribute('aria-hidden', 'true');

    // AI Inside
    var aInside = document.createElement('a');
    aInside.href = 'inside.html';
    aInside.textContent = 'AI Inside';
    if (isInside) aInside.classList.add('active');
    panel.appendChild(aInside);

    // AI Work group (collapsible)
    var group = document.createElement('div');
    group.className = 'nav-mobile-group';

    var aWork = document.createElement('a');
    aWork.href = 'work.html';
    aWork.textContent = 'AI Work';
    if (isWork) aWork.classList.add('active');

    group.appendChild(aWork);
    panel.appendChild(group);

    // AI Personal
    var aPersonal = document.createElement('a');
    aPersonal.href = 'personal.html';
    aPersonal.textContent = 'AI Personal';
    if (isPersonal) aPersonal.classList.add('active');
    panel.appendChild(aPersonal);

    // AI SalesX
    var aSalesX = document.createElement('a');
    aSalesX.href = 'salesx.html';
    aSalesX.textContent = 'AI SalesX';
    if (isSalesX) aSalesX.classList.add('active');
    panel.appendChild(aSalesX);

    // Book a demo CTA
    var aCta = document.createElement('a');
    aCta.href = '#demo';
    aCta.textContent = 'Book a demo';
    aCta.className = 'nav-mobile-cta';
    panel.appendChild(aCta);

    nav.appendChild(panel);

    var setOpen = function (open) {
      document.body.classList.toggle('nav-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      panel.setAttribute('aria-hidden', open ? 'false' : 'true');
    };

    toggle.addEventListener('click', function (e) {
      e.stopPropagation();
      setOpen(!document.body.classList.contains('nav-open'));
    });

    panel.querySelectorAll('a:not(.nav-mobile-group-row a)').forEach(function (a) {
      a.addEventListener('click', function () { setOpen(false); });
    });
    aWork.addEventListener('click', function () { setOpen(false); });

    document.addEventListener('click', function (e) {
      if (!document.body.classList.contains('nav-open')) return;
      if (panel.contains(e.target) || toggle.contains(e.target)) return;
      setOpen(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && document.body.classList.contains('nav-open')) setOpen(false);
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 768 && document.body.classList.contains('nav-open')) setOpen(false);
    });

    this.remove();
  }
}

  customElements.define('infina-nav', InfinaNav);
})();
