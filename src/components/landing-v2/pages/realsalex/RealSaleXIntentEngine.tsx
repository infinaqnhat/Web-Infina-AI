import { Fragment } from "react";
import { useRevealOnScroll } from "@/components/landing-v2/hooks/use-reveal-on-scroll";
import { engineCards, engineLoopSteps } from "./realsalex-content-data";

/**
 * RealSaleXIntentEngine — READS / SCORES / TRIGGERS cards plus the compounding
 * data-loop strip.
 * Mirrors <section class="section killer-section"> in Web-Infina-AI/realsalex.html.
 */
const RealSaleXIntentEngine = () => {
  const revealRef = useRevealOnScroll<HTMLElement>();

  return (
    <section className="section killer-section" ref={revealRef}>
      <div className="container">
        <div className="section-head reveal">
          <h2>The intent-signal engine and the asset it builds.</h2>
        </div>

        <div className="rst-grid">
          {engineCards.map((card) => (
            <div className="rst-card reveal" key={card.k}>
              <div className="k">{card.k}</div>
              <p>{card.text}</p>
            </div>
          ))}
        </div>

        <div className="loop-strip reveal">
          {engineLoopSteps.map((step, i) => (
            <Fragment key={step}>
              <span>{step}</span>
              {i < engineLoopSteps.length - 1 && <em>→</em>}
            </Fragment>
          ))}
        </div>

        <p className="payoff reveal">
          Every conversation becomes structured, <b>company-owned</b> buyer-intent data that is
          yours to keep, deal after deal. It compounds every time you close.
        </p>
      </div>
    </section>
  );
};

export default RealSaleXIntentEngine;
