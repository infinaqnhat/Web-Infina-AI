/**
 * FocusHero — hero section for /focus-alignment.
 * Ported verbatim from Web-Infina-AI/focus-alignment.html hero section.
 * 2-col layout: left text + CTA, right = hero-panels (AI Chat + Priorities) + floating teammates card.
 */

const FocusHero = () => (
  <section className="hero">
    <div className="hero-bg" />
    <div className="hero-grid-bg" />
    <div className="fa-shape fa-shape-1" />
    <div className="fa-shape fa-shape-2" />
    <div className="fa-shape fa-shape-3" />
    <div className="fa-shape fa-shape-4" />
    <div className="container">
      <div className="hero-grid">
        {/* Left: text + CTA */}
        <div className="hero-text">
          <h1>
            The{" "}
            <span className="accent-blue">
              AI chief
              <br />
              of staff
            </span>{" "}
            for
            <br />
            teams under 50.
          </h1>
          <p className="hero-sub">
            Stop retyping the same status update across Slack, Asana, and your
            OKR spreadsheet. Infina 1Thing connects your priorities, key
            results, and daily reports — in one AI chat. So your team does the
            right work, every single day.
          </p>
          <div className="hero-ctas">
            <a href="#demo" className="btn-primary-blue">
              Start chatting →
            </a>
          </div>
        </div>

        {/* Right: visual mockup */}
        <div className="hero-visual">
          <div className="hero-panels">
            {/* AI Chat panel */}
            <div className="hero-panel">
              <div className="hero-panel-header">
                <div className="hero-panel-title">
                  <div
                    style={{
                      width: 28,
                      height: 28,
                      borderRadius: 8,
                      background: "var(--blue)",
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                    }}
                  >
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="white">
                      <path d="M12 2l2.09 6.26L20 10l-5.91 1.74L12 18l-2.09-6.26L4 10l5.91-1.74z" />
                      <path
                        d="M19 14l.9 2.6 2.6.9-2.6.9L19 21l-.9-2.6-2.6-.9 2.6-.9z"
                        opacity=".7"
                      />
                    </svg>
                  </div>
                  AI Chat
                </div>
                <span
                  style={{
                    fontSize: 11,
                    color: "#22c55e",
                    fontWeight: 600,
                    display: "flex",
                    alignItems: "center",
                    gap: 4,
                  }}
                >
                  <span
                    style={{
                      width: 6,
                      height: 6,
                      borderRadius: "50%",
                      background: "#22c55e",
                      display: "inline-block",
                    }}
                  />
                  Live · Synced
                </span>
              </div>
              <div className="hero-panel-body">
                <div style={{ display: "flex", justifyContent: "flex-end", marginBottom: 14 }}>
                  <div className="hero-chat-bubble">Any blockers on KR-355?</div>
                </div>
                <div
                  style={{
                    fontSize: 13,
                    color: "var(--muted)",
                    lineHeight: 1.6,
                    marginBottom: 4,
                  }}
                >
                  <strong style={{ color: "var(--fg)" }}>KR-355</strong> is in
                  Queue. Last update: 1st draft sent to James. Noah is working
                  with James on revisions.
                </div>
                <div className="hero-task-card">
                  <div className="hero-task-card-id">KR-355</div>
                  <div className="hero-task-card-name">Infina AI logo redesign</div>
                  <div className="hero-task-card-footer">
                    <span className="hero-tag hero-tag-queue">Queue</span>
                  </div>
                </div>
                <div style={{ fontSize: 13, color: "var(--muted)", lineHeight: 1.55 }}>
                  No blocker logged — want me to ask Nathan for a status check?
                </div>
              </div>
              <div className="hero-input-bar">
                <span className="hero-input-placeholder">
                  Ask anything about your team's work...
                </span>
                <div className="hero-send-btn">
                  <svg
                    width="14"
                    height="14"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="white"
                    strokeWidth="2.5"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <line x1="22" y1="2" x2="11" y2="13" />
                    <polygon points="22 2 15 22 11 13 2 9 22 2" />
                  </svg>
                </div>
              </div>
            </div>

            {/* Priorities panel */}
            <div className="prio-panel">
              <div className="prio-panel-header">
                <div className="prio-panel-title">
                  <svg
                    width="16"
                    height="16"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                  >
                    <circle cx="12" cy="12" r="10" />
                    <path d="M12 6v6l4 2" />
                  </svg>
                  Priorities · Q2
                </div>
              </div>
              <div className="prio-panel-body">
                <div className="prio-section-label">
                  FOCUS <span className="prio-count">2</span>
                </div>
                <div className="prio-card">
                  <div className="prio-item-id">KR-358</div>
                  <div className="prio-item-name">Infina AI Landing Page</div>
                  <div className="prio-bar prio-bar-blue" />
                </div>
                <div className="prio-card">
                  <div className="prio-item-id" style={{ color: "#1863dc" }}>
                    SHP-568
                  </div>
                  <div className="prio-item-name">
                    Website merge — MKT &amp; Product
                  </div>
                  <div className="prio-bar prio-bar-purple" />
                </div>
                <div className="prio-section-label">
                  QUEUE <span className="prio-count">1</span>
                </div>
                <div className="prio-queue-card">
                  <div className="prio-item-id">KR-355</div>
                  <div
                    className="prio-item-name"
                    style={{ marginBottom: 8 }}
                  >
                    Infina AI logo redesign
                  </div>
                  <div
                    style={{
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "space-between",
                    }}
                  >
                    <span className="hero-tag hero-tag-review">In review</span>
                    <span style={{ fontSize: 11, color: "var(--muted)" }}>
                      James
                    </span>
                  </div>
                </div>
                <div className="prio-section-label">
                  DONE <span className="prio-count">8</span>
                </div>
              </div>
            </div>
          </div>

          {/* Floating teammates card */}
          <div className="hero-floating-card">
            <div className="teammate-avatars">
              <div className="teammate-avatar" style={{ background: "#1863dc" }}>
                NQ
              </div>
              <div className="teammate-avatar" style={{ background: "#1863dc" }}>
                GA
              </div>
              <div className="teammate-avatar" style={{ background: "#06b6d4" }}>
                TN
              </div>
              <div className="teammate-avatar" style={{ background: "#f59e0b" }}>
                JM
              </div>
              <div className="teammate-avatar" style={{ background: "#ef4444" }}>
                EK
              </div>
              <div className="teammate-overflow">+12</div>
            </div>
            <span className="teammate-text">
              17 teammates
              <br />
              aligned today
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>
);

export default FocusHero;
