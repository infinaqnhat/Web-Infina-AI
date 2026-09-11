import { useRevealOnScroll } from "@/components/landing-v2/hooks/use-reveal-on-scroll";
import { UPLOADS, resultCards } from "./realsalex-content-data";

const BAND_IMAGE = `${UPLOADS}/realsalex-results-band.png`;
const BAND_ALT = "A real estate sales team reviewing results together in a modern brokerage office";

/**
 * RealSaleXResults — "10+ hours back every week" band over a team photo,
 * with the 4 outcome cards below.
 * Mirrors <section class="results-band"> in Web-Infina-AI/realsalex.html.
 *
 * The photo appears twice by design, exactly as in the source: .results-bg is
 * the desktop full-bleed background layer, .results-photo is the stacked
 * mobile crop. CSS shows only one of them at any viewport width.
 */
const RealSaleXResults = () => {
  const revealRef = useRevealOnScroll<HTMLElement>();

  return (
    <section className="results-band" ref={revealRef}>
      <div className="results-bg">
        <img src={BAND_IMAGE} alt={BAND_ALT} />
      </div>
      <div className="container">
        <div className="results-grid">
          <div className="results-copy reveal">
            <span className="results-eyebrow">What changes when you run</span>
            <h2>with a smart companion.</h2>
            <p className="results-sub">Spend less time on the work that slows you down.</p>
            <div className="results-get">
              Get
              <svg className="results-get-arrow" width="110" height="55" viewBox="0 0 110 55" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M8 12 C30 8, 52 9, 68 17 C80 23, 87 31, 92 40" stroke="#0A5BFF" strokeWidth="2.8" strokeLinecap="round" fill="none" />
                <path d="M82 36 L92 40 L90 30" stroke="#0A5BFF" strokeWidth="2.8" strokeLinecap="round" strokeLinejoin="round" fill="none" />
              </svg>
            </div>
            <div className="results-hero-stat">
              <span className="num">10+</span>
              <span className="unit">HOURS</span>
              <span className="line2">
                <span className="ul-word">
                  back
                  <svg width="160" height="18" viewBox="0 0 160 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                      <linearGradient id="underlineGradient" x1="3" y1="0" x2="157" y2="0" gradientUnits="userSpaceOnUse">
                        <stop offset="0%" stopColor="#8DBDFF" stopOpacity="0.95" />
                        <stop offset="55%" stopColor="#A8CEFF" stopOpacity="0.75" />
                        <stop offset="82%" stopColor="#BCD9FF" stopOpacity="0.45" />
                        <stop offset="100%" stopColor="#D7E8FF" stopOpacity="0" />
                      </linearGradient>
                    </defs>
                    <path d="M4 11.3 C29 8.8, 58 7.2, 88 7.1 C113 7.0, 136 7.7, 157 9.1 C136 9.0, 113 9.1, 88 9.7 C58 10.2, 29 12.1, 4 13.1 C2.7 13.1, 2.4 11.8, 4 11.3 Z" fill="url(#underlineGradient)" />
                  </svg>
                </span>{" "}
                every week.
              </span>
            </div>
            <div className="results-note">More time for clients, relationships, and growth.</div>
          </div>

          <div className="results-photo reveal">
            <img src={BAND_IMAGE} alt={BAND_ALT} />
          </div>
        </div>

        <div className="results-cards">
          {resultCards.map((card) => (
            <div className="rcard reveal" key={card.label}>
              <div className="rcard-ic">{card.icon}</div>
              <span className="rcard-stat">{card.stat}</span>
              <span className="rcard-label">{card.label}</span>
              <span className="rcard-desc">{card.desc}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default RealSaleXResults;
