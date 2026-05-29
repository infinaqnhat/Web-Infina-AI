// NEW component — mirrors work.html L1775–1885 <section class="section context-ai-section" style="display:none">

/**
 * Hidden context-aware AI section — chat mockup + feature list.
 * Mirrors <section class="section context-ai-section" style="display:none"> in work.html L1775–1885.
 *
 * Layout: .context-grid (2-col) — left: .context-visual (chat window + metric card),
 * right: .context-content (badge + h2 + description + feature checklist).
 */
const WorkContextAISection = () => {
  return (
    <section className="section context-ai-section">
      <div className="container">
        <div className="context-grid reveal">

          {/* LEFT: visual — chat window + metric card — work.html L1778–1836 */}
          <div className="context-visual">
            <div className="context-chat-window">
              <div className="context-chat-header">
                <div className="context-dots">
                  <span style={{ background: "#ff5f57" }} />
                  <span style={{ background: "#ffbd2e" }} />
                  <span style={{ background: "#28ca42" }} />
                </div>
              </div>
              <div className="context-chat-body">
                {/* User message — work.html L1788–1798 */}
                <div className="context-msg context-msg-user">
                  <div className="context-avatar context-avatar-user">
                    <svg
                      width="16"
                      height="16"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="white"
                      strokeWidth="2"
                    >
                      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                      <circle cx="12" cy="7" r="4" />
                    </svg>
                  </div>
                  <div className="context-bubble context-bubble-user">
                    What are my top priorities for this week?
                  </div>
                </div>

                {/* AI message — work.html L1800–1821 */}
                <div className="context-msg context-msg-ai">
                  <div className="context-avatar context-avatar-ai">
                    <svg
                      width="16"
                      height="16"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="white"
                      strokeWidth="2.5"
                    >
                      <path d="M13 2L3 14h8l-1 8 10-12h-8l1-8z" />
                    </svg>
                  </div>
                  <div className="context-bubble context-bubble-ai">
                    <div style={{ marginBottom: 12, fontWeight: 600 }}>
                      Here are your top 3 Strategic High Priorities:
                    </div>
                    <div className="context-priority-item">
                      <div
                        className="context-priority-dot"
                        style={{ background: "#ef4444" }}
                      />
                      <div
                        className="context-priority-bar"
                        style={{
                          width: "85%",
                          background: "linear-gradient(90deg, #ef4444, #fca5a5)",
                        }}
                      />
                    </div>
                    <div className="context-priority-item">
                      <div
                        className="context-priority-dot"
                        style={{ background: "#f59e0b" }}
                      />
                      <div
                        className="context-priority-bar"
                        style={{
                          width: "68%",
                          background: "linear-gradient(90deg, #f59e0b, #fcd34d)",
                        }}
                      />
                    </div>
                    <div className="context-priority-item">
                      <div
                        className="context-priority-dot"
                        style={{ background: "#3b82f6" }}
                      />
                      <div
                        className="context-priority-bar"
                        style={{
                          width: "45%",
                          background: "linear-gradient(90deg, #3b82f6, #93c5fd)",
                        }}
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Metric card — work.html L1825–1835 */}
            <div className="context-metric-card">
              <div className="context-metric-icon">
                <svg
                  width="16"
                  height="16"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#10b981"
                  strokeWidth="2"
                >
                  <polyline points="22 12 18 12 15 21 9 3 6 12 2 12" />
                </svg>
              </div>
              <div className="context-metric-content">
                <div className="context-metric-label">Efficiency</div>
                <div className="context-metric-value">Trending Up</div>
              </div>
            </div>
          </div>

          {/* RIGHT: content — work.html L1838–1882 */}
          <div className="context-content">
            <div className="context-badge">
              <svg
                width="16"
                height="16"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
              >
                <path d="M13 2L3 14h8l-1 8 10-12h-8l1-8z" />
              </svg>
              AI Intelligence
            </div>
            <h2>
              AI that understands{" "}
              <span className="context-highlight">your context</span>
            </h2>
            <p className="context-description">
              Our AI doesn't just answer questions—it understands your
              priorities, team structure, and progress to provide meaningful
              insights tailored to your organization.
            </p>

            <ul className="context-features">
              <li>
                <div className="context-check">
                  <svg
                    width="14"
                    height="14"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="3"
                  >
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                </div>
                <span>Context-aware AI that understands your priorities</span>
              </li>
              <li>
                <div className="context-check">
                  <svg
                    width="14"
                    height="14"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="3"
                  >
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                </div>
                <span>Role-based access for robust security</span>
              </li>
              <li>
                <div className="context-check">
                  <svg
                    width="14"
                    height="14"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="3"
                  >
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                </div>
                <span>Automated daily reporting &amp; blocker tracking</span>
              </li>
              <li>
                <div className="context-check">
                  <svg
                    width="14"
                    height="14"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="3"
                  >
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                </div>
                <span>Real-time team collaboration &amp; sync</span>
              </li>
            </ul>
          </div>

        </div>
      </div>
    </section>
  );
};

export default WorkContextAISection;
