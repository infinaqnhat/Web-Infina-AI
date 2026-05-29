/**
 * Meet the Specialists section.
 * Mirrors inside.html L5775-5845 <section class="meet-specialists">
 * 4 specialist domain cards: Stock, Wealth Management, Personal Finance, Insurance.
 */
const InsideMeetSpecialists = () => (
  <section className="meet-specialists">
    <div className="container">
      <div className="meet-specialists-layout">

        <div className="meet-specialists-left">
          <span className="section-eyebrow-plain">Meet the Specialists</span>
          <h2>
            Four specialists,
            <br />
            <span className="accent-text">built to grow with you.</span>
          </h2>
          <p className="meet-specialists-desc">
            Each specialist is purpose-built for a financial domain. Start with one or all
            four, and expand with custom specialists built around your specific needs.
          </p>
        </div>

        <div className="hero-agents-grid">

          <div className="hero-agent-card">
            <div>
              <span className="hero-agent-title-main">Stock</span>
              <span className="hero-agent-title-sub">Specialist Agent</span>
            </div>
            <span className="hero-agent-badge">Inside stock trading apps</span>
            <ul className="hero-agent-list">
              <li>Market insights tailored to each user's holdings</li>
              <li>Surfaces risks and opportunities in their portfolio</li>
              <li>Alerts on moves that matter, nothing else</li>
            </ul>
          </div>

          <div className="hero-agent-card">
            <div>
              <span className="hero-agent-title-main">Wealth Management</span>
              <span className="hero-agent-title-sub">Specialist Agent</span>
            </div>
            <span className="hero-agent-badge">Inside fund management apps/web</span>
            <ul className="hero-agent-list">
              <li>Fund questions answered instantly</li>
              <li>Investing plans built around real goals</li>
              <li>Asset mix matched to risk profile and timeline</li>
              <li>Flags when to rebalance, and why</li>
            </ul>
          </div>

          <div className="hero-agent-card">
            <div>
              <span className="hero-agent-title-main">Personal Finance</span>
              <span className="hero-agent-title-sub">Specialist Agent</span>
            </div>
            <span className="hero-agent-badge">Inside banking/e-wallet apps</span>
            <ul className="hero-agent-list">
              <li>Matches customers to products that fit their situation</li>
              <li>Shows where money goes and where to improve</li>
              <li>Clarifies loan options and credit improvement steps</li>
              <li>Builds financial confidence in plain language</li>
            </ul>
          </div>

          <div className="hero-agent-card">
            <div>
              <span className="hero-agent-title-main">Insurance</span>
              <span className="hero-agent-title-sub">Specialist Agent</span>
            </div>
            <span className="hero-agent-badge">Inside insurance apps/web</span>
            <ul className="hero-agent-list">
              <li>Finds coverage that fits, not just what's available</li>
              <li>Answers policy questions any time, in plain language</li>
              <li>Guides customers through claims to get what they're entitled to</li>
            </ul>
          </div>

        </div>

      </div>
    </div>
  </section>
);

export default InsideMeetSpecialists;
