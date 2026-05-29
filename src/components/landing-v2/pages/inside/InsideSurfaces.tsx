import { useState } from "react";

// NEW component — mirrors inside.html L5851-6145 <section class="surfaces" id="surfaces" style="display:none">
// Tabbed UI: Mobile SDK / Web Embed / Admin Dashboard. Inline JS tab logic ported to useState.

type SurfaceTab = "mobile" | "web" | "admin";

const InsideSurfaces = () => {
  const [activeTab, setActiveTab] = useState<SurfaceTab>("mobile");

  return (
    <section className="surfaces" id="surfaces" style={{ display: "none" }}>
      <div className="container">
        <div className="surfaces-header">
          <span className="section-label">Flexible Deployment Options</span>
          <h2>Everywhere Your Product Appears</h2>
          <p>
            Choose the right integration platform, from Native SDK on mobile, quick Web Embed
            to internal Admin Dashboard.
          </p>
        </div>

        <div className="surface-tabs" role="tablist">
          <span className="surface-tab-indicator" aria-hidden="true" />
          <button
            className={`surface-tab${activeTab === "mobile" ? " is-active" : ""}`}
            data-tab="mobile"
            role="tab"
            aria-selected={activeTab === "mobile"}
            onClick={() => setActiveTab("mobile")}
          >
            <span className="surface-tab-num">01</span>
            Mobile SDK
          </button>
          <button
            className={`surface-tab${activeTab === "web" ? " is-active" : ""}`}
            data-tab="web"
            role="tab"
            aria-selected={activeTab === "web"}
            onClick={() => setActiveTab("web")}
          >
            <span className="surface-tab-num">02</span>
            Web Embed
          </button>
          <button
            className={`surface-tab${activeTab === "admin" ? " is-active" : ""}`}
            data-tab="admin"
            role="tab"
            aria-selected={activeTab === "admin"}
            onClick={() => setActiveTab("admin")}
          >
            Admin Dashboard
          </button>
        </div>

        <div className="surface-panel-wrap">

          {/* Panel 1: Mobile SDK */}
          <div
            className={`surface-panel${activeTab === "mobile" ? " is-active" : ""}`}
            data-panel="mobile"
          >
            <div className="surface-copy">
              <h3>
                <span className="accent">Seamless Native Integration.</span> Embed AI specialists
                directly into your iOS and Android apps with optimized Mobile SDK.
              </h3>
              <p>AI experience without forcing customers to leave your ecosystem.</p>
              <p><strong>Go-live in 2-3 weeks.</strong> We'll handle the complete setup for you.</p>
              <a href="#demo" className="surface-cta">Book a Demo</a>
            </div>
            <div className="surface-visual">
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
                      <svg viewBox="0 0 20 12" fill="none" stroke="currentColor" strokeWidth="1.5">
                        <rect x="1" y="2" width="16" height="8" rx="2" />
                        <rect x="18" y="5" width="1.5" height="2" />
                        <rect x="2.5" y="3.5" width="11" height="5" rx="1" fill="currentColor" stroke="none" />
                      </svg>
                    </span>
                  </div>
                  <div className="phone-header">
                    <div className="phone-avatar">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round">
                        <circle cx="12" cy="9" r="3.2" />
                        <path d="M5 20c1-3.5 4-5.5 7-5.5s6 2 7 5.5" />
                      </svg>
                    </div>
                    <div className="phone-greeting">
                      <small>Hello,</small>
                      <strong>Minh Anh!</strong>
                    </div>
                    <button className="phone-icon-btn" aria-label="settings">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round">
                        <circle cx="12" cy="12" r="3" />
                        <path d="M12 2v3M12 19v3M22 12h-3M5 12H2M19 5l-2 2M7 17l-2 2M19 19l-2-2M7 7L5 5" />
                      </svg>
                    </button>
                  </div>

                  <div className="phone-balance">
                    <div className="phone-balance-row">
                      <span className="phone-balance-label">Available Balance</span>
                      <span className="phone-balance-trend">
                        <svg viewBox="0 0 12 12" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
                          <polyline points="2 9 5 6 7 8 10 4" />
                        </svg>
                        +12.4%
                      </span>
                    </div>
                    <div className="phone-balance-value">$150,000</div>
                    <div className="phone-balance-actions">
                      <div className="phone-action"><span>↗</span>Deposit</div>
                      <div className="phone-action"><span>↙</span>Withdraw</div>
                      <div className="phone-action"><span>⇄</span>Transfer</div>
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
                          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                            <path d="M22 10v6M2 10l10-5 10 5-10 5z" />
                            <path d="M6 12v5c3 3 9 3 12 0v-5" />
                          </svg>
                        </span>
                        <div className="phone-goal-info">
                          <small>Goal • 62%</small>
                          <strong>Education Fund</strong>
                        </div>
                        <span className="phone-goal-badge">
                          <svg viewBox="0 0 12 12" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <polyline points="2 8 5 5 7 7 10 4" />
                          </svg>
                          +18%
                        </span>
                      </div>
                      <div className="phone-progress">
                        <div className="phone-progress-bar" />
                      </div>
                      <div className="phone-goal-stats">
                        <div className="phone-stat">
                          <small>Growth</small>
                          <strong className="phone-stat-up">+32%</strong>
                        </div>
                        <div className="phone-stat-divider" />
                        <div className="phone-stat">
                          <small>Remaining</small>
                          <strong>8 months</strong>
                        </div>
                      </div>
                    </div>

                    <p className="phone-ai-msg">
                      Open a dedicated savings fund to accelerate reaching your goal sooner?
                    </p>

                    <div className="phone-ai-actions">
                      <button className="phone-btn-primary">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                          <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" />
                        </svg>
                        Chat with AI
                      </button>
                    </div>
                    <div className="phone-ai-typing" aria-hidden="true">
                      <span /><span /><span />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Panel 2: Web Embed */}
          <div
            className={`surface-panel${activeTab === "web" ? " is-active" : ""}`}
            data-panel="web"
          >
            <div className="surface-copy">
              <h3>
                <span className="accent">Full White-label.</span> AI specialists seamlessly
                integrated with your product branding, for your experience and customers.
              </h3>
              <p>UI Components easily customizable to perfectly match your Design System.</p>
              <p><strong>Quick integration with just 1 line of script.</strong></p>
              <a href="#demo" className="surface-cta">Book a Demo</a>
            </div>
            <div className="surface-visual">
              <div className="mock-browser">
                <div className="mock-browser-bar">
                  <div className="mock-browser-dots"><span /><span /><span /></div>
                  <div className="mock-browser-url">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="10" height="10">
                      <circle cx="11" cy="11" r="7" />
                      <path d="M21 21l-4.3-4.3" />
                    </svg>
                    safeguard-insurance.com
                  </div>
                </div>
                <div className="mock-browser-body">
                  <div className="mock-skel-row">
                    <div className="mock-skel-logo">S</div>
                    <span className="mock-skel-brand">SafeGuard</span>
                    <div className="mock-skel-line short" />
                    <div className="mock-skel-line short" />
                    <div className="mock-skel-line short" />
                  </div>
                  <div className="mock-skel-block tall w70" />
                  <div className="mock-skel-pillrow">
                    <div className="mock-skel-pill w60" />
                    <div className="mock-skel-pill w40" />
                  </div>
                  <div className="mock-skel-block w90" />
                  <div className="mock-skel-block w50" />
                  <div className="mock-skel-block w80" />
                  <div className="mock-skel-block w70" />

                  <div className="mock-chat">
                    <div className="mock-chat-head">
                      <strong>AI Advisor</strong>
                      <small>POWERED BY INFINA</small>
                    </div>
                    <div className="mock-chat-body">
                      <div className="mock-chat-msg user">
                        My family has 4 members, which health insurance plan should I choose?
                      </div>
                      <div className="mock-chat-msg ai">
                        Based on your family size, the 'Dual Protection' plan offers comprehensive
                        benefits and 15% discount for the 3rd member onwards.
                      </div>
                    </div>
                    <div className="mock-chat-input">
                      <span>Type a message…</span>
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <line x1="22" y1="2" x2="11" y2="13" />
                        <polygon points="22 2 15 22 11 13 2 9 22 2" />
                      </svg>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Panel 3: Admin Dashboard */}
          <div
            className={`surface-panel${activeTab === "admin" ? " is-active" : ""}`}
            data-panel="admin"
          >
            <div className="surface-copy">
              <h3>
                <span className="accent">Flexible Management &amp; Control.</span> Visual Knowledge
                Base management, with built-in reporting and in-depth analytics.
              </h3>
              <p>
                Partner Dashboard provides complete data overview: usage levels, engagement rates
                and full compliance logs.
              </p>
              <p>
                Capture critical insights to continuously train language and refine AI advisory
                flows.
              </p>
              <a href="#demo" className="surface-cta">Book a Demo</a>
            </div>
            <div className="surface-visual">
              <div className="mock-admin">
                <div className="mock-admin-side">
                  <div className="mock-admin-brand">Admin</div>
                  <div className="mock-admin-nav-item is-active">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <rect x="2" y="3" width="20" height="14" rx="2" />
                      <path d="M8 21h8M12 17v4" />
                    </svg>
                    Analytics
                  </div>
                  <div className="mock-admin-nav-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                      <circle cx="12" cy="7" r="4" />
                    </svg>
                    Customers
                  </div>
                  <div className="mock-admin-nav-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                    </svg>
                    Conversations
                  </div>
                  <div className="mock-admin-nav-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M4 4h12a4 4 0 0 1 4 4v12H8a4 4 0 0 1-4-4z" />
                    </svg>
                    Knowledge Base
                  </div>
                  <div className="mock-admin-nav-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
                    </svg>
                    Plans
                  </div>
                  <div className="mock-admin-nav-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <ellipse cx="12" cy="5" rx="9" ry="3" />
                      <path d="M3 5v14c0 1.7 4 3 9 3s9-1.3 9-3V5" />
                      <path d="M3 12c0 1.7 4 3 9 3s9-1.3 9-3" />
                    </svg>
                    Datasets
                  </div>
                </div>
                <div className="mock-admin-body">
                  <div className="mock-admin-topbar">
                    <span className="mock-admin-title">Analytics</span>
                    <span className="mock-admin-user">H</span>
                  </div>
                  <div className="mock-admin-metrics">
                    <div className="mock-metric">
                      <div className="mock-metric-label">USERS</div>
                      <div className="mock-metric-main">8,450 / 10,000</div>
                      <div className="mock-metric-pct">84.5%</div>
                    </div>
                    <div className="mock-metric">
                      <div className="mock-metric-label">AI CHAT MESSAGES</div>
                      <div className="mock-metric-main">142,890 / 200,000</div>
                      <div className="mock-metric-pct">71.4%</div>
                    </div>
                  </div>
                  <div className="mock-admin-section-title">ACTIVITY</div>
                  <div className="mock-admin-activity-grid">
                    <div className="mock-activity-card">
                      <div className="mock-activity-label">TOTAL USERS</div>
                      <div className="mock-activity-val">8,450</div>
                      <div className="mock-activity-change" style={{ opacity: 0 }}>placeholder</div>
                    </div>
                    <div className="mock-activity-card">
                      <div className="mock-activity-label">DAU</div>
                      <div className="mock-activity-val">2,340</div>
                      <div className="mock-activity-change up">vs last week</div>
                    </div>
                    <div className="mock-activity-card">
                      <div className="mock-activity-label">WAU</div>
                      <div className="mock-activity-val">5,120</div>
                      <div className="mock-activity-change up">vs last week</div>
                    </div>
                    <div className="mock-activity-card">
                      <div className="mock-activity-label">MAU</div>
                      <div className="mock-activity-val">7,890</div>
                      <div className="mock-activity-change up">vs last week</div>
                    </div>
                    <div className="mock-activity-card">
                      <div className="mock-activity-label">NEW USERS</div>
                      <div className="mock-activity-val">1,240</div>
                      <div className="mock-activity-change up">vs last week</div>
                    </div>
                  </div>
                  <div className="mock-admin-chart-header">
                    <div className="mock-admin-section-title">DAU TREND</div>
                    <div className="mock-time-pills">
                      <span className="active">7d</span>
                      <span>30d</span>
                      <span>90d</span>
                    </div>
                  </div>
                  <div className="mock-admin-chart">
                    <svg width="100%" height="70" viewBox="0 0 260 70" preserveAspectRatio="none">
                      <rect x="10" y="55" width="18" height="15" fill="#10b981" opacity="0.3" rx="2" />
                      <rect x="40" y="50" width="18" height="20" fill="#10b981" opacity="0.3" rx="2" />
                      <rect x="70" y="52" width="18" height="18" fill="#10b981" opacity="0.3" rx="2" />
                      <rect x="100" y="48" width="18" height="22" fill="#10b981" opacity="0.3" rx="2" />
                      <rect x="130" y="45" width="18" height="25" fill="#10b981" opacity="0.3" rx="2" />
                      <rect x="160" y="40" width="18" height="30" fill="#10b981" opacity="0.4" rx="2" />
                      <rect x="190" y="35" width="18" height="35" fill="#10b981" opacity="0.5" rx="2" />
                      <rect x="220" y="8" width="18" height="62" fill="#10b981" opacity="0.7" rx="2" />
                    </svg>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
};

export default InsideSurfaces;
