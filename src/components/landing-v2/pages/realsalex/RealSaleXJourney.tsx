import { useRevealOnScroll } from "@/components/landing-v2/hooks/use-reveal-on-scroll";
import { journeyAgents, journeyStages } from "./realsalex-content-data";

/**
 * RealSaleXJourney — the 4-stage buyer journey linked by one animated arrow,
 * followed by the three agents behind it.
 * Mirrors <section class="section" id="how"> in Web-Infina-AI/realsalex.html.
 *
 * The arrow is a single non-scaling-stroke SVG behind the stage grid; the
 * per-stage .jdot markers sit on top of it. The dashed white overlay path
 * animates left-to-right and is disabled under prefers-reduced-motion (CSS).
 *
 * The section keeps the source's inline `background:var(--surface)` because
 * that override lives on the element in the static page, not in its stylesheet.
 */
const RealSaleXJourney = () => {
  const revealRef = useRevealOnScroll<HTMLElement>();

  return (
    <section className="section" id="how" style={{ background: "var(--surface)" }} ref={revealRef}>
      <div className="container">
        <div className="section-head reveal">
          <h2>One companion, the whole journey, from first inquiry to closed deal.</h2>
          <p>Sell-side, for brokerages selling residential inventory to home buyers.</p>
        </div>

        <div className="journey-flow reveal">
          <svg className="journey-arrow" viewBox="0 0 1200 180" preserveAspectRatio="none" aria-hidden="true">
            <defs>
              <linearGradient id="jgrad" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0" stopColor="#1863dc" stopOpacity=".28" />
                <stop offset=".55" stopColor="#1863dc" />
                <stop offset="1" stopColor="#0f4fc0" />
              </linearGradient>
            </defs>
            <path className="jarrow-glow" d="M28,90 L1172,90" fill="none" stroke="#1863dc" strokeWidth="18" strokeLinecap="round" opacity=".12" vectorEffect="non-scaling-stroke" />
            <path className="jarrow-line" d="M28,90 L1172,90" fill="none" stroke="url(#jgrad)" strokeWidth="7" strokeLinecap="round" vectorEffect="non-scaling-stroke" />
            <path className="jarrow-flow" d="M28,90 L1172,90" fill="none" stroke="#fff" strokeWidth="3" strokeLinecap="round" strokeDasharray="2 30" opacity=".75" vectorEffect="non-scaling-stroke" />
          </svg>

          <div className="jstages">
            {journeyStages.map((stage) => (
              <div className="jstage" key={stage.num}>
                <div className="jhead">
                  <span className="jnum">{stage.num}</span>
                  <span className="jname">{stage.name}</span>
                </div>
                <p className="jsub">{stage.sub}</p>
                <div className="jphoto">
                  <img src={stage.image} alt={stage.imageAlt} loading="lazy" />
                  <span className="jdot" />
                  <div className="jchip">
                    <span className="jchip-ic">{stage.chipIcon}</span>
                    <span className="jchip-tx">{stage.chipText}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="agents-icons reveal">
          {journeyAgents.map((agent) => (
            <div className="aic" key={agent.title}>
              <span className="aic-ic">{agent.icon}</span>
              <div>
                <h3>{agent.title}</h3>
                <p>{agent.text}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default RealSaleXJourney;
