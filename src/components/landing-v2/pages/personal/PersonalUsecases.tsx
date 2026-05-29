// NEW component — mirrors personal.html L1531-1613 <section class="usecases-modern" style="display:none">
// Note: HTML contains 4 cards (plan estimated 6 — actual count verified from source).

/**
 * PersonalUsecases
 * Hidden "Popular Use Cases" section — 4-card grid.
 * Preserved verbatim from personal.html L1531–1613.
 * All class names, SVG paths, and copy match source exactly.
 */
const PersonalUsecases = () => {
  return (
    <section className="usecases-modern">
      <div className="container">
        <h2 className="usecases-headline">Popular Use Cases</h2>

        <div className="usecases-grid">

          {/* Stock Analysis */}
          <div className="usecase-card" data-index="0">
            <div className="usecase-icon-wrapper">
              <div className="usecase-icon">
                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <polyline points="22 12 18 12 15 21 9 3 6 12 2 12" />
                </svg>
              </div>
            </div>
            <h3 className="usecase-title">Stock Analysis</h3>
            <p className="usecase-subtitle">Portfolio insights &amp; trends</p>
            <ul className="usecase-list">
              <li>Analyze user portfolio, offer insights</li>
              <li>Real-time market trends analysis</li>
              <li>Send smart alerts &amp; recommendations</li>
            </ul>
          </div>

          {/* Insurance */}
          <div className="usecase-card" data-index="1">
            <div className="usecase-icon-wrapper">
              <div className="usecase-icon">
                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                </svg>
              </div>
            </div>
            <h3 className="usecase-title">Insurance</h3>
            <p className="usecase-subtitle">Policy comparison &amp; claims</p>
            <ul className="usecase-list">
              <li>Compare policies &amp; recommend</li>
              <li>Guide through claims process</li>
              <li>Analyze coverage gaps</li>
            </ul>
          </div>

          {/* Personal Finance */}
          <div className="usecase-card" data-index="2">
            <div className="usecase-icon-wrapper">
              <div className="usecase-icon">
                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <line x1="12" y1="1" x2="12" y2="23" />
                  <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
                </svg>
              </div>
            </div>
            <h3 className="usecase-title">Personal Finance</h3>
            <p className="usecase-subtitle">Budget tracking &amp; insights</p>
            <ul className="usecase-list">
              <li>Track spending &amp; budget optimization</li>
              <li>Manage wallet balance &amp; transactions</li>
              <li>Detect unusual transactions &amp; fraud</li>
            </ul>
          </div>

          {/* Wealth Management */}
          <div className="usecase-card" data-index="3">
            <div className="usecase-icon-wrapper">
              <div className="usecase-icon">
                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <rect x="2" y="7" width="20" height="14" rx="2" ry="2" />
                  <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16" />
                </svg>
              </div>
            </div>
            <h3 className="usecase-title">Wealth Management</h3>
            <p className="usecase-subtitle">Fund analysis &amp; goals</p>
            <ul className="usecase-list">
              <li>Compare funds &amp; recommend options</li>
              <li>Analyze portfolio allocation</li>
              <li>Goal-based investing &amp; tracking</li>
            </ul>
          </div>

        </div>
      </div>
    </section>
  );
};

export default PersonalUsecases;
