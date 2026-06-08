/**
 * Mirrors the #core-v2 section of home.html (lines 5981–6249).
 * All class names, text, and SVG geometry reproduced verbatim from HTML source.
 */
const HomeCoreSection = () => (
  <section className="core-v2-section" id="core-v2">
    <div className="container">
      <div className="core-v2-header">
        <span className="core-v2-eyebrow">INFINA AI CORE</span>
        <h2 className="core-v2-headline">
          One platform,{" "}
          <span className="core-v2-accent">customizable for every job.</span>
        </h2>
      </div>

      {/* Fan SVG + chips (on top, flowing upward) */}
      <div className="core-v2-chips-section">
        <div className="core-v2-chips">
          <div className="core-v2-chip core-v2-chip--blue">
            <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
              <path d="M3 18v-6a9 9 0 0 1 18 0v6" />
              <path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z" />
            </svg>
            Customer Support
          </div>
          <div className="core-v2-chip core-v2-chip--green">
            <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
              <line x1="18" y1="20" x2="18" y2="10" />
              <line x1="12" y1="20" x2="12" y2="14" />
              <line x1="6" y1="20" x2="6" y2="16" />
              <polyline points="3 7 8 12 13 8 21 4" />
              <polyline points="17 4 21 4 21 8" />
            </svg>
            Sales
          </div>
          <div className="core-v2-chip core-v2-chip--blue">
            <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
              <path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z" />
              <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" />
            </svg>
            Operations
          </div>
          <div className="core-v2-chip core-v2-chip--green">
            <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="12" cy="12" r="10" />
              <line x1="12" y1="6" x2="12" y2="18" />
              <path d="M15 9.5a3 3 0 0 0-6 0c0 1.5 1.5 2 3 2.5s3 1 3 2.5a3 3 0 0 1-6 0" />
            </svg>
            Finance
          </div>
          <div className="core-v2-chip core-v2-chip--purple">
            <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
              <polyline points="9 12 11 14 15 10" />
            </svg>
            Compliance
          </div>
        </div>
        <svg
          className="core-v2-fan-svg"
          height="40"
          viewBox="0 0 1000 40"
          preserveAspectRatio="none"
          style={{ transform: "scaleY(-1)" }}
        >
          <defs>
            <filter id="fan-glow" x="-150%" y="-150%" width="400%" height="400%">
              <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="blur" />
              <feMerge>
                <feMergeNode in="blur" />
                <feMergeNode in="SourceGraphic" />
              </feMerge>
            </filter>
            {/* Hidden full-journey paths for each chip — dots travel these */}
            <path id="fan-p1" d="M500 0 V16 H100 V38" />
            <path id="fan-p2" d="M500 0 V16 H300 V38" />
            <path id="fan-p3" d="M500 0 V38" />
            <path id="fan-p4" d="M500 0 V16 H700 V38" />
            <path id="fan-p5" d="M500 0 V16 H900 V38" />
          </defs>
          {/* Center vertical stem — dashes flow upward */}
          <line x1="500" y1="0" x2="500" y2="36" stroke="#1863dc" strokeWidth="1.5" strokeDasharray="4 3" vectorEffect="non-scaling-stroke">
            <animate attributeName="stroke-dashoffset" from="0" to="-7" dur="0.45s" repeatCount="indefinite" />
          </line>
          {/* Horizontal bus bar — dashes flow outward from center (left half) */}
          <line x1="500" y1="16" x2="100" y2="16" stroke="#1863dc" strokeWidth="1.5" strokeDasharray="4 3" vectorEffect="non-scaling-stroke">
            <animate attributeName="stroke-dashoffset" from="0" to="-7" dur="0.45s" repeatCount="indefinite" />
          </line>
          {/* Horizontal bus bar — dashes flow outward from center (right half) */}
          <line x1="500" y1="16" x2="900" y2="16" stroke="#1863dc" strokeWidth="1.5" strokeDasharray="4 3" vectorEffect="non-scaling-stroke">
            <animate attributeName="stroke-dashoffset" from="0" to="-7" dur="0.45s" repeatCount="indefinite" />
          </line>
          {/* 4 outer vertical drops — dashes flow upward */}
          <line x1="100" y1="16" x2="100" y2="36" stroke="#1863dc" strokeWidth="1.5" strokeDasharray="4 3" vectorEffect="non-scaling-stroke">
            <animate attributeName="stroke-dashoffset" from="0" to="-7" dur="0.45s" repeatCount="indefinite" />
          </line>
          <line x1="300" y1="16" x2="300" y2="36" stroke="#1863dc" strokeWidth="1.5" strokeDasharray="4 3" vectorEffect="non-scaling-stroke">
            <animate attributeName="stroke-dashoffset" from="0" to="-7" dur="0.45s" repeatCount="indefinite" />
          </line>
          <line x1="700" y1="16" x2="700" y2="36" stroke="#1863dc" strokeWidth="1.5" strokeDasharray="4 3" vectorEffect="non-scaling-stroke">
            <animate attributeName="stroke-dashoffset" from="0" to="-7" dur="0.45s" repeatCount="indefinite" />
          </line>
          <line x1="900" y1="16" x2="900" y2="36" stroke="#1863dc" strokeWidth="1.5" strokeDasharray="4 3" vectorEffect="non-scaling-stroke">
            <animate attributeName="stroke-dashoffset" from="0" to="-7" dur="0.45s" repeatCount="indefinite" />
          </line>
          {/* Dots at each chip (static anchors) */}
          <circle cx="100" cy="38" r="3" fill="#1863dc" />
          <circle cx="300" cy="38" r="3" fill="#1863dc" />
          <circle cx="500" cy="38" r="3" fill="#1863dc" />
          <circle cx="700" cy="38" r="3" fill="#1863dc" />
          <circle cx="900" cy="38" r="3" fill="#1863dc" />
        </svg>
      </div>

      {/* Output card */}
      <div className="core-v2-output-wrap">
        <div className="core-v2-output">
          <div className="core-v2-output-icon">
            <svg viewBox="0 0 621 358" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M456.379 6.26318L458.036 9.96826L606.674 342.21L610.62 351.032H545.004L543.363 347.277L398.108 15.0347L394.273 6.26318H456.379Z" stroke="#001A68" strokeWidth="12.5261" />
              <path d="M222.803 7.82861L219.877 14.4292L71.2744 349.645L70.0361 352.439H7.25391L10.2217 345.82L160.527 10.604L161.771 7.82861H222.803Z" fill="#001A68" stroke="#001A68" strokeWidth="9.39458" />
              <mask id="output-logo-mask" maskUnits="userSpaceOnUse" x="120.065" y="4.53027" width="379" height="352" fill="black">
                <rect fill="white" x="120.065" y="4.53027" width="379" height="352" />
                <path d="M484.101 346.996H432.54L382.135 231.286H236.396L186.627 346.996H135.065L284.458 14.5303H334.708L484.101 346.996ZM261.631 172.616H356.102L319.769 91.1279H296.681L261.631 172.616Z" />
              </mask>
              <path d="M484.101 346.996V356.391H498.622L492.67 343.146L484.101 346.996ZM432.54 346.996L423.927 350.748L426.385 356.391H432.54V346.996ZM382.135 231.286L390.748 227.534L388.29 221.892H382.135V231.286ZM236.396 231.286V221.892H230.21L227.766 227.574L236.396 231.286ZM186.627 346.996V356.391H192.813L195.258 350.708L186.627 346.996ZM135.065 346.996L126.496 343.146L120.544 356.391H135.065V346.996ZM284.458 14.5303V5.1357H278.38L275.889 10.6797L284.458 14.5303ZM334.708 14.5303L343.278 10.6797L340.787 5.1357H334.708V14.5303ZM261.631 172.616L253.001 168.904L247.364 182.011H261.631V172.616ZM356.102 172.616V182.011H370.577L364.682 168.791L356.102 172.616ZM319.769 91.1279L328.349 87.3022L325.866 81.7334H319.769V91.1279ZM296.681 91.1279V81.7334H290.495L288.051 87.4159L296.681 91.1279ZM484.101 337.602H432.54V356.391H484.101V337.602ZM432.54 346.996L441.152 343.244L390.748 227.534L373.522 235.038L423.927 350.748L432.54 346.996ZM382.135 221.892H236.396V240.681H382.135V221.892ZM236.396 231.286L227.766 227.574L177.997 343.284L195.258 350.708L245.026 234.998L236.396 231.286ZM186.627 337.602H135.065V356.391H186.627V337.602ZM135.065 346.996L143.634 350.847L293.028 18.3808L275.889 10.6797L126.496 343.146L135.065 346.996ZM284.458 23.9249H334.708V5.1357H284.458V23.9249ZM334.708 14.5303L326.139 18.3808L475.532 350.847L492.67 343.146L343.278 10.6797L334.708 14.5303ZM261.631 182.011H356.102V163.222H261.631V182.011ZM356.102 172.616L364.682 168.791L328.349 87.3022L311.189 94.9536L347.522 176.442L356.102 172.616ZM319.769 81.7334H296.681V100.523H319.769V81.7334ZM296.681 91.1279L288.051 87.4159L253.001 168.904L270.261 176.328L305.311 94.8399L296.681 91.1279Z" fill="#001A68" mask="url(#output-logo-mask)" />
              <path d="M334.729 14.0435L334.921 14.4526L377.517 105.132L377.994 106.146H291.532L262.516 173.104H355.73L355.917 173.528L381.228 230.759L381.669 231.759H236.877L188.627 346.531L188.441 346.973L187.96 346.966L136.722 346.223L135.641 346.208L136.083 345.22L284.242 14.4644L284.43 14.0435H334.729Z" fill="#001A68" stroke="#001A68" strokeWidth="1.42342" />
            </svg>
          </div>
          <div className="core-v2-output-text">
            <h3>Custom Infina AI Specialist</h3>
            <p>Built around the client's workflow, systems, data, and operating rules.</p>
          </div>
        </div>
      </div>

      {/* Converge arrow (flipped to flow upward into the specialist) */}
      <div className="core-v2-converge">
        <svg
          className="core-v2-converge-svg"
          height="48"
          viewBox="0 0 1000 48"
          preserveAspectRatio="none"
          fill="none"
          aria-hidden="true"
          style={{ transform: "scaleY(-1)" }}
        >
          <defs>
            <filter id="cv-glow-g" x="-150%" y="-150%" width="400%" height="400%">
              <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur" />
              <feMerge>
                <feMergeNode in="blur" />
                <feMergeNode in="SourceGraphic" />
              </feMerge>
            </filter>
            <filter id="cv-glow-b" x="-150%" y="-150%" width="400%" height="400%">
              <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur" />
              <feMerge>
                <feMergeNode in="blur" />
                <feMergeNode in="SourceGraphic" />
              </feMerge>
            </filter>
          </defs>
          {/* Static paths */}
          <path
            id="cv-path-green"
            d="M218 0 V16 Q218 30 232 30 H486 Q500 30 500 40 V42"
            stroke="#149a6e"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            fill="none"
            vectorEffect="non-scaling-stroke"
            strokeDasharray="6 5"
          >
            <animate attributeName="stroke-dashoffset" from="0" to="-22" dur="0.65s" repeatCount="indefinite" />
          </path>
          <path
            id="cv-path-blue"
            d="M782 0 V16 Q782 30 768 30 H514 Q500 30 500 40 V42"
            stroke="#1863dc"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            fill="none"
            vectorEffect="non-scaling-stroke"
            strokeDasharray="6 5"
          >
            <animate attributeName="stroke-dashoffset" from="0" to="-22" dur="0.65s" repeatCount="indefinite" />
          </path>
          <path
            d="M492 40 L500 47 L508 40"
            stroke="#1863dc"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            fill="none"
            vectorEffect="non-scaling-stroke"
          />
        </svg>
      </div>

      <div className="core-v2-col-labels">
        <span className="core-v2-label-green">Client Context</span>
        <span></span>
        <span className="core-v2-label-blue">Infina AI Core</span>
      </div>

      <div className="core-v2-rows-wrap">
        <div className="core-v2-rows">

          {/* Row 1 */}
          <div className="core-v2-row">
            <div className="core-v2-lcard">
              <div className="core-v2-icon core-v2-icon--green">
                <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
                  <rect x="9" y="2" width="6" height="4" rx="1" />
                  <rect x="2" y="18" width="6" height="4" rx="1" />
                  <rect x="16" y="18" width="6" height="4" rx="1" />
                  <line x1="12" y1="6" x2="12" y2="12" />
                  <line x1="12" y1="12" x2="5" y2="18" />
                  <line x1="12" y1="12" x2="19" y2="18" />
                </svg>
              </div>
              <div className="core-v2-card-text">
                <h3>Business Workflow</h3>
                <p>The process and steps to automate</p>
              </div>
            </div>
            <div className="core-v2-conn">
              <div className="core-v2-conn-line"></div>
              <span className="core-v2-conn-label">Defines how work gets done</span>
            </div>
            <div className="core-v2-rcard">
              <div className="core-v2-icon core-v2-icon--blue">
                <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
                  <rect x="9" y="2" width="6" height="4" rx="1" />
                  <rect x="2" y="18" width="6" height="4" rx="1" />
                  <rect x="16" y="18" width="6" height="4" rx="1" />
                  <line x1="12" y1="6" x2="12" y2="12" />
                  <line x1="12" y1="12" x2="5" y2="18" />
                  <line x1="12" y1="12" x2="19" y2="18" />
                </svg>
              </div>
              <div className="core-v2-card-text">
                <h3>Agent Orchestration</h3>
                <p>Coordinates AI agents and workflows</p>
              </div>
            </div>
          </div>

          {/* Row 2 */}
          <div className="core-v2-row">
            <div className="core-v2-lcard">
              <div className="core-v2-icon core-v2-icon--green">
                <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
                  <ellipse cx="12" cy="5" rx="9" ry="3" />
                  <path d="M3 5v4c0 1.66 4.03 3 9 3s9-1.34 9-3V5" />
                  <path d="M3 9v4c0 1.66 4.03 3 9 3s9-1.34 9-3V9" />
                  <path d="M3 13v4c0 1.66 4.03 3 9 3s9-1.34 9-3v-4" />
                </svg>
              </div>
              <div className="core-v2-card-text">
                <h3>Internal Systems</h3>
                <p>The software stack the specialist works with</p>
              </div>
            </div>
            <div className="core-v2-conn">
              <div className="core-v2-conn-line"></div>
              <span className="core-v2-conn-label">Defines where action happens</span>
            </div>
            <div className="core-v2-rcard">
              <div className="core-v2-icon core-v2-icon--blue">
                <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M4 7h3a2 2 0 0 0 2-2a2.4 2.4 0 0 1 4 0a2 2 0 0 0 2 2h3a1 1 0 0 1 1 1v3a2 2 0 0 0 2 2a2.4 2.4 0 0 1 0 4a2 2 0 0 0-2 2v3a1 1 0 0 1-1 1h-3a2 2 0 0 1-2-2a2.4 2.4 0 0 0-4 0a2 2 0 0 1-2 2h-3a1 1 0 0 1-1-1v-3a2 2 0 0 1 2-2a2.4 2.4 0 0 0 0-4a2 2 0 0 1-2-2v-3a1 1 0 0 1 1-1z" />
                </svg>
              </div>
              <div className="core-v2-card-text">
                <h3>Tools &amp; Connectors</h3>
                <p>Connects to apps, systems, and APIs</p>
              </div>
            </div>
          </div>

          {/* Row 3 */}
          <div className="core-v2-row">
            <div className="core-v2-lcard">
              <div className="core-v2-icon core-v2-icon--green">
                <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
                  <polyline points="14 2 14 8 20 8" />
                  <rect x="9" y="13" width="3" height="4" rx="1" />
                  <path d="M9 13v-1a2 2 0 0 1 4 0v1" />
                </svg>
              </div>
              <div className="core-v2-card-text">
                <h3>Private Data</h3>
                <p>Company documents, records, and knowledge</p>
              </div>
            </div>
            <div className="core-v2-conn">
              <div className="core-v2-conn-line"></div>
              <span className="core-v2-conn-label">Defines what the specialist knows</span>
            </div>
            <div className="core-v2-rcard">
              <div className="core-v2-icon core-v2-icon--blue">
                <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
                  <ellipse cx="12" cy="5" rx="9" ry="3" />
                  <path d="M3 5v4c0 1.66 4.03 3 9 3s9-1.34 9-3V5" />
                  <path d="M3 9v4c0 1.66 4.03 3 9 3s9-1.34 9-3V9" />
                  <path d="M3 13v4c0 1.66 4.03 3 9 3s9-1.34 9-3v-4" />
                </svg>
              </div>
              <div className="core-v2-card-text">
                <h3>Knowledge &amp; Data</h3>
                <p>Grounds the specialist in trusted knowledge</p>
              </div>
            </div>
          </div>

          {/* Row 4 */}
          <div className="core-v2-row">
            <div className="core-v2-lcard">
              <div className="core-v2-icon core-v2-icon--green">
                <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                  <polyline points="9 12 11 14 15 10" />
                </svg>
              </div>
              <div className="core-v2-card-text">
                <h3>Business Rules &amp; Compliance</h3>
                <p>Policies, approvals, and constraints</p>
              </div>
            </div>
            <div className="core-v2-conn">
              <div className="core-v2-conn-line"></div>
              <span className="core-v2-conn-label">Defines how quality and safety are enforced</span>
            </div>
            <div className="core-v2-rcard">
              <div className="core-v2-icon core-v2-icon--blue">
                <svg viewBox="0 0 24 24" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                  <polyline points="9 12 11 14 15 10" />
                </svg>
              </div>
              <div className="core-v2-card-text">
                <h3>Evaluation &amp; Safety</h3>
                <p>Applies guardrails, evals, and monitoring</p>
              </div>
            </div>
          </div>

        </div>{/* /core-v2-rows */}
      </div>{/* /core-v2-rows-wrap */}

    </div>
  </section>
);

export default HomeCoreSection;
