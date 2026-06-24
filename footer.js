(function () {
  if (customElements.get('infina-footer')) return;

  var CSS = [
    'infina-footer { display: contents; }',
    'footer.infina-footer { background: #fff; padding: 48px 0; border-top: 1px solid var(--border-light, rgba(0,0,0,.08)); }',
    'footer.infina-footer .footer-inner { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 24px; max-width: 1200px; margin: 0 auto; padding: 0 32px; }',
    'footer.infina-footer .footer-logo { display: flex; align-items: center; }',
    'footer.infina-footer .footer-logo img { height: 23px; width: auto; display: block; }',
    'footer.infina-footer .footer-links { display: flex; gap: 32px; }',
    'footer.infina-footer .footer-links a { font-size: 14px; color: var(--muted, #9ca3af); transition: color .2s; text-decoration: none; }',
    'footer.infina-footer .footer-links a:hover { color: var(--accent, #001F5C); }',
    'footer.infina-footer .footer-copy { font-size: 13px; color: var(--muted, #9ca3af); }',
    '@media (max-width: 640px) {',
    '  footer.infina-footer .footer-inner { flex-direction: column; text-align: center; padding: 0 16px; }',
    '}'
  ].join('\n');

  class InfinaFooter extends HTMLElement {
    connectedCallback() {
      if (!document.getElementById('infina-footer-styles')) {
        var s = document.createElement('style');
        s.id = 'infina-footer-styles';
        s.textContent = CSS;
        document.head.appendChild(s);
      }

      var footer = document.createElement('footer');
      footer.className = 'infina-footer';
      footer.innerHTML =
        '<div class="footer-inner">' +
          '<div class="footer-logo">' +
            '<img src="uploads/infina-ai-logo-web-329e3857.png" alt="Infina AI">' +
          '</div>' +
          '<div class="footer-links">' +
            '<a href="inside.html">Inside</a>' +
            '<a href="work.html">Work</a>' +
            '<a href="personal.html">Personal</a>' +
            '<a href="salesx.html">SalesX</a>' +
          '</div>' +
          '<p class="footer-copy">© 2026 Infina. All rights reserved.</p>' +
        '</div>';

      this.parentNode.insertBefore(footer, this);
      this.remove();
    }
  }

  customElements.define('infina-footer', InfinaFooter);
})();
