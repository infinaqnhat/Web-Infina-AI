/**
 * Inside page AI quality section.
 * Mirrors the <section class="ai-quality"> in inside.html.
 * 3 process cards (pre-deployment x2, live daily x1) + 2 quality tool cards.
 */
const InsideAiQuality = () => (
  <section className="ai-quality">
    <div className="container">
      <div className="ai-quality-header">
        <span className="section-eyebrow-plain">AI Quality</span>
        <h2>Every Response. Tested. Monitored.<br /><span className="accent-text">Improved.</span></h2>
        <p>
          Uncontrolled AI in financial services is a liability. Every AI Specialist Agent must
          pass a rigorous quality bar before it reaches your customers, and is scored
          continuously once it does.
        </p>
      </div>

      <div className="ai-quality-process">
        <div className="ai-process-card">
          <div className="ai-process-header">
            <div className="ai-process-number">1</div>
            <span className="ai-process-stage">PRE-DEPLOYMENT</span>
          </div>
          <h3>Single-Turn Testing</h3>
          <p>
            Every agent response is evaluated against a golden dataset using up to 16 evaluators
            per response, covering domain accuracy, safety, hallucination, bias, toxicity, and
            tool correctness. Runs before every prompt change or model upgrade.
          </p>
        </div>

        <div className="ai-process-card">
          <div className="ai-process-header">
            <div className="ai-process-number">2</div>
            <span className="ai-process-stage">PRE-DEPLOYMENT</span>
          </div>
          <h3>Multi-Turn Testing</h3>
          <p>
            Full conversation flows are simulated end-to-end, verifying agent routing
            correctness, context retention across turns, handoff smoothness, and tool
            orchestration timing.
          </p>
        </div>

        <div className="ai-process-card">
          <div className="ai-process-header">
            <div className="ai-process-number">3</div>
            <span className="ai-process-stage">LIVE, DAILY</span>
          </div>
          <h3>Production Monitoring</h3>
          <p>
            10% of real customer conversations are automatically sampled and scored daily. An
            alert fires if average quality drops below 0.7. Every production failure becomes a
            test case, permanently strengthening the system.
          </p>
        </div>
      </div>

      <div className="ai-quality-tools">
        <p className="ai-quality-tools-label">Your quality tools</p>
        <div className="ai-quality-tools-row">
          <div className="ai-quality-tool-card">
            <div className="ai-quality-tool-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                <ellipse cx="12" cy="5" rx="9" ry="3" />
                <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3" />
                <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5" />
              </svg>
            </div>
            <div>
              <h4>Golden Dataset</h4>
              <p>
                Curate the ground-truth Q&amp;A pairs used to evaluate every agent response
                before deployment. Your dataset grows smarter with every conversation.
              </p>
            </div>
          </div>
          <div className="ai-quality-tool-card">
            <div className="ai-quality-tool-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                <path d="M3 3v18h18" />
                <path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3" />
              </svg>
            </div>
            <div>
              <h4>Evaluation Results</h4>
              <p>
                See per-response scores across accuracy, safety, hallucination, and tool
                correctness. Drill into any failing response and trace exactly why it scored low.
              </p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>
);

export default InsideAiQuality;
