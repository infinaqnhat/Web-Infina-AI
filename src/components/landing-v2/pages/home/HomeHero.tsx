/**
 * Hero section — mirrors home.html `.hero` (h1 "AI Specialists for Every Job"
 * + hero-feature trio).
 *
 * The "Infina AI Core" feature link targets the #core-v2 section on the same
 * page (plain anchor — LandingHome handles hash scroll).
 */
const HomeHero = () => (
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
          <h1>
            <span className="line">AI Specialists for</span>
            <br />
            <span className="line line-accent">Every Job</span>
          </h1>
          <p className="hero-sub">
            Specialist AI agents with domain expertise that perform deep
            analysis, execute complex tasks, and automate workflows.
          </p>

          <div className="hero-features">
            <div className="hero-feature">
              <div className="hero-feature-icon">
                <svg viewBox="0 0 24 24">
                  <circle cx="12" cy="8" r="4" />
                  <path d="M4 21v-1a6 6 0 0 1 6-6h4a6 6 0 0 1 6 6v1" />
                </svg>
              </div>
              <h3>Domain-trained specialists</h3>
              <p>Trained on your industry's rules, products, and workflows.</p>
            </div>
            <div className="hero-feature">
              <div className="hero-feature-icon">
                <svg viewBox="0 0 24 24">
                  <rect x="3" y="3" width="7" height="7" rx="1.5" />
                  <rect x="14" y="3" width="7" height="7" rx="1.5" />
                  <rect x="3" y="14" width="7" height="7" rx="1.5" />
                  <rect x="14" y="14" width="7" height="7" rx="1.5" />
                </svg>
              </div>
              <h3>Built for any industry</h3>
              <p>
                Any vertical, any product, powered by{" "}
                <a href="#core-v2">Infina AI Core</a>.
              </p>
            </div>
            <div className="hero-feature">
              <div className="hero-feature-icon">
                <svg viewBox="0 0 24 24">
                  <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
                </svg>
              </div>
              <h3>Go live in days</h3>
              <p>Pre-built agents, connectors, and compliance. Zero build time.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
);

export default HomeHero;
