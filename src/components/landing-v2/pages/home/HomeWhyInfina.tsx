// NEW component — mirrors home.html L5369–5430 <section class="why-infina" id="why-infina">
// Section is inside an HTML comment in home.html (hidden, preserved for reuse).
// Ported here as a visible React component per phase-03 spec.

/**
 * Why Infina AI section — converts HTML markup directly to TSX.
 * All class names preserved verbatim from home.html so landing-home.css
 * selectors resolve unchanged. SVG attributes converted to camelCase per JSX rules.
 * HTML comment: "WHY INFINA AI SECTION - hidden, preserved for reuse"
 *
 * Note: HTML uses <span class="eyebrow"> (not "section-eyebrow") — preserved verbatim.
 */
const HomeWhyInfina = () => (
  <section className="why-infina" id="why-infina">
    <div className="container">
      <div className="section-header">
        <span className="eyebrow">Why Infina AI</span>
        <h2>
          The faster path <span className="accent">to AI that works</span>
        </h2>
      </div>

      <div className="why-grid">
        <div className="why-item">
          <span className="why-item-num">01</span>
          <div className="why-item-icon" aria-hidden="true">
            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M12 1v22" />
              <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
            </svg>
          </div>
          <h4>Cost optimization</h4>
          <p>
            No need to invest in an in-house AI team. Costs tied to actual
            value, pay per use and scale flexibly with revenue.
          </p>
        </div>

        <div className="why-item">
          <span className="why-item-num">02</span>
          <div className="why-item-icon" aria-hidden="true">
            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
              <polyline points="9 12 11 14 15 10" />
            </svg>
          </div>
          <h4>Minimize risk</h4>
          <p>
            Infina AI commits and takes responsibility for the quality of advice
            and information that the AI system provides to end users.
          </p>
        </div>

        <div className="why-item">
          <span className="why-item-num">03</span>
          <div className="why-item-icon" aria-hidden="true">
            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M13 2 3 14h8l-1 8 10-12h-8l1-8z" />
            </svg>
          </div>
          <h4>Shorten time to market</h4>
          <p>
            Deploy in just 3 weeks via API, Webview or Infina AI SDKs, ready to
            bring your AI product to market quickly.
          </p>
        </div>

        <div className="why-item">
          <span className="why-item-num">04</span>
          <div className="why-item-icon" aria-hidden="true">
            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <ellipse cx="12" cy="6" rx="9" ry="3" />
              <path d="M3 6v6c0 1.66 4 3 9 3s9-1.34 9-3V6" />
              <path d="M3 12v6c0 1.66 4 3 9 3s9-1.34 9-3v-6" />
            </svg>
          </div>
          <h4>No training data shortage</h4>
          <p>
            System trained and continuously improved from millions of real
            interactions each month on Infina.ai platform.
          </p>
        </div>
      </div>
    </div>
  </section>
);

export default HomeWhyInfina;
