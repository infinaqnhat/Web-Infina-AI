import { intentSteps } from "./realsalex-content-data";
import { RealSaleXIcon } from "./realsalex-icons";

const HIGHEST_STROKE = { stroke: "#0A2A66", strokeWidth: 1.8, strokeLinecap: "round" } as const;

/**
 * "Turn curiosity into intent." (Listing Agent tab): a 4-step staircase from
 * 42 exploring buyers down to 8 ready to transact. Mirrors the
 * <div class="intent-staircase"> section in Web-Infina-AI/realsalex-v2.html.
 * Desktop draws rising columns on a floor; ≤900px CSS turns the same markup
 * into a vertical timeline with the "From curiosity to closing" outro.
 */
const RealSaleXIntentEngine = ({ hidden }: { hidden: boolean }) => (
  <section className="section" hidden={hidden}>
    <div className="container">
      <div className="section-head reveal">
        <span className="eyebrow">Know what buyers care about</span>
        <h2>
          Turn curiosity into <span className="accent">intent.</span>
        </h2>
        <p>Not all questions mean the same thing. Property Expert helps you see which ones do.</p>
      </div>
      <div className="intent-staircase">
        <div className="intent-funnel reveal">
          {intentSteps.map((step, i) => (
            <div key={step.stage} className={`intent-step lvl-${i + 1}`}>
              <span className="intent-count">{step.count}</span>
              <span className="intent-stage">{step.stage}</span>
              <span className="intent-divider" />
              <p className="intent-example">{step.example}</p>
              <span className="intent-icon">
                <RealSaleXIcon name={step.icon} />
              </span>
            </div>
          ))}
        </div>
        <div className="intent-floor" />
        <span className="intent-highest">
          <svg className="intent-highest-desktop" width="34" height="22" viewBox="0 0 44 28" fill="none">
            <path d="M42 2C28 3 16 10 8 22" {...HIGHEST_STROKE} />
            <path d="M8 22L9.5 15.5" {...HIGHEST_STROKE} />
            <path d="M8 22L14 19.5" {...HIGHEST_STROKE} />
          </svg>
          <RealSaleXIcon
            name="arrowRight"
            className="intent-highest-mobile"
            style={{ transform: "scaleX(-1) rotate(-40deg)" }}
          />
          Highest intent
        </span>
        <div className="intent-outro">
          <span>From curiosity to closing</span>
          <RealSaleXIcon name="chevronDown" />
        </div>
      </div>
    </div>
  </section>
);

export default RealSaleXIntentEngine;
