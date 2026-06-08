import { useState, useRef } from "react";

/**
 * Why Infina AI Inside section.
 * Mirrors inside.html L5533-5618 <section class="why-inside"> only.
 * 6 cards in 2 rows; expandable cards (c1, c4) toggle detail panels.
 * c5 and c6 detail content lives in the standalone
 * InsideDataProtection / InsideAdminPortal components.
 * Row 1 panel: c1 (Mobile SDK). Row 2 panel: c4 (Web Embed).
 * The c5/c6 detail panels shown here mirror the HTML detail-c5/detail-c6
 * sub-panels inside panel-row2 exactly as they appear in the source HTML.
 */

type ExpandCard = "c1" | "c4" | "c5" | "c6" | null;

const CARD_ROW: Record<NonNullable<ExpandCard>, "row1" | "row2"> = {
  c1: "row1",
  c4: "row2",
  c5: "row2",
  c6: "row2",
};

const InsideWhyInside = () => {
  const [activeCard, setActiveCard] = useState<ExpandCard>(null);
  const panelRow1Ref = useRef<HTMLDivElement>(null);
  const panelRow2Ref = useRef<HTMLDivElement>(null);

  const handleCardClick = (card: ExpandCard) => {
    if (!card) return;
    const newActive = activeCard === card ? null : card;
    setActiveCard(newActive);
    if (newActive) {
      const row = CARD_ROW[newActive];
      const ref = row === "row1" ? panelRow1Ref : panelRow2Ref;
      setTimeout(() => {
        ref.current?.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }, 50);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent, card: ExpandCard) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      handleCardClick(card);
    }
  };

  const isActive = (card: ExpandCard) => activeCard === card;
  const row1Open = activeCard === "c1";
  const row2Open = activeCard === "c4" || activeCard === "c5" || activeCard === "c6";

  return (
    <section className="why-inside">
      <div className="container">
        <div className="why-inside-layout">

          <div className="why-inside-left">
            <span className="section-eyebrow-plain">What You Get</span>
            <h2>
              Everything your customers need.
              <br />
              <span className="accent-text">Nothing you have to build.</span>
            </h2>
            <p className="why-inside-sub">
              Most fintech apps are tools. With AI Inside, yours becomes an advisor.
            </p>
          </div>

          <div className="why-inside-grid">

            {/* Row 1 */}
            <div
              className={`why-inside-card${isActive("c1") ? " is-active" : ""}`}
              data-card="c1"
              role="button"
              tabIndex={0}
              aria-expanded={isActive("c1")}
              onClick={() => handleCardClick("c1")}
              onKeyDown={(e) => handleKeyDown(e, "c1")}
              style={{ cursor: "pointer" }}
            >
              <div className="why-stat">24/7</div>
              <h3>AI in every screen</h3>
              <p>Your customers get access to a financial AI specialist without leaving your app. No switching, no friction, no drop-off.</p>
            </div>

            <div className="why-inside-card">
              <div className="why-stat">In-context</div>
              <h3>Smarter with your data</h3>
              <p>The AI sees the user's portfolio, the screen they're on, and their behavior. Every response is more relevant than any generic AI can offer.</p>
            </div>

            <div className="why-inside-card">
              <div className="why-stat">Low cost</div>
              <h3>A fraction of in-house cost</h3>
              <p>No engineering team to hire, no months of development, no infrastructure to maintain. The lowest-cost path to AI in your product.</p>
            </div>

            {/* Row 1 detail panel */}
            <div
              ref={panelRow1Ref}
              className={`why-detail-panel${row1Open ? " is-open" : ""}`}
              id="panel-row1"
              aria-hidden={!row1Open}
            >
              <div
                className={`why-detail-inner${row1Open ? " is-visible" : ""}`}
                id="detail-c1"
                style={{ gridTemplateColumns: "1fr" }}
              >
                <div className="why-detail-col" style={{ borderRight: "none" }}>
                  <div className="why-detail-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                      <rect x="6" y="2" width="12" height="20" rx="2.5" />
                      <path d="M11 18h2" />
                    </svg>
                  </div>
                  <h4>Mobile SDK</h4>
                  <p>Embed AI specialists directly into your iOS and Android apps. AI experience without forcing customers to leave your ecosystem. Go-live in 2 to 3 weeks.</p>
                </div>
              </div>
            </div>

            {/* Row 2 */}
            <div
              className={`why-inside-card${isActive("c4") ? " is-active" : ""}`}
              data-card="c4"
              role="button"
              tabIndex={0}
              aria-expanded={isActive("c4")}
              onClick={() => handleCardClick("c4")}
              onKeyDown={(e) => handleKeyDown(e, "c4")}
              style={{ cursor: "pointer" }}
            >
              <div className="why-stat">100% yours</div>
              <h3>Fully white-labeled</h3>
              <p>Looks and feels like your product. Your brand, your design system, your user experience. Infina AI runs invisibly underneath.</p>
            </div>

            <div
              className={`why-inside-card${isActive("c5") ? " is-active" : ""}`}
              data-card="c5"
              role="button"
              tabIndex={0}
              aria-expanded={isActive("c5")}
              onClick={() => handleCardClick("c5")}
              onKeyDown={(e) => handleKeyDown(e, "c5")}
              style={{ cursor: "pointer" }}
            >
              <div className="why-stat">Zero PII</div>
              <h3>Regulation-compliant by design</h3>
              <p>All user data is fully de-identified before reaching the AI. Built to meet financial regulations out of the box.</p>
            </div>

            <div
              className={`why-inside-card${isActive("c6") ? " is-active" : ""}`}
              data-card="c6"
              role="button"
              tabIndex={0}
              aria-expanded={isActive("c6")}
              onClick={() => handleCardClick("c6")}
              onKeyDown={(e) => handleKeyDown(e, "c6")}
              style={{ cursor: "pointer" }}
            >
              <div className="why-stat">No code</div>
              <h3>Full control, zero engineering</h3>
              <p>Manage your AI's knowledge base, monitor response quality, and track usage from a partner dashboard. No tickets, no deployments.</p>
            </div>

            {/* Row 2 detail panel */}
            <div
              ref={panelRow2Ref}
              className={`why-detail-panel${row2Open ? " is-open" : ""}`}
              id="panel-row2"
              aria-hidden={!row2Open}
            >
              {/* c4: Web Embed */}
              <div
                className={`why-detail-inner${isActive("c4") ? " is-visible" : ""}`}
                id="detail-c4"
                style={{ gridTemplateColumns: "1fr" }}
              >
                <div className="why-detail-col" style={{ borderRight: "none" }}>
                  <div className="why-detail-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                      <rect x="2" y="3" width="20" height="14" rx="2" />
                      <path d="M8 21h8M12 17v4" />
                    </svg>
                  </div>
                  <h4>Web Embed</h4>
                  <p>Full white-label. AI specialists seamlessly integrated with your product branding. UI components easily customizable to perfectly match your design system. Quick integration with just 1 line of script.</p>
                </div>
              </div>

              {/* c5: Data Protection */}
              <div
                className={`why-detail-inner${isActive("c5") ? " is-visible" : ""}`}
                id="detail-c5"
              >
                <div className="why-detail-col">
                  <div className="why-detail-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
                      <circle cx="9" cy="7" r="4" />
                      <line x1="23" y1="11" x2="17" y2="11" />
                    </svg>
                  </div>
                  <h4>De-identified by design</h4>
                  <p>All user records are stripped of personally identifiable information before AI processing. Only first name and PartnerID are retained for session mapping.</p>
                </div>
                <div className="why-detail-col">
                  <div className="why-detail-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                      <rect x="3" y="11" width="18" height="11" rx="2" />
                      <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                    </svg>
                  </div>
                  <h4>No PII in the AI layer</h4>
                  <p>The AI never sees IDs, phone numbers, emails, or financial account details. Responses are personalised using anonymised behavioural data only.</p>
                </div>
                <div className="why-detail-col">
                  <div className="why-detail-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M12 2l8 4v6c0 5-3.5 9-8 10-4.5-1-8-5-8-10V6z" />
                      <path d="M9 12l2 2 4-4" />
                    </svg>
                  </div>
                  <h4>Regulation-ready</h4>
                  <p>Designed to meet personal data protection requirements. Partner data handling terms are documented in the partner agreement.</p>
                </div>
              </div>

              {/* c6: Admin Portal */}
              <div
                className={`why-detail-inner${isActive("c6") ? " is-visible" : ""}`}
                id="detail-c6"
                style={{ gridTemplateColumns: "repeat(3,1fr)" }}
              >
                <div className="why-detail-col">
                  <div className="why-detail-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
                      <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
                    </svg>
                  </div>
                  <h4>Knowledge Base</h4>
                  <p>Upload and manage the financial content your AI draws from. Product specs, market data, compliance rules. Update anytime, no engineering ticket required.</p>
                </div>
                <div className="why-detail-col">
                  <div className="why-detail-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                      <ellipse cx="12" cy="5" rx="9" ry="3" />
                      <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3" />
                      <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5" />
                    </svg>
                  </div>
                  <h4>Golden Dataset</h4>
                  <p>Curate the ground-truth Q&amp;A pairs used to evaluate every agent response before deployment. Your dataset grows smarter with every conversation.</p>
                </div>
                <div className="why-detail-col">
                  <div className="why-detail-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                    </svg>
                  </div>
                  <h4>Conversation Histories</h4>
                  <p>Browse every user conversation in full. Filter by agent, date, or quality score. Understand exactly what your customers are asking and how the AI responded.</p>
                </div>
                <div className="why-detail-col" style={{ borderTop: "1px solid var(--border-light)" }}>
                  <div className="why-detail-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M3 3v18h18" />
                      <path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3" />
                    </svg>
                  </div>
                  <h4>Evaluation Results</h4>
                  <p>See per-response scores across accuracy, safety, hallucination, and tool correctness. Drill into any failing response and trace exactly why it scored low.</p>
                </div>
                <div className="why-detail-col" style={{ borderTop: "1px solid var(--border-light)" }}>
                  <div className="why-detail-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M3 3v18h18" />
                      <path d="m19 9-5 5-4-4-3 3" />
                    </svg>
                  </div>
                  <h4>AI Analytics</h4>
                  <p>Track engagement, resolution rates, handoff frequency, and quality trends over time. Turn AI behavior data into product decisions.</p>
                </div>
                <div className="why-detail-col" style={{ borderTop: "1px solid var(--border-light)" }}>
                  <div className="why-detail-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
                      <circle cx="9" cy="7" r="4" />
                      <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
                      <path d="M16 3.13a4 4 0 0 1 0 7.75" />
                    </svg>
                  </div>
                  <h4>Usage &amp; Customers</h4>
                  <p>Monitor active customers, session volume, agent usage breakdown, and growth trends. Full visibility into how your AI is being used and by whom.</p>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>
  );
};

export default InsideWhyInside;
