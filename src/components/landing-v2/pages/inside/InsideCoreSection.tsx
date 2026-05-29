/**
 * Inside page "How it Works" section.
 * Mirrors inside.html L5619-5709 <section class="core" id="how-it-works">
 * 4-step journey panel with animated connectors.
 */
const InsideCoreSection = () => (
  <section className="core" id="how-it-works">
    <div className="container">
      <div className="core-layout">

        <div className="core-left">
          <span className="section-eyebrow-plain">How it Works</span>
          <h2>
            One integration.
            <br />
            <span className="accent-text">Infinite reach.</span>
          </h2>
          <p className="core-left-desc">
            Your customers get access to an AI Specialist Agent, fully embedded within your
            application. No switching, no extra apps, no friction.
          </p>
        </div>

        <div>
          <div className="step-journey-panel">
            <div className="step-journey">

              <div className="step-item">
                <div className="step-num-row">
                  <div className="step-num">1</div>
                  <div className="step-connector" aria-hidden="true">
                    <div className="step-connector-track" />
                    <div className="step-connector-stream" />
                    <div className="step-connector-dot" />
                    <div className="step-connector-dot" />
                    <div className="step-connector-dot" />
                  </div>
                </div>
                <div className="step-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="#1863dc" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                    <rect x="6" y="2" width="12" height="20" rx="2.5" />
                    <path d="M11 18h2" />
                  </svg>
                </div>
                <div className="step-title">Your Platform</div>
                <div className="step-sub">Your existing app or web product</div>
              </div>

              <div className="step-item">
                <div className="step-num-row">
                  <div className="step-num">2</div>
                  <div className="step-connector" aria-hidden="true">
                    <div className="step-connector-track" />
                    <div className="step-connector-stream" style={{ animationDelay: "0.3s" }} />
                    <div className="step-connector-dot" style={{ animationDelay: "0.3s" }} />
                    <div className="step-connector-dot" style={{ animationDelay: "0.9s" }} />
                    <div className="step-connector-dot" style={{ animationDelay: "1.5s" }} />
                  </div>
                </div>
                <div className="step-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="#1863dc" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                    <polyline points="16 18 22 12 16 6" />
                    <polyline points="8 6 2 12 8 18" />
                  </svg>
                </div>
                <div className="step-title">Add the SDK</div>
                <div className="step-sub">White-label UI drops in seamlessly</div>
              </div>

              <div className="step-item">
                <div className="step-num-row">
                  <div className="step-num">3</div>
                  <div className="step-connector" aria-hidden="true">
                    <div className="step-connector-track" />
                    <div className="step-connector-stream" style={{ animationDelay: "0.6s" }} />
                    <div className="step-connector-dot" style={{ animationDelay: "0.6s" }} />
                    <div className="step-connector-dot" style={{ animationDelay: "1.2s" }} />
                    <div className="step-connector-dot" style={{ animationDelay: "1.8s" }} />
                  </div>
                </div>
                <div className="step-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="#1863dc" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                    <circle cx="12" cy="12" r="9" />
                    <path d="M12 7v5l3 2" />
                  </svg>
                </div>
                <div className="step-title">AI Powers It</div>
                <div className="step-sub">Specialist layer + compliance built in</div>
              </div>

              <div className="step-item">
                <div className="step-num-row">
                  <div className="step-num">4</div>
                </div>
                <div className="step-icon" style={{ borderColor: "rgba(20,154,110,0.2)" }}>
                  <svg viewBox="0 0 24 24" fill="none" stroke="#149a6e" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                    <circle cx="12" cy="9" r="3.5" />
                    <path d="M5 20c1-3.5 4-5.5 7-5.5s6 2 7 5.5" />
                  </svg>
                </div>
                <div className="step-title">Customers Get Value</div>
                <div className="step-sub">AI specialist in every screen, 24/7</div>
              </div>

            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
);

export default InsideCoreSection;
