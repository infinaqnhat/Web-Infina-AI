import { Link } from "react-router-dom";

/**
 * About page CTA section — mirrors about.html L1262–1271.
 * CTA order matches HTML: btn-primary "Book a Demo" first, btn-ghost "Try Infina.ai →" second.
 * #lead-form → smooth scroll. /personal → <Link>.
 */
const AboutCtaSection = () => {
  const handleDemoClick = (e: React.MouseEvent<HTMLAnchorElement>) => {
    e.preventDefault();
    const el = document.getElementById("lead-form");
    if (el) el.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <section className="cta">
      <div className="container">
        <h2>Ready to Embed the AI That's Already Live?</h2>
        <p>
          Try Infina.ai to experience the product yourself, or book a call to
          discuss embedding it in your app.
        </p>
        <div className="cta-btns">
          <a href="#lead-form" className="btn-primary" onClick={handleDemoClick}>
            Book a Demo
          </a>
          <Link to="/personal" className="btn-ghost">
            Try Infina.ai →
          </Link>
        </div>
      </div>
    </section>
  );
};

export default AboutCtaSection;
