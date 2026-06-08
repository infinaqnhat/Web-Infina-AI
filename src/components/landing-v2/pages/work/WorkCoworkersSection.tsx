import { useState, useEffect, useRef } from "react";
import { SCENARIOS, FEATURE_TABS } from "./work-coworkers-data";

/**
 * AI Coworkers section — centered header + Slack/WhatsApp CTAs + sticky mockup.
 * Mirrors <section class="section coworkers-section"> in Web-Infina-AI/work.html L981–1189.
 *
 * Layout:
 *  - coworkers-header: centered, no badges/eyebrow
 *  - .coworkers-ctas: btn-slack + btn-whatsapp
 *  - coworkers-grid: 280px/1fr
 *  - .cw-panels-wrap: position:sticky top:100px (via CSS)
 *  - left column: .feature-pills (selector buttons) + .feature-display (active feature card)
 *
 * React state model: activeIdx drives which panel/tab is active.
 * IntersectionObserver adds "visible" class to .reveal elements on scroll.
 */

/** Official Slack logo mark (SVG paths from slack.com brand assets) */
const SlackIcon = () => (
  <svg
    width="18"
    height="18"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 122.8 122.8"
    aria-hidden="true"
  >
    <path
      d="M25.8 77.6c0 7.1-5.8 12.9-12.9 12.9S0 84.7 0 77.6s5.8-12.9 12.9-12.9h12.9v12.9zm6.5 0c0-7.1 5.8-12.9 12.9-12.9s12.9 5.8 12.9 12.9v32.3c0 7.1-5.8 12.9-12.9 12.9s-12.9-5.8-12.9-12.9V77.6z"
      fill="#e01e5a"
    />
    <path
      d="M45.2 25.8c-7.1 0-12.9-5.8-12.9-12.9S38.1 0 45.2 0s12.9 5.8 12.9 12.9v12.9H45.2zm0 6.5c7.1 0 12.9 5.8 12.9 12.9s-5.8 12.9-12.9 12.9H12.9C5.8 58.1 0 52.3 0 45.2s5.8-12.9 12.9-12.9h32.3z"
      fill="#36c5f0"
    />
    <path
      d="M97 45.2c0-7.1 5.8-12.9 12.9-12.9s12.9 5.8 12.9 12.9-5.8 12.9-12.9 12.9H97V45.2zm-6.5 0c0 7.1-5.8 12.9-12.9 12.9s-12.9-5.8-12.9-12.9V12.9C64.7 5.8 70.5 0 77.6 0s12.9 5.8 12.9 12.9v32.3z"
      fill="#2eb67d"
    />
    <path
      d="M77.6 97c7.1 0 12.9 5.8 12.9 12.9s-5.8 12.9-12.9 12.9-12.9-5.8-12.9-12.9V97h12.9zm0-6.5c-7.1 0-12.9-5.8-12.9-12.9s5.8-12.9 12.9-12.9h32.3c7.1 0 12.9 5.8 12.9 12.9s-5.8 12.9-12.9 12.9H77.6z"
      fill="#ecb22e"
    />
  </svg>
);

/** WhatsApp logo mark */
const WhatsAppIcon = () => (
  <svg
    width="18"
    height="18"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24"
    fill="#fff"
    aria-hidden="true"
  >
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 00-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z" />
  </svg>
);

const WorkCoworkersSection = () => {
  const [activeIdx, setActiveIdx] = useState(0);
  const sectionRef = useRef<HTMLElement>(null);

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

  const scenario = SCENARIOS[activeIdx];

  return (
    <section className="section coworkers-section" ref={sectionRef}>
      <div className="container">

        {/* Centered header — no badges/eyebrow */}
        <div className="coworkers-header reveal">
          <h2>
            Works inside your setup.{" "}
            <span className="gradient-text">Acts the moment you ask.</span>
          </h2>
          <div className="coworkers-ctas">
            <button className="btn-slack" type="button">
              <SlackIcon />
              Add to Slack
            </button>
            <button className="btn-whatsapp" type="button">
              <WhatsAppIcon />
              Add to WhatsApp
            </button>
          </div>
        </div>

        {/* 2-col grid: tabs left, sticky mockup right */}
        <div className="coworkers-grid reveal">
          {/* Feature selector pills + display card (left column) */}
          <div className="coworkers-features">
            <div className="feature-pills">
              {FEATURE_TABS.map((feat, i) => (
                <button
                  key={feat.title}
                  type="button"
                  className={`feature-pill${activeIdx === i ? " feature-pill-active" : ""}`}
                  data-tab={i}
                  onClick={() => setActiveIdx(i)}
                >
                  {feat.title}
                </button>
              ))}
            </div>
            <div className="feature-display">
              <div className="feature-display-icon">
                {FEATURE_TABS[activeIdx].icon}
              </div>
              <h4>{FEATURE_TABS[activeIdx].title}</h4>
              <p>{FEATURE_TABS[activeIdx].desc}</p>
            </div>
          </div>

          {/* Sticky mockup wrap (right column) — driven by activeIdx state */}
          <div className="cw-panels-wrap">
            <div className="slack-mockup">
              <div className="slack-window">
                <div className="slack-header">
                  <span className="slack-channel"># {scenario.channel}</span>
                  <span className="slack-time">{scenario.time}</span>
                </div>
                <div className="slack-messages">
                  {/* User message */}
                  <div className="slack-message">
                    <div
                      className="slack-avatar"
                      style={{ background: scenario.userColor }}
                    >
                      {scenario.userInitials}
                    </div>
                    <div className="slack-msg-content">
                      <div className="slack-msg-header">
                        <span className="slack-username">{scenario.user}</span>
                        <span className="slack-timestamp">{scenario.time}</span>
                      </div>
                      <div className="slack-msg-text">{scenario.userMessage}</div>
                    </div>
                  </div>

                  {/* Bot message */}
                  <div className="slack-message slack-bot">
                    <div className="slack-avatar slack-bot-avatar">
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
                    <div className="slack-msg-content">
                      <div className="slack-msg-header">
                        <span className="slack-username">{scenario.botName}</span>
                        <span className="slack-app-badge">APP</span>
                        <span className="slack-timestamp">{scenario.time}</span>
                      </div>
                      <div className="slack-msg-text">{scenario.botResponse}</div>

                      {/* Card: table items */}
                      {scenario.cardItems && (
                        <div className="slack-card">
                          <div className="slack-card-label">{scenario.cardLabel}</div>
                          {scenario.cardItems.map((item) => (
                            <div
                              key={item.label}
                              style={{
                                display: "flex",
                                justifyContent: "space-between",
                                marginBottom: 8,
                                fontSize: 13,
                              }}
                            >
                              <span style={{ color: "rgba(255,255,255,.6)" }}>
                                {item.label}
                              </span>
                              <span
                                style={{
                                  color: item.highlight ? "#f59e0b" : "#fff",
                                  fontWeight: 600,
                                }}
                              >
                                {item.value}
                              </span>
                            </div>
                          ))}
                          <div className="slack-card-actions" style={{ marginTop: 16 }}>
                            <button className="slack-btn-primary">
                              {scenario.buttons[0]}
                            </button>
                            <button className="slack-btn-ghost">
                              {scenario.buttons[1]}
                            </button>
                          </div>
                        </div>
                      )}

                      {/* Card: warning */}
                      {scenario.cardWarning && (
                        <div className="slack-card">
                          <div className="slack-card-label">{scenario.cardLabel}</div>
                          <div className="slack-card-item">
                            <div className="slack-warning-bar" />
                            <div>
                              <div className="slack-card-title">{scenario.cardTitle}</div>
                              <div className="slack-card-desc">{scenario.cardDesc}</div>
                            </div>
                          </div>
                          <div className="slack-card-actions">
                            <button className="slack-btn-primary">
                              {scenario.buttons[0]}
                            </button>
                            <button className="slack-btn-ghost">
                              {scenario.buttons[1]}
                            </button>
                          </div>
                        </div>
                      )}

                      {/* Card: checklist */}
                      {scenario.cardChecks && (
                        <div className="slack-card">
                          <div className="slack-card-label">{scenario.cardLabel}</div>
                          {scenario.cardChecks.map((check) => (
                            <div
                              key={check.text}
                              style={{
                                display: "flex",
                                alignItems: "center",
                                gap: 10,
                                marginBottom: 10,
                              }}
                            >
                              <span
                                style={{
                                  color: check.warning ? "#f59e0b" : "#22c55e",
                                  fontSize: 16,
                                }}
                              >
                                {check.done ? "✓" : "⚠"}
                              </span>
                              <span
                                style={{
                                  fontSize: 13,
                                  color: check.warning
                                    ? "#f59e0b"
                                    : "rgba(255,255,255,.8)",
                                }}
                              >
                                {check.text}
                              </span>
                            </div>
                          ))}
                          <div className="slack-card-actions" style={{ marginTop: 16 }}>
                            <button className="slack-btn-primary">
                              {scenario.buttons[0]}
                            </button>
                            <button className="slack-btn-ghost">
                              {scenario.buttons[1]}
                            </button>
                          </div>
                        </div>
                      )}
                    </div>
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

export default WorkCoworkersSection;
