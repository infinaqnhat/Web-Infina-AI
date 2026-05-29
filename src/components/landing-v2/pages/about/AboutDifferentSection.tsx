/**
 * About page "What Makes Us Different" section — mirrors about.html L1205–1259.
 * Pure static markup — CSS handles card animations via nth-child delay rules
 * in landing-about.css. No JS conversion needed.
 */
const AboutDifferentSection = () => (
  <section className="different">
    <div className="container">
      <div className="different-header">
        <h2>What Makes Us Different</h2>
      </div>

      <div className="different-grid">
        {/* Card 1 */}
        <div className="different-card">
          <div className="different-icon">
            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M12 2L2 7l10 5 10-5-10-5z" />
              <path d="M2 17l10 5 10-5" />
              <path d="M2 12l10 5 10-5" />
            </svg>
          </div>
          <h3 className="different-title">Proven in Production, Not a Prototype</h3>
          <p className="different-desc">
            Infina AI Inside isn't a demo. It's built on AI that's already
            tested by real users with real money — not built speculatively for
            a sales deck.
          </p>
        </div>

        {/* Card 2 */}
        <div className="different-card">
          <div className="different-icon">
            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
              <circle cx="9" cy="7" r="4" />
              <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
              <path d="M16 3.13a4 4 0 0 1 0 7.75" />
            </svg>
          </div>
          <h3 className="different-title">Multi-Agent Architecture</h3>
          <p className="different-desc">
            A flexible family of multi-agent specialists — stocks agents,
            investing, budgeting, wealth management — each fine-tuned on real
            financial conversations.
          </p>
        </div>

        {/* Card 3 */}
        <div className="different-card">
          <div className="different-icon">
            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <circle cx="12" cy="12" r="10" />
              <path d="M12 6v6l4 2" />
            </svg>
          </div>
          <h3 className="different-title">Country-Specific Expertise</h3>
          <p className="different-desc">
            Deep understanding of local markets, regulations, and language
            nuances. Built for Southeast Asia, expanding globally.
          </p>
        </div>

        {/* Card 4 */}
        <div className="different-card">
          <div className="different-icon">
            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />
            </svg>
          </div>
          <h3 className="different-title">Fastest Path to Live AI</h3>
          <p className="different-desc">
            Live in 3 weeks from decision to live AI in your app. No drawn-out
            roadmap. You're embedding what's already running.
          </p>
        </div>
      </div>
    </div>
  </section>
);

export default AboutDifferentSection;
