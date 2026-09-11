import { useRevealOnScroll } from "@/components/landing-v2/hooks/use-reveal-on-scroll";
import { faqItems } from "./realsalex-content-data";

/**
 * RealSaleXFaq — "Answers before you ask." six-item list.
 * Mirrors <section class="section faq-section"> in Web-Infina-AI/realsalex.html.
 */
const RealSaleXFaq = () => {
  const revealRef = useRevealOnScroll<HTMLElement>();

  return (
    <section className="section faq-section" ref={revealRef}>
      <div className="container">
        <div className="section-head reveal">
          <h2>Answers before you ask.</h2>
        </div>
        <div className="faq-list">
          {faqItems.map((item) => (
            <div className="faq-item reveal" key={item.q}>
              <h3>{item.q}</h3>
              <p>{item.a}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default RealSaleXFaq;
