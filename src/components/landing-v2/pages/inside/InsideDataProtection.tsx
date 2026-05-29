// NEW component — mirrors inside.html L6151-6208 <section class="data-protection" style="display:none">
// 3 static de-identification feature cards.

const InsideDataProtection = () => (
  <section className="data-protection" style={{ display: "none" }}>
    <div className="container">
      <div className="dp-header">
        <div className="dp-badge">
          <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
          </svg>
        </div>
        <span className="dp-eyebrow">USER DATA PROTECTION</span>
        <h2>De-identified. Regulation-compliant. Zero PII.</h2>
        <p className="dp-intro">
          We comply with all applicable personal data protection regulations. Before any data
          reaches the AI, it is fully de-identified — your customers' personal information never
          enters the model.
        </p>
      </div>

      <div className="dp-features">
        <div className="dp-feature">
          <div className="dp-feature-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
              <circle cx="8.5" cy="7" r="4" />
              <line x1="23" y1="11" x2="17" y2="11" />
            </svg>
          </div>
          <div className="dp-feature-content">
            <h4>De-identified by design</h4>
            <p>
              All user records are stripped of personally identifiable information before AI
              processing. Only first name and PartnerID are retained for session mapping.
            </p>
          </div>
        </div>

        <div className="dp-feature">
          <div className="dp-feature-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
              <path d="M7 11V7a5 5 0 0 1 10 0v4" />
            </svg>
          </div>
          <div className="dp-feature-content">
            <h4>No PII in the AI layer</h4>
            <p>
              The AI never sees IDs, phone numbers, emails, or financial account details.
              Responses are personalised using anonymised behavioural data only.
            </p>
          </div>
        </div>

        <div className="dp-feature">
          <div className="dp-feature-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
              <polyline points="14 2 14 8 20 8" />
              <line x1="16" y1="13" x2="8" y2="13" />
              <line x1="16" y1="17" x2="8" y2="17" />
            </svg>
          </div>
          <div className="dp-feature-content">
            <h4>Regulation-ready</h4>
            <p>
              Designed to meet personal data protection requirements. Partner data handling terms
              are documented in the partner agreement.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
);

export default InsideDataProtection;
