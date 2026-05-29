// NEW component — mirrors work.html L1714–1771 <section class="section sales-section" style="display:none">

/**
 * Hidden sales section — CRM & Sales Pipeline specialist agent pitch.
 * Mirrors <section class="section sales-section" style="display:none"> in work.html L1714–1771.
 *
 * Layout: section-header + .sales-features-grid with 4 .sales-feature-card entries.
 * Cards: Intelligent Integration Layer, Multi-Channel Communication,
 *        Automated Actions, Vertical Customization.
 */
const WorkSalesSection = () => {
  return (
    <section className="section sales-section">
      <div className="container">
        <div className="section-header reveal">
          <p className="section-label">Sales Solution</p>
          <h2>
            Specialist Agent for{" "}
            <span className="gradient-text">CRM &amp; Sales Pipeline Management</span>
          </h2>
          <p>Like Salesforce's AgentForce but more affordable and customizable</p>
        </div>

        <div className="sales-features-grid">
          {/* Card 1 — work.html L1723–1734 */}
          <div className="sales-feature-card reveal">
            <div className="sales-card-icon">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <rect x="3" y="3" width="7" height="7" />
                <rect x="14" y="3" width="7" height="7" />
                <rect x="14" y="14" width="7" height="7" />
                <rect x="3" y="14" width="7" height="7" />
              </svg>
            </div>
            <h3>Intelligent Integration Layer</h3>
            <p>
              Works with existing CRM, ERP, etc… Seamlessly connects to your
              current systems without disruption.
            </p>
          </div>

          {/* Card 2 — work.html L1736–1745 */}
          <div className="sales-feature-card reveal">
            <div className="sales-card-icon">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                <path d="M8 10h8M8 14h4" />
              </svg>
            </div>
            <h3>Multi-Channel Communication</h3>
            <p>
              Chat via Slack, WhatsApp, Web, or app. Meet your sales team where
              they already work.
            </p>
          </div>

          {/* Card 3 — work.html L1747–1755 */}
          <div className="sales-feature-card reveal">
            <div className="sales-card-icon">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <polyline points="22 12 18 12 15 21 9 3 6 12 2 12" />
              </svg>
            </div>
            <h3>Automated Actions</h3>
            <p>
              Agent take actions for sales person, including updating CRM, send
              email, etc… Reduce manual data entry.
            </p>
          </div>

          {/* Card 4 — work.html L1757–1768 */}
          <div className="sales-feature-card reveal">
            <div className="sales-card-icon">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
                <polyline points="14 2 14 8 20 8" />
                <line x1="12" y1="18" x2="12" y2="12" />
                <line x1="9" y1="15" x2="15" y2="15" />
              </svg>
            </div>
            <h3>Vertical Customization</h3>
            <p>
              Customized for a certain vertical like real-estate, insurance,
              etc… Industry-specific workflows built-in.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default WorkSalesSection;
