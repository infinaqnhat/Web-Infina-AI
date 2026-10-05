import { UPLOADS, trustPoints } from "./realsalex-content-data";
import type { AgentTab } from "./realsalex-content-data";
import RealSaleXGroundedDiagram from "./RealSaleXGroundedDiagram";

/**
 * Data-trust section on the surface background. One section, two tab bodies:
 * buying shows "Your client. Your relationship. Your data." with a photo,
 * listing shows the "Grounded in your listing" diagram. Mirrors
 * <section class="section" style="background:var(--surface);"> in
 * Web-Infina-AI/realsalex-v2.html, inline styles kept as in the source.
 */
const RealSaleXTrust = ({ tab }: { tab: AgentTab }) => (
  <section className="section" style={{ background: "var(--surface)" }}>
    <div className="container">
      <div className="tab-copy" hidden={tab !== "buying"}>
        <div className="trust-grid">
          <div className="reveal">
            <span className="eyebrow">An extension of you, not a replacement</span>
            <h2
              style={{
                fontSize: "clamp(28px,3.6vw,42px)",
                fontWeight: 800,
                letterSpacing: "-.02em",
                lineHeight: 1.15,
                color: "var(--accent)",
              }}
            >
              Your client. Your relationship. <span className="accent">Your data.</span>
            </h2>
            <ul className="trust-list">
              {trustPoints.map((point) => (
                <li key={point}>
                  <span className="dot" />
                  <span className="tx">{point}</span>
                </li>
              ))}
            </ul>
          </div>
          <figure className="trust-photo reveal" style={{ margin: 0 }}>
            <img src={`${UPLOADS}/realsalex-results-band.png`} alt="An agent sitting with two clients in a living room" />
          </figure>
        </div>
      </div>

      <div className="tab-copy" hidden={tab !== "listing"}>
        <div className="section-head reveal">
          <span className="eyebrow">Not another chatbot</span>
          <h2>
            Grounded in your listing. <span className="accent">Never guessing.</span>
          </h2>
          <p>Answers powered by real listing data.</p>
        </div>
        <RealSaleXGroundedDiagram />
      </div>
    </div>
  </section>
);

export default RealSaleXTrust;
