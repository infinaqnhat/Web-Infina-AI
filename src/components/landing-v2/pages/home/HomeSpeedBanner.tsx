import React from "react";

// NEW component — mirrors home.html L5074–5286 <section class="speed-banner">
// Section is inside an HTML comment in home.html (hidden, preserved for reuse).
// Ported here as a visible React component per phase-03 spec.

/**
 * Speed Banner section — converts HTML markup directly to TSX.
 * All class names preserved verbatim from home.html so landing-home.css
 * selectors resolve unchanged. SVG attributes converted to camelCase per JSX rules.
 * HTML comment: "SPEED BANNER SECTION - hidden, preserved for reuse"
 */
const HomeSpeedBanner = () => (
  <section className="speed-banner">
    <div className="container">
      <div className="speed-grid">
        <div className="speed-text">
          <span className="speed-pill">
            <span className="speed-pill-dot" />
            Time to Deploy
          </span>
          <h2 className="speed-headline">
            Just <span className="speed-accent">2–3 weeks</span> to get AI
            ready on your{" "}
            <span className="speed-accent" style={{ fontStyle: "italic" }}>
              app
            </span>
            ,{" "}
            <span className="speed-accent" style={{ fontStyle: "italic" }}>
              web
            </span>
            , or{" "}
            <span className="speed-accent" style={{ fontStyle: "italic" }}>
              internal
            </span>{" "}
            business systems.
          </h2>

          <div className="speed-timeline" aria-hidden="true">
            <div className="speed-tl-track">
              <div className="speed-tl-fill" />
            </div>
            <div className="speed-tl-steps">
              <div className="speed-tl-step">
                <span className="speed-tl-dot" />
                <small>Week 1</small>
                <strong>Setup</strong>
              </div>
              <div className="speed-tl-step">
                <span className="speed-tl-dot" />
                <small>Week 2</small>
                <strong>Integration</strong>
              </div>
              <div className="speed-tl-step">
                <span className="speed-tl-dot" />
                <small>Week 3</small>
                <strong>Fine-tune</strong>
              </div>
              <div className="speed-tl-step is-live">
                <span className="speed-tl-dot" />
                <small>LAUNCH</small>
                <strong>Live</strong>
              </div>
            </div>
          </div>

          <div className="speed-benefits-grid">
            <div className="benefit-card" style={{ "--i": 0 } as React.CSSProperties}>
              <div className="benefit-icon">
                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="1.8"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M3 17l5-5 3 3 7-8" />
                  <path d="M14 7h4v4" />
                </svg>
              </div>
              <div className="benefit-body">
                <strong>Increase revenue, reduce costs</strong>
                <small>Automate operations, increase efficiency</small>
              </div>
            </div>

            <div className="benefit-card" style={{ "--i": 1 } as React.CSSProperties}>
              <div className="benefit-icon">
                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="1.8"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <circle cx="12" cy="8" r="3" />
                  <path d="M4 21v-2a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v2" />
                </svg>
              </div>
              <div className="benefit-body">
                <strong>Onboarding &amp; Conversion</strong>
                <small>Guide new users, shorten product activation time</small>
              </div>
            </div>

            <div className="benefit-card" style={{ "--i": 2 } as React.CSSProperties}>
              <div className="benefit-icon">
                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="1.8"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M12 3l2 5 5 2-5 2-2 5-2-5-5-2 5-2z" />
                </svg>
              </div>
              <div className="benefit-body">
                <strong>Personalized advice</strong>
                <small>
                  Recommend right products to right people at right time like
                  1-1 expert
                </small>
              </div>
            </div>

            <div className="benefit-card" style={{ "--i": 3 } as React.CSSProperties}>
              <div className="benefit-icon">
                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="1.8"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <rect x="3" y="3" width="7" height="7" rx="1.5" />
                  <rect x="14" y="3" width="7" height="7" rx="1.5" />
                  <rect x="3" y="14" width="7" height="7" rx="1.5" />
                  <path d="M14 17.5h7M17.5 14v7" />
                </svg>
              </div>
              <div className="benefit-body">
                <strong>Effective cross-sell</strong>
                <small>
                  Leverage behavioral data, context-aware cross-sell suggestions
                </small>
              </div>
            </div>
          </div>
        </div>

        <div className="speed-visual" aria-hidden="true">
          <div className="phone">
            <div className="phone-notch" />
            <div className="phone-screen">
              <div className="phone-status">
                <span>9:41</span>
                <span className="phone-status-icons">
                  <svg viewBox="0 0 18 12" fill="currentColor">
                    <rect x="0" y="6" width="3" height="6" rx="1" />
                    <rect x="5" y="4" width="3" height="8" rx="1" />
                    <rect x="10" y="2" width="3" height="10" rx="1" />
                    <rect x="15" y="0" width="3" height="12" rx="1" />
                  </svg>
                  <svg
                    viewBox="0 0 20 12"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="1.5"
                  >
                    <rect x="1" y="2" width="16" height="8" rx="2" />
                    <rect x="18" y="5" width="1.5" height="2" />
                    <rect
                      x="2.5"
                      y="3.5"
                      width="11"
                      height="5"
                      rx="1"
                      fill="currentColor"
                      stroke="none"
                    />
                  </svg>
                </span>
              </div>

              <div className="phone-header">
                <div className="phone-avatar">
                  <svg
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="1.6"
                    strokeLinecap="round"
                  >
                    <circle cx="12" cy="9" r="3.2" />
                    <path d="M5 20c1-3.5 4-5.5 7-5.5s6 2 7 5.5" />
                  </svg>
                </div>
                <div className="phone-greeting">
                  <small>Hello,</small>
                  <strong>Minh Anh!</strong>
                </div>
                <button className="phone-icon-btn" aria-label="settings">
                  <svg
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="1.6"
                    strokeLinecap="round"
                  >
                    <circle cx="12" cy="12" r="3" />
                    <path d="M12 2v3M12 19v3M22 12h-3M5 12H2M19.07 4.93l-2.12 2.12M7.05 16.95l-2.12 2.12M19.07 19.07l-2.12-2.12M7.05 7.05L4.93 4.93" />
                  </svg>
                </button>
              </div>

              <div className="phone-balance">
                <div className="phone-balance-row">
                  <span className="phone-balance-label">Available balance</span>
                  <span className="phone-balance-trend">
                    <svg
                      viewBox="0 0 12 12"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                    >
                      <polyline points="2 9 5 6 7 8 10 4" />
                    </svg>
                    +12.4%
                  </span>
                </div>
                <div className="phone-balance-value">2.560.500.000 ₫</div>
                <div className="phone-balance-actions">
                  <div className="phone-action">
                    <span>↗</span>
                    <small>Deposit</small>
                  </div>
                  <div className="phone-action">
                    <span>↙</span>
                    <small>Withdraw</small>
                  </div>
                  <div className="phone-action">
                    <span>⇄</span>
                    <small>Transfer</small>
                  </div>
                </div>
              </div>

              <div className="phone-ai-card">
                <div className="phone-ai-header">
                  <span className="phone-ai-badge">
                    <span className="phone-ai-dot" />
                    AI Advisor
                  </span>
                </div>

                <div className="phone-goal">
                  <div className="phone-goal-top">
                    <span className="phone-goal-icon" aria-hidden="true">
                      <svg
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="1.8"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      >
                        <circle cx="12" cy="12" r="9" />
                        <circle cx="12" cy="12" r="5" />
                        <circle cx="12" cy="12" r="1.5" fill="currentColor" />
                      </svg>
                    </span>
                    <div className="phone-goal-info">
                      <small>Goal • 85%</small>
                      <strong>Buy house</strong>
                    </div>
                    <span className="phone-goal-badge">
                      <svg
                        viewBox="0 0 12 12"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      >
                        <polyline points="2 8 5 5 7 7 10 4" />
                      </svg>
                      +15%
                    </span>
                  </div>
                  <div className="phone-progress">
                    <div className="phone-progress-bar" />
                  </div>
                  <div className="phone-goal-stats">
                    <div className="phone-stat">
                      <small>Growth</small>
                      <strong className="phone-stat-up">+26%</strong>
                    </div>
                    <div className="phone-stat-divider" />
                    <div className="phone-stat">
                      <small>Remaining</small>
                      <strong>5 months</strong>
                    </div>
                  </div>
                </div>

                <p className="phone-ai-msg">
                  Increase contribution to reach goal sooner?
                </p>

                <div className="phone-ai-actions">
                  <button className="phone-btn-primary">
                    <svg
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    >
                      <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" />
                    </svg>
                    Chat with AI
                  </button>
                </div>
                <div className="phone-ai-typing" aria-hidden="true">
                  <span />
                  <span />
                  <span />
                </div>
              </div>
            </div>
          </div>
          <div className="speed-visual-glow" />
        </div>
      </div>
    </div>
  </section>
);

export default HomeSpeedBanner;
