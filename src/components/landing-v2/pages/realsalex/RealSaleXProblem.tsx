import { useRevealOnScroll } from "@/components/landing-v2/hooks/use-reveal-on-scroll";
import { problemStats } from "./realsalex-content-data";

/**
 * RealSaleXProblem — "Deals die in the silence between meetings" stat section.
 * Mirrors the first <section class="section"> in Web-Infina-AI/realsalex.html.
 */
const RealSaleXProblem = () => {
  const revealRef = useRevealOnScroll<HTMLElement>();

  return (
    <section className="section" ref={revealRef}>
      <div className="container">
        <div className="section-head reveal">
          <h2>Deals die in the silence between meetings.</h2>
          <p>
            ~40–50% of leads are never followed up, and the average agent takes 15 hours to reply.
            That gap is revenue you&apos;re not collecting.
          </p>
        </div>
        <div className="stat-cards">
          {problemStats.map((s) => (
            <div className="stat-card reveal" key={s.stat}>
              <b>{s.stat}</b>
              <p>{s.text}</p>
            </div>
          ))}
        </div>
        <p className="sowhat reveal">
          The winners of the next decade will <span className="hl">own buyer intent</span>, not just
          buyer records.
        </p>
      </div>
    </section>
  );
};

export default RealSaleXProblem;
