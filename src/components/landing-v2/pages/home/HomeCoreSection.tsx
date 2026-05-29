import React from "react";

/**
 * Core section — mirrors home.html L5289–5366 <section class="core-section" id="core">.
 * All class names, inline styles, and SVG paths preserved verbatim from HTML.
 * CSS custom properties (--delay, --tag-color) cast via React.CSSProperties.
 */
const HomeCoreSection = () => (
  <section className="core-section" id="core">
    <div className="container">
      <div className="core-header">
        <div className="core-platform-header" style={{ marginBottom: "24px" }}>
          <div className="core-platform-badge">
            <span className="core-badge-dot" />
            INFINA AI CORE
          </div>
        </div>
        <h2 className="core-headline">
          One infinitely capable core{" "}
          <span className="core-accent">
            that powers every specialist we build.
          </span>
        </h2>
      </div>

      <div className="core-products-row">
        <span
          className="product-tag"
          style={{
            "--tag-color": "#1863dc",
            boxShadow: "0 4px 14px rgba(24, 99, 220, 0.35)",
          } as React.CSSProperties}
        >
          Infina AI Inside
        </span>
        <span
          className="product-tag"
          style={{
            "--tag-color": "#149a6e",
            boxShadow: "0 4px 14px rgba(20, 154, 110, 0.35)",
          } as React.CSSProperties}
        >
          Infina AI Work
        </span>
        <span
          className="product-tag"
          style={{
            "--tag-color": "#7e57c2",
            boxShadow: "0 4px 14px rgba(126, 87, 194, 0.35)",
          } as React.CSSProperties}
        >
          Infina AI Personal
        </span>
      </div>

      <div className="core-platform">
        <div className="core-grid">
          <div className="core-card" style={{ "--delay": "0s" } as React.CSSProperties}>
            <div className="core-card-icon">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.6"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <circle cx="12" cy="12" r="3" />
                <path d="M12 1v6m0 6v6" />
                <circle cx="12" cy="12" r="9" />
                <path d="M16.2 7.8l-8.4 8.4m0-8.4l8.4 8.4" />
              </svg>
            </div>
            <h3 className="core-card-title">Agent Orchestration</h3>
            <p className="core-card-desc">
              Multi-agent coordination and long-running memory so your AI
              specialists plan, collaborate, and get the job done end-to-end.
            </p>
          </div>

          <div className="core-card" style={{ "--delay": "0.1s" } as React.CSSProperties}>
            <div className="core-card-icon">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.6"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <rect x="3" y="3" width="7" height="7" rx="1.5" />
                <rect x="14" y="3" width="7" height="7" rx="1.5" />
                <rect x="3" y="14" width="7" height="7" rx="1.5" />
                <rect x="14" y="14" width="7" height="7" rx="1.5" />
                <path d="M10 6.5h4M10 17.5h4M6.5 10v4M17.5 10v4" />
              </svg>
            </div>
            <h3 className="core-card-title">Tools &amp; Connectors</h3>
            <p className="core-card-desc">
              Pre-built integrations to financial institutions, enterprise
              systems, and business tools so specialists can actually take
              action from day one.
            </p>
          </div>

          <div className="core-card" style={{ "--delay": "0.2s" } as React.CSSProperties}>
            <div className="core-card-icon">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.6"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
                <circle cx="18" cy="6" r="3" />
                <circle cx="6" cy="18" r="3" />
              </svg>
            </div>
            <h3 className="core-card-title">Knowledge &amp; Data</h3>
            <p className="core-card-desc">
              Real-time market data and your private enterprise knowledge,
              giving every specialist the right context to act.
            </p>
          </div>

          <div className="core-card" style={{ "--delay": "0.3s" } as React.CSSProperties}>
            <div className="core-card-icon">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.6"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                <path d="M9 12l2 2 4-4" />
              </svg>
            </div>
            <h3 className="core-card-title">Evaluation &amp; Safety</h3>
            <p className="core-card-desc">
              Built-in guardrails, audit trails, and task-level evals keeping
              every specialist accurate, compliant, and production-ready.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
);

export default HomeCoreSection;
