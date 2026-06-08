import { useState, useEffect, useRef } from "react";
import { AGENT_GROUPS } from "./work-agents-data";

/**
 * Specialist Agents section — sticky-left 2-column grid.
 * Mirrors <section class="agents-section"> in Web-Infina-AI/work.html L1519–1634.
 *
 * Divergences from infina-pfa-80389 reference:
 *  - "1 thing" prefix in titleMain rendered with muted inline color (hasMutedPrefix flag)
 *  - crm-video-wrap: collapsible video toggle after "For Sales Teams" cards (showCrmVideo flag)
 *  - exploreLink uses plain <a href> (HTML-relative "focus-alignment.html"), not React Router <Link>
 *  - agents-grid-tabs "For Operations" has id="aw-work-grid" on the container
 *
 * NOTE: This is the VISIBLE agents section (class="agents-section", no display:none).
 * The hidden agents section (id="agents", display:none) is WorkAgentsHidden.
 */
// YouTube embed loaded lazily — src is only set once the panel opens so the
// iframe doesn't fetch the video on initial page load.
const CRM_VIDEO_SRC = "https://www.youtube-nocookie.com/embed/z3EU2NE_gEU?rel=0";

const WorkAgentsSection = () => {
  const sectionRef = useRef<HTMLElement>(null);
  // crm video toggle state: tracks open/closed for the collapsible panel
  const [crmVideoOpen, setCrmVideoOpen] = useState(false);

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

  /**
   * Render titleMain with optional muted "1 thing" prefix.
   * HTML L1570: <span style="color:var(--fg-secondary);font-weight:500;">1 thing</span> | Focus & Alignment
   */
  const renderTitleMain = (titleMain: string, hasMutedPrefix?: boolean) => {
    if (!hasMutedPrefix) return <>{titleMain}</>;
    // Split at " | " to isolate the prefix
    const pipeIdx = titleMain.indexOf(" | ");
    if (pipeIdx === -1) return <>{titleMain}</>;
    const prefix = titleMain.slice(0, pipeIdx);
    const rest = titleMain.slice(pipeIdx); // includes " | "
    return (
      <>
        <span style={{ color: "var(--fg-secondary)", fontWeight: 500 }}>{prefix}</span>
        {rest}
      </>
    );
  };

  return (
    <section className="agents-section" ref={sectionRef}>
      <div className="container">
        <div className="specialists-grid">

          {/* LEFT: sticky label + heading + sub — work.html L1523–1528 */}
          <div className="specialists-left">
            <span className="section-eyebrow">Meet the Specialists</span>
            <h2>
              AI Specialists for{" "}
              <span className="accent">Every Company Function</span>
            </h2>
            <p>Less chasing tasks. More closing them.</p>
          </div>

          {/* RIGHT: scrollable grouped cards */}
          <div className="specialists-right">
            {AGENT_GROUPS.map((group, groupIdx) => (
              <div key={group.audienceLabel} className="agents-work-audience-t">
                <span className="agents-audience-label-t">{group.audienceLabel}</span>
                <div
                  className={`agents-grid-tabs${group.gridFour ? " agents-grid-4" : ""}`}
                  {...(groupIdx === 1 ? { id: "aw-work-grid" } : {})}
                >
                  {group.cards.map((card) => (
                    <div
                      key={card.titleMain}
                      className={`agents-card-t${card.isRow ? " agents-card-row-t" : ""}`}
                    >
                      {card.isRow ? (
                        /* Row layout: meta left, bullets right — work.html L1536–1549 */
                        <>
                          <div className="agents-card-row-meta-t">
                            <h3 className="agents-card-title-t">
                              <span className="agents-title-main-t">
                                {renderTitleMain(card.titleMain, card.hasMutedPrefix)}
                              </span>
                              <span className="agents-title-sub-t">{card.titleSub}</span>
                            </h3>
                            <div className="agents-context-badge-t">{card.contextBadge}</div>
                          </div>
                          <ul className="agents-list-t agents-list-row-t">
                            {card.bullets.map((b) => (
                              <li key={b.text}>{b.text}</li>
                            ))}
                          </ul>
                        </>
                      ) : (
                        /* Column layout — work.html L1567–1627 */
                        <>
                          <div className="agents-card-left-t">
                            <h3 className="agents-card-title-t">
                              <span className="agents-title-main-t">
                                {renderTitleMain(card.titleMain, card.hasMutedPrefix)}
                              </span>
                              <span className="agents-title-sub-t">{card.titleSub}</span>
                            </h3>
                            <div className="agents-context-badge-t">{card.contextBadge}</div>
                          </div>
                          <div className="agents-card-right-t">
                            <ul className="agents-list-t">
                              {card.bullets.map((b) => (
                                <li key={b.text}>{b.text}</li>
                              ))}
                            </ul>
                            {card.exploreLink && (
                              <a href={card.exploreLink} className="agents-explore-link">
                                {card.exploreLinkText}
                              </a>
                            )}
                          </div>
                        </>
                      )}
                    </div>
                  ))}
                </div>

                {/* CRM video toggle — work.html L1551–1561 (For Sales Teams group only) */}
                {group.showCrmVideo && (
                  <div className="crm-video-wrap">
                    <button
                      className="crm-video-toggle"
                      id="crm-video-toggle"
                      aria-expanded={crmVideoOpen}
                      onClick={() => setCrmVideoOpen((v) => !v)}
                      type="button"
                    >
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                        <polygon points="5,3 19,12 5,21" />
                      </svg>
                      <span className="crm-video-toggle-text">
                        {crmVideoOpen ? "Hide video" : "See how it works"}
                      </span>
                    </button>
                    <div
                      className={`crm-video-panel${crmVideoOpen ? " open" : ""}`}
                      id="crm-video-panel"
                    >
                      <div className="crm-video-ratio">
                        <iframe
                          id="crm-video-iframe"
                          src={crmVideoOpen ? CRM_VIDEO_SRC : ""}
                          title="See how it works"
                          style={{ border: "none" }}
                          allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                          allowFullScreen
                        />
                      </div>
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>

        </div>
      </div>
    </section>
  );
};

export default WorkAgentsSection;
