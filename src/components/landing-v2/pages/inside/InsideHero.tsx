/**
 * Inside page hero section.
 * Mirrors inside.html L5488-5528 <section class="hero" id="hero">
 */
const InsideHero = () => {
  const handleDemo = (e: React.MouseEvent<HTMLAnchorElement>) => {
    e.preventDefault();
    const el = document.getElementById("demo");
    if (el) el.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <section className="hero" id="hero">
      <div className="hero-bg" />
      <div className="hero-grid-bg" />
      <div className="shape shape-1" />
      <div className="shape shape-2" />
      <div className="shape shape-3" />
      <div className="shape shape-4" />
      <div className="container">
        <div className="hero-grid">
          <div className="hero-text">
            <div className="hero-badge">For Products</div>
            <h1>
              <span className="line">Your AI Specialist, built in.</span>
              <br />
              <span className="line line-accent">More engaged customers.</span>
              <br />
              <span className="line line-accent">More revenue. Zero build time.</span>
            </h1>
            <ul className="hero-value-list">
              <li>
                <span className="hero-value-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                    <rect x="5" y="2" width="14" height="20" rx="2" />
                    <path d="M12 18h.01" />
                    <path d="M9 6h6M9 10h6" />
                  </svg>
                </span>
                <span><strong>AI Specialist</strong> integrated on your app or web</span>
              </li>
              <li>
                <span className="hero-value-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M13 2L4.5 14h6l-1 8L19 10h-6z" />
                  </svg>
                </span>
                Go live in weeks, not months
              </li>
              <li>
                <span className="hero-value-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                    <polyline points="22 7 13.5 15.5 8.5 10.5 2 17" />
                    <polyline points="16 7 22 7 22 13" />
                  </svg>
                </span>
                Help customers make better financial decisions
              </li>
            </ul>
            <div className="hero-cta-row">
              <a href="#demo" className="btn-primary" onClick={handleDemo}>
                Book a demo →
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default InsideHero;
