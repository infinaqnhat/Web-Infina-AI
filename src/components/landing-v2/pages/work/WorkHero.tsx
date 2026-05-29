/**
 * Work page hero section.
 * Mirrors <section class="hero"> in Web-Infina-AI/work.html L940–978.
 *
 * Divergences from infina-pfa-80389 reference:
 *  - hero-badge text: "For Business" (was "B2B · For Enterprise")
 *  - bullet list: class="hero-value-list" with hero-value-icon SVGs (was "hero-bullets" plain li)
 *  - CTAs: single "Book a demo →" only (was two buttons incl. "Explore agents")
 */
const WorkHero = () => {
  const scrollToAnchor = (targetId: string) => (e: React.MouseEvent<HTMLAnchorElement>) => {
    e.preventDefault();
    const el = document.getElementById(targetId);
    if (el) el.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <section className="hero">
      <div className="hero-bg" />
      <div className="hero-grid-bg" />
      <div className="shape shape-1" />
      <div className="shape shape-2" />
      <div className="shape shape-3" />
      <div className="shape shape-4" />
      <div className="container">
        <div className="hero-grid">
          <div className="hero-text">
            <div className="hero-badge">For Business</div>
            <h1>
              <span className="line">Your team, working at their best</span>
              <br />
              <span className="line line-accent">with AI handling the rest.</span>
            </h1>
            <ul className="hero-value-list">
              <li>
                <span className="hero-value-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                  </svg>
                </span>
                Integrate in Slack and WhatsApp
              </li>
              <li>
                <span className="hero-value-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                    <polyline points="23 4 23 10 17 10" />
                    <polyline points="1 20 1 14 7 14" />
                    <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15" />
                  </svg>
                </span>
                Automates updates, tracking, and routine workflows 24/7
              </li>
              <li>
                <span className="hero-value-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
                    <circle cx="9" cy="7" r="4" />
                    <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
                    <path d="M16 3.13a4 4 0 0 1 0 7.75" />
                  </svg>
                </span>
                Frees your team for decisions and the work that moves business forward
              </li>
            </ul>
            <div className="hero-ctas">
              <a href="#demo" className="btn-primary" onClick={scrollToAnchor("demo")}>
                Book a demo →
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default WorkHero;
