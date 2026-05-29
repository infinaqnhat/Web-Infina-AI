// NEW component — mirrors work.html L1637–1711 <section class="section" id="agents" style="display:none">
// This is the OLD 4-icon-card agents layout, distinct from the VISIBLE WorkAgentsSection
// (which uses class="agents-section" + specialists-grid layout at L1519).
// Content: "Specialist Agents" header + 4 .agent-card icon cards.

/**
 * Hidden agents section — old 4-icon-card layout.
 * Mirrors <section class="section" id="agents" style="display:none"> in work.html L1637–1711.
 *
 * DISTINCT from WorkAgentsSection (visible, class="agents-section", specialists-grid layout).
 * This section uses .agents-grid with .agent-card + .agent-icon-wrap + .agent-body structure.
 * Cards: Focus & Alignment, Expense Management, Knowledge Base & Expertise, Custom Workflow.
 */
const WorkAgentsHidden = () => {
  return (
    <section className="section" id="agents">
      <div className="container">
        <div className="section-header reveal">
          <p className="section-label">Specialist Agents</p>
          <h2>
            AI Agents for{" "}
            <span className="gradient-text">Every Company Function</span>
          </h2>
          <p>
            Four specialist agents customized to your internal processes. Each
            agent integrates seamlessly with existing tools and workflows.
          </p>
        </div>

        <div className="agents-grid">
          {/* Agent 1 — work.html L1647–1660 */}
          <div className="agent-card reveal">
            <div className="agent-icon-wrap">
              <div className="agent-icon">
                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="white"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <circle cx="12" cy="12" r="10" />
                  <path d="M12 6v6l4 2" />
                </svg>
              </div>
            </div>
            <div className="agent-body">
              <h3>Focus &amp; Alignment Agent</h3>
              <p>
                Agent helps employees{" "}
                <span className="text-highlight">
                  focus weekly and align their priorities
                </span>{" "}
                with team, department, and company goals by understanding
                company OKRs and resolving conflicts.
              </p>
            </div>
          </div>

          {/* Agent 2 — work.html L1662–1675 */}
          <div className="agent-card reveal">
            <div className="agent-icon-wrap">
              <div className="agent-icon">
                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="white"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
                </svg>
              </div>
            </div>
            <div className="agent-body">
              <h3>Expense Management Agent</h3>
              <p>
                Analyze all{" "}
                <span className="text-highlight">
                  spending data from all the SaaS, Cloud, credit card
                  statements, bank statements
                </span>
                , etc… and suggest ways to cut costs.
              </p>
            </div>
          </div>

          {/* Agent 3 — work.html L1677–1691 */}
          <div className="agent-card reveal">
            <div className="agent-icon-wrap">
              <div className="agent-icon">
                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="white"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />
                  <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />
                </svg>
              </div>
            </div>
            <div className="agent-body">
              <h3>Knowledge Base &amp; Expertise Agent</h3>
              <p>
                A user can ask AI to{" "}
                <span className="text-highlight">
                  explain a Slack thread or research related context
                </span>{" "}
                on the web or across company data sources.
              </p>
            </div>
          </div>

          {/* Agent 4 — work.html L1693–1708 */}
          <div className="agent-card reveal">
            <div className="agent-icon-wrap">
              <div className="agent-icon">
                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="white"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <rect x="8" y="2" width="8" height="4" rx="1" ry="1" />
                  <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2" />
                  <path d="M9 12h6M9 16h6" />
                </svg>
              </div>
            </div>
            <div className="agent-body">
              <h3>Custom Workflow Agent</h3>
              <p>
                Take a workflow that can be{" "}
                <span className="text-highlight">
                  fully automated and done by an Agent
                </span>
                . This is customizable for applicable workflow requested by
                clients.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default WorkAgentsHidden;
