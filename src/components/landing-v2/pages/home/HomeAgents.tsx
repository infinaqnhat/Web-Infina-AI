import { useState } from "react";
import { Link } from "react-router-dom";
import {
  type TabKey,
  insideCards,
  personalRows,
  workAudiences,
} from "./home-agents-data";

/**
 * Agents tabbed section — mirrors home.html agents-section L4312–4543.
 * Tab state managed via React useState; keyboard-accessible via role="tab"
 * and aria-selected. Panel CSS (display:none / display:block + fade-up) is
 * handled by .agents-panel / .agents-panel.active in landing-home.css.
 *
 * DIFF FROM infina-pfa-80389: content matches HTML verbatim. The React
 * tabbed UI is canonical — the HTML also uses tabs (JS-driven), so no
 * structural divergence. Data parity verified against home.html L4332–4543.
 */

const TABS: { key: TabKey; label: string }[] = [
  { key: "inside", label: "Infina AI Inside" },
  { key: "work", label: "Infina AI Work" },
  { key: "personal", label: "Infina AI Personal" },
];

const HomeAgents = () => {
  const [activeTab, setActiveTab] = useState<TabKey>("inside");

  return (
    <section className="agents-section">
      <div className="container">
        <div className="section-header">
          <span className="section-eyebrow">Meet the Specialists</span>
          <h2>
            The right specialist,{" "}
            <span className="accent">exactly where you need them</span>
          </h2>
        </div>

        {/* Tab bar */}
        <div className="agents-tabs" role="tablist">
          {TABS.map((tab) => (
            <button
              key={tab.key}
              className={`agents-tab${activeTab === tab.key ? " active" : ""}`}
              data-tab={tab.key}
              role="tab"
              aria-selected={activeTab === tab.key}
              onClick={() => setActiveTab(tab.key)}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {/* ── Panel: AI Inside ── */}
        <div
          id="tab-inside"
          className={`agents-panel${activeTab === "inside" ? " active" : ""}`}
        >
          <p className="agents-panel-tagline">
            Live inside your platforms. Get the experts 24/7.
          </p>
          <div className="agents-grid agents-grid-4" id="inside-grid">
            {insideCards.map((card) => (
              <div
                key={card.agent}
                className="agents-card"
                data-agent={card.agent}
              >
                <div className="agents-card-left">
                  <h3 className="agents-card-title">
                    <span className="agents-title-main">{card.titleMain}</span>
                    <span className="agents-title-sub">{card.titleSub}</span>
                  </h3>
                  <div className="agents-context-badge">
                    {card.contextBadge}
                  </div>
                </div>
                <div className="agents-card-right">
                  <ul className="agents-list">
                    {card.bullets.map((b) => (
                      <li key={b}>{b}</li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* ── Panel: AI Personal ── */}
        <div
          id="tab-personal"
          className={`agents-panel${activeTab === "personal" ? " active" : ""}`}
        >
          <p className="agents-panel-tagline">
            A specialist for every life decision you face.
          </p>
          <div className="agents-personal-rows">
            {personalRows.map((row) => (
              <div
                key={row.titleMain}
                className={`agents-personal-row${row.muted ? " agents-personal-row--muted" : ""}`}
              >
                <h3 className="agents-card-title">
                  <span
                    className="agents-title-main"
                    style={row.muted ? { color: "var(--muted)" } : undefined}
                  >
                    {row.titleMain}
                  </span>
                  <span className="agents-title-sub">{row.titleSub}</span>
                </h3>
                {row.tags && (
                  <div className="agents-personal-tags">
                    {row.tags.map((tag) => (
                      <span key={tag}>{tag}</span>
                    ))}
                  </div>
                )}
                {row.ctaHref && (
                  <Link to={row.ctaHref} className="agents-personal-cta">
                    See it in action{" "}
                    <span className="agents-personal-cta-arrow">→</span>
                  </Link>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* ── Panel: AI Work ── */}
        <div
          id="tab-work"
          className={`agents-panel${activeTab === "work" ? " active" : ""}`}
        >
          <p className="agents-panel-tagline">
            Less chasing tasks. More closing them.
          </p>
          {workAudiences.map((audience) => (
            <div key={audience.label} className="agents-work-audience">
              <span className="agents-audience-label">{audience.label}</span>
              <div
                className={`agents-grid${audience.cards.length > 1 ? " agents-grid-4" : ""}`}
                id={audience.label === "For Sales Teams" ? undefined : "work-grid"}
              >
                {audience.cards.map((card) =>
                  card.wide ? (
                    <div
                      key={card.titleMain}
                      className="agents-card agents-card-row"
                    >
                      <div className="agents-card-row-meta">
                        <h3 className="agents-card-title">
                          <span className="agents-title-main">
                            {card.titleMain}
                          </span>
                          <span className="agents-title-sub">
                            {card.titleSub}
                          </span>
                        </h3>
                        <div className="agents-context-badge">
                          {card.contextBadge}
                        </div>
                      </div>
                      <ul className="agents-list agents-list-row">
                        {card.bullets.map((b) => (
                          <li key={b}>{b}</li>
                        ))}
                      </ul>
                    </div>
                  ) : (
                    <div key={card.titleMain} className="agents-card">
                      <div className="agents-card-left">
                        <h3 className="agents-card-title">
                          <span className="agents-title-main">
                            {card.titleMain}
                          </span>
                          <span className="agents-title-sub">
                            {card.titleSub}
                          </span>
                        </h3>
                        <div className="agents-context-badge">
                          {card.contextBadge}
                        </div>
                      </div>
                      <div className="agents-card-right">
                        <ul className="agents-list">
                          {card.bullets.map((b) => (
                            <li key={b}>{b}</li>
                          ))}
                        </ul>
                      </div>
                    </div>
                  )
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default HomeAgents;
