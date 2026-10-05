import { testimonials } from "./realsalex-content-data";

/**
 * "From agents sending advisors": three agent quotes, shown on both tabs.
 * Mirrors the testimonials <section class="section"> in
 * Web-Infina-AI/realsalex-v2.html (sample quotes, as in the source).
 */
const RealSaleXTestimonials = () => (
  <section className="section">
    <div className="container">
      <div className="section-head reveal">
        <span className="eyebrow">From agents sending advisors</span>
      </div>
      <div className="testi-grid">
        {testimonials.map((t) => (
          <div key={t.name} className="testi reveal">
            <blockquote>{t.quote}</blockquote>
            <div className="testi-who">
              <img className="testi-avatar" src={t.avatar} alt={t.name} />
              <span>
                <b>{t.name}</b>
                <span>{t.meta}</span>
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default RealSaleXTestimonials;
