(function () {
  if (customElements.get('rw-footer')) return;

  // ReallyWise site footer. Attribute: links = JSON array of { text, href, dataSlide }
  var CSS = [
    'rw-footer { display: contents; }',
    'footer.rw-footer { background: #fff; padding: 48px 0; border-top: 1px solid var(--border, #DCE1EC); }',
    'footer.rw-footer .footer-inner { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 24px; max-width: 1200px; margin: 0 auto; padding: 0 32px; }',
    'footer.rw-footer .footer-logo { display: flex; align-items: center; }',
    'footer.rw-footer .footer-logo img { height: 32px; width: auto; display: block; }',
    'footer.rw-footer .footer-links { display: flex; gap: 32px; }',
    'footer.rw-footer .footer-links a { font-family: var(--font-body, "DM Sans", system-ui, sans-serif); font-size: 14px; font-weight: 500; color: var(--fg-secondary, #4E5878); text-decoration: none; transition: color .2s; }',
    'footer.rw-footer .footer-links a:hover { color: var(--accent, #071843); }',
    'footer.rw-footer .footer-copy { font-family: var(--font-body, "DM Sans", system-ui, sans-serif); font-size: 13px; color: var(--fg-secondary, #4E5878); }',
    '@media (max-width: 768px) {',
    '  footer.rw-footer .footer-inner { flex-direction: column; text-align: center; padding: 0 16px; }',
    '}'
  ].join('\n');

  function esc(str) { return String(str).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  class RwFooter extends HTMLElement {
    connectedCallback() {
      if (!document.getElementById('rw-footer-styles')) {
        var s = document.createElement('style');
        s.id = 'rw-footer-styles';
        s.textContent = CSS;
        document.head.appendChild(s);
      }

      var links = [];
      try { links = JSON.parse(this.getAttribute('links') || '[]'); } catch (e) {}
      var linksHtml = links.map(function (l) {
        var extra = l.dataSlide !== undefined ? ' data-slide="' + esc(l.dataSlide) + '"' : '';
        return '<a href="' + esc(l.href) + '"' + extra + '>' + esc(l.text) + '</a>';
      }).join('');

      var footer = document.createElement('footer');
      footer.className = 'rw-footer';
      footer.innerHTML =
        '<div class="footer-inner">' +
          '<div class="footer-logo"><img src="brand/Really_Wise_Logo.svg" alt="ReallyWise"></div>' +
          '<div class="footer-links">' + linksHtml + '</div>' +
          '<p class="footer-copy">© 2026 ReallyWise. All rights reserved.</p>' +
        '</div>';

      this.parentNode.insertBefore(footer, this);
      this.remove();
    }
  }

  customElements.define('rw-footer', RwFooter);
})();
