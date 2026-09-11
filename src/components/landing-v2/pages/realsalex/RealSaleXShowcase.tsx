import { useRevealOnScroll } from "@/components/landing-v2/hooks/use-reveal-on-scroll";
import { showcaseBlocks } from "./realsalex-content-data";

/**
 * RealSaleXShowcase — two product shots (buyer Deal Room, agent dashboard)
 * inside a browser chrome frame.
 * Mirrors the "Real product. Real deals." section in Web-Infina-AI/realsalex.html.
 *
 * <picture> swaps to the mobile crop under 760px, same breakpoint as the source.
 */
const RealSaleXShowcase = () => {
  const revealRef = useRevealOnScroll<HTMLElement>();

  return (
    <section className="section" ref={revealRef}>
      <div className="container">
        <div className="section-head reveal">
          <h2>Real product. Real deals. No new portal to learn.</h2>
        </div>

        {showcaseBlocks.map((block) => (
          <div className="showcase-block reveal" key={block.frameUrl}>
            <div className="showcase-head">
              <div className="tag">{block.tag}</div>
              <h3>{block.heading}</h3>
              <ul className="showcase-list twocol">
                {block.bullets.map((bullet, i) => (
                  <li key={i}>{bullet}</li>
                ))}
              </ul>
            </div>
            <div className="showcase-shot bframe">
              <div className="bframe-bar">
                <span className="bframe-dot" />
                <span className="bframe-dot" />
                <span className="bframe-dot" />
                <span className="bframe-url">{block.frameUrl}</span>
              </div>
              <picture>
                <source media="(max-width:760px)" srcSet={block.imageMobile} />
                <img src={block.image} alt={block.imageAlt} loading="lazy" />
              </picture>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default RealSaleXShowcase;
