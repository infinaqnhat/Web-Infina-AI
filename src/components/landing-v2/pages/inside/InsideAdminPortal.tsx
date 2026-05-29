// NEW component — mirrors inside.html L6214-6292 <section class="admin-portal" style="display:none">
// 6 static admin feature cards.

const InsideAdminPortal = () => (
  <section className="admin-portal" style={{ display: "none" }}>
    <div className="container">
      <div className="admin-portal-header">
        <span className="admin-portal-badge">ADMIN PORTAL</span>
        <h2>Full Control. Zero Engineering.</h2>
        <p>
          Every partner gets a purpose-built admin portal. No setup. No configuration. Just log
          in and you're in command of your AI.
        </p>
      </div>

      <div className="admin-highlight">
        <h3>Your AI. Your data. Your dashboard.</h3>
        <p>
          Manage your knowledge base, golden dataset, usage, customers, conversation histories,
          evaluation results, and AI analytics — all in one place.
        </p>
      </div>

      <div className="admin-cards-grid">
        <div className="admin-feature-card">
          <div className="admin-card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
              <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
            </svg>
          </div>
          <h4>Knowledge Base</h4>
          <p>
            Upload and manage the financial content your AI draws from — product specs, market
            data, compliance rules. Update anytime, no engineering ticket required.
          </p>
        </div>

        <div className="admin-feature-card">
          <div className="admin-card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <ellipse cx="12" cy="5" rx="9" ry="3" />
              <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3" />
              <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5" />
            </svg>
          </div>
          <h4>Golden Dataset</h4>
          <p>
            Curate the ground-truth Q&amp;A pairs used to evaluate every agent response before
            deployment. Your dataset grows smarter with every conversation.
          </p>
        </div>

        <div className="admin-feature-card">
          <div className="admin-card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
            </svg>
          </div>
          <h4>Conversation Histories</h4>
          <p>
            Browse every user conversation in full. Filter by agent, date, or quality score.
            Understand exactly what your customers are asking — and how the AI responded.
          </p>
        </div>

        <div className="admin-feature-card">
          <div className="admin-card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M3 3v18h18" />
              <path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3" />
            </svg>
          </div>
          <h4>Evaluation Results</h4>
          <p>
            See per-response scores across accuracy, safety, hallucination, and tool correctness.
            Drill into any failing response and trace exactly why it scored low.
          </p>
        </div>

        <div className="admin-feature-card">
          <div className="admin-card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M3 3v18h18" />
              <path d="m19 9-5 5-4-4-3 3" />
            </svg>
          </div>
          <h4>AI Analytics</h4>
          <p>
            Track engagement, resolution rates, handoff frequency, and quality trends over time.
            Turn AI behavior data into product decisions.
          </p>
        </div>

        <div className="admin-feature-card">
          <div className="admin-card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
              <circle cx="9" cy="7" r="4" />
              <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
              <path d="M16 3.13a4 4 0 0 1 0 7.75" />
            </svg>
          </div>
          <h4>Usage &amp; Customers</h4>
          <p>
            Monitor active customers, session volume, agent usage breakdown, and growth trends.
            Full visibility into how your AI is being used — and by whom.
          </p>
        </div>
      </div>
    </div>
  </section>
);

export default InsideAdminPortal;
