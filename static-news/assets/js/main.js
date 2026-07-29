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
