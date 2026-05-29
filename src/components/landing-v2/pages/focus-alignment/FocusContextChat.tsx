import { useEffect, useRef, useState } from "react";
import {
  CHAT_SCENARIOS,
  PROMPT_BUTTONS,
  type ScenarioKey,
} from "./focus-context-chat-scenarios";

/**
 * FocusContextChat — "AI that understands your context" section.
 * Source-mirrored from Web-Infina-AI/focus-alignment.html context section + JS renderChat().
 *
 * DIVERGENCE FROM infina-pfa-80389:
 *   The "blockers" scenario here renders the full HTML response:
 *     aiIntro (strong-wrapped KR-355) + single task card + followup text + action buttons row.
 *   infina-pfa-80389 simplified blockers to a typing indicator only.
 *   This mirror restores the full HTML renderChat(key === 'blockers') branch.
 */

const AiAvatar = () => (
  <div className="chat-ai-avatar">
    <svg
      width="14"
      height="14"
      viewBox="0 0 24 24"
      fill="none"
      stroke="white"
      strokeWidth="2.5"
    >
      <path d="M13 2L3 14h8l-1 8 10-12h-8l1-8z" />
    </svg>
  </div>
);

const ChatBody = ({ scenarioKey }: { scenarioKey: ScenarioKey }) => {
  const s = CHAT_SCENARIOS[scenarioKey];

  return (
    <div className="chat-body" id="chat-body">
      {/* User message */}
      <div className="chat-msg-user">
        <div className="chat-bubble-user">{s.userMsg}</div>
      </div>

      {/* AI response — typing indicator (infina-pfa-80389 simplification, not used in mirror) */}
      {s.typing && (
        <div className="chat-msg-ai">
          <AiAvatar />
          <div className="chat-typing">
            <span />
            <span />
            <span />
          </div>
        </div>
      )}

      {/* AI response — blockers: single task card + followup + action buttons */}
      {s.actions && s.task && (
        <div className="chat-msg-ai">
          <AiAvatar />
          <div className="chat-bubble-ai">
            <div style={{ fontSize: 13, color: "var(--fg)", marginBottom: 4 }}>
              {s.aiIntro}
            </div>
            {/* Single task card (blockers scenario) */}
            <div
              className="chat-task-card"
              style={{ marginTop: 10, marginBottom: 10 }}
            >
              <div style={{ display: "flex", alignItems: "center", gap: 8, flex: 1 }}>
                <svg
                  width="14"
                  height="14"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="var(--blue)"
                  strokeWidth="2"
                >
                  <rect x="3" y="3" width="7" height="7" />
                  <rect x="14" y="3" width="7" height="7" />
                  <rect x="14" y="14" width="7" height="7" />
                  <rect x="3" y="14" width="7" height="7" />
                </svg>
                <span className="chat-task-card-id">{s.task.id}</span>
                <span style={{ fontSize: 12, fontWeight: 600, color: "var(--fg)" }}>
                  {s.task.name}
                </span>
              </div>
              <span className="chat-task-card-tag hero-tag-queue">{s.task.tag}</span>
            </div>
            <div
              style={{
                fontSize: 13,
                color: "var(--muted)",
                marginBottom: 12,
              }}
            >
              {s.followup}
            </div>
            <div className="chat-action-row">
              {s.actions.map((label, i) => (
                <button
                  key={label}
                  className={`chat-action-btn${i === 0 ? " primary" : ""}`}
                >
                  {label}
                </button>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* AI response — tasks list (priorities scenario) */}
      {s.tasks && (
        <div className="chat-msg-ai">
          <AiAvatar />
          <div className="chat-bubble-ai">
            <div style={{ fontWeight: 700, marginBottom: 10, fontSize: 13 }}>
              Infina AI
            </div>
            <div style={{ fontSize: 13, color: "var(--muted)", marginBottom: 12 }}>
              {s.aiIntro}
            </div>
            {s.tasks.map((t) => (
              <div
                key={t.id}
                style={{
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "space-between",
                  padding: "8px 10px",
                  borderRadius: 8,
                  border: "1px solid var(--border)",
                  marginBottom: 6,
                  fontSize: 12,
                }}
              >
                <span
                  style={{
                    fontSize: 11,
                    fontWeight: 700,
                    color: t.idColor,
                    minWidth: 50,
                  }}
                >
                  {t.id}
                </span>
                <span style={{ flex: 1, padding: "0 8px", color: "var(--fg)" }}>
                  {t.name}
                </span>
                <span className={`status-tag ${t.tagClass}`}>{t.tag}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* AI response — report/note scenario */}
      {s.note && (
        <div className="chat-msg-ai">
          <AiAvatar />
          <div className="chat-bubble-ai">
            <div style={{ fontWeight: 700, marginBottom: 8, fontSize: 13 }}>
              Infina AI
            </div>
            <div style={{ fontSize: 13, color: "var(--muted)", marginBottom: 12 }}>
              {s.aiIntro}
            </div>
            <div
              style={{
                background: "#f8f9ff",
                border: "1px solid rgba(24,99,220,.15)",
                borderRadius: 8,
                padding: "10px 12px",
                fontSize: 12,
                color: "var(--fg)",
                marginBottom: 10,
              }}
            >
              {s.note}
            </div>
            <div style={{ fontSize: 13, color: "var(--blue)", fontWeight: 600 }}>
              {s.followup}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

const FocusContextChat = () => {
  const [activeScenario, setActiveScenario] = useState<ScenarioKey>("priorities");
  const sectionRef = useRef<HTMLElement>(null);

  /* Reveal on scroll — mirrors HTML IntersectionObserver logic */
  useEffect(() => {
    const section = sectionRef.current;
    if (!section) return;
    const revealEls = section.querySelectorAll<HTMLElement>(".reveal");
    const observers: IntersectionObserver[] = [];
    revealEls.forEach((el) => {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("visible");
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.1 }
      );
      observer.observe(el);
      observers.push(observer);
    });
    return () => observers.forEach((o) => o.disconnect());
  }, []);

  return (
    <section className="section context-section" ref={sectionRef}>
      <div className="container">
        <div className="section-header reveal">
          <p className="section-label">AI Intelligence</p>
          <h2>
            AI that understands{" "}
            <span className="accent-blue-text">your context</span>
          </h2>
          <p>
            Our AI doesn't just answer questions — it understands your
            priorities, team structure, and progress to provide meaningful
            insights tailored to your organization.
          </p>
        </div>

        <div className="context-grid reveal">
          {/* Chat window */}
          <div className="chat-window">
            <div className="chat-titlebar">
              <div className="chat-dots">
                <span style={{ background: "#ff5f57" }} />
                <span style={{ background: "#ffbd2e" }} />
                <span style={{ background: "#28ca42" }} />
              </div>
              <span className="chat-title-text">infina1thing · AI Chat</span>
              <span className="chat-online">Online</span>
            </div>

            <ChatBody scenarioKey={activeScenario} />

            {/* Prompt tab bar — mirrors HTML #chat-prompts click handler */}
            <div
              className="chat-prompt-bar"
              id="chat-prompts"
              role="tablist"
              aria-label="Chat scenarios"
            >
              {PROMPT_BUTTONS.map(({ key, label }) => (
                <button
                  key={key}
                  role="tab"
                  aria-selected={activeScenario === key}
                  className={`chat-prompt-btn${activeScenario === key ? " active" : ""}`}
                  onClick={() => setActiveScenario(key)}
                >
                  {label}
                </button>
              ))}
            </div>
          </div>

          {/* Right: checklist + pro tip */}
          <div>
            <ul className="context-check-list">
              <li>
                <div className="check-icon">
                  <svg
                    width="13"
                    height="13"
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
                <div className="check-icon">
                  <svg
                    width="13"
                    height="13"
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
                <div className="check-icon">
                  <svg
                    width="13"
                    height="13"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="3"
                  >
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                </div>
                <span>Automated daily reporting and blocker tracking</span>
              </li>
              <li>
                <div className="check-icon">
                  <svg
                    width="13"
                    height="13"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="3"
                  >
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                </div>
                <span>Real-time team collaboration and sync</span>
              </li>
            </ul>
            <div className="pro-tip-box">
              <div className="pro-tip-label">
                <svg
                  width="14"
                  height="14"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2.5"
                >
                  <path d="M13 2L3 14h8l-1 8 10-12h-8l1-8z" />
                </svg>
                Pro Tip
              </div>
              <p>
                Click any sample prompt above to see how the AI responds with
                real context from your team's priorities, blockers, and reports.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default FocusContextChat;
