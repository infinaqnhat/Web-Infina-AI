(function () {
  var toggle = document.querySelector('.nav-toggle');
  if (!toggle) return;

  function setOpen(open) {
    document.body.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  toggle.addEventListener('click', function (e) {
    e.stopPropagation();
    setOpen(!document.body.classList.contains('nav-open'));
  });

  document.addEventListener('click', function (e) {
    if (!document.body.classList.contains('nav-open')) return;
    var panel = document.querySelector('.nav-mobile-panel');
    if ((panel && panel.contains(e.target)) || toggle.contains(e.target)) return;
    setOpen(false);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') setOpen(false);
  });

  window.addEventListener('resize', function () {
    if (window.innerWidth > 768) setOpen(false);
  });
})();

/* ===== AJAX pagination for the News table (keeps viewport) ===== */
(function () {
  var container = document.querySelector('.nr-table');
  if (!container) return;

  function loadPage(url, push) {
    container.classList.add('is-loading');
    fetch(url, { headers: { 'X-Requested-With': 'fetch' }, credentials: 'same-origin' })
      .then(function (res) {
        if (!res.ok) throw new Error('bad response');
        return res.text();
      })
      .then(function (html) {
        var doc = new DOMParser().parseFromString(html, 'text/html');
        var next = doc.querySelector('.nr-table');
        if (!next) throw new Error('no news block');
        container.innerHTML = next.innerHTML;
        container.classList.remove('is-loading');
        if (push) history.pushState({ nrAjax: true }, '', url);
      })
      .catch(function () {
        window.location.href = url; // graceful fallback
      });
  }

  document.addEventListener('click', function (e) {
    var link = e.target.closest('.nr-table .wp-block-query-pagination a');
    if (!link) return;
    e.preventDefault();
    loadPage(link.href, true);
  });

  window.addEventListener('popstate', function (e) {
    if (e.state && e.state.nrAjax) loadPage(location.href, false);
  });
})();
