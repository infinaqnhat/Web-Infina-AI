import { Link } from "react-router-dom";

/**
 * About page hero section — mirrors about.html L1127–1146.
 * CTA order matches HTML: btn-primary "Book a demo →" first, btn-ghost "See the live product" second.
 * Internal hash link #lead-form → smooth scroll via click handler.
 * /personal → <Link> (internal route).
 */
const AboutHero = () => {
  const handleDemoClick = (e: React.MouseEvent<HTMLAnchorElement>) => {
    e.preventDefault();
    const el = document.getElementById("lead-form");
    if (el) el.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <section className="hero">
      <div className="hero-bg" />
      <div className="hero-grid-bg" />
      <div className="shape shape-1" />
      <div className="shape shape-2" />
      <div className="shape shape-3" />
      <div className="shape shape-4" />
      <div className="container">
        <div className="hero-grid">
          <div className="hero-text">
            <h1>
              <span className="line">We Built the AI First.</span>
              <br />
              <span className="line line-accent">Then We Made It Available to You.</span>
            </h1>
            <p className="hero-sub">
              Cutting-edge AI used to be a luxury. We built Infina.ai so that
              world-class AI is accessible to more users. Now financial
              institutions embed the same technology in their own apps.
            </p>
            <div className="hero-ctas">
              <a href="#lead-form" className="btn-primary" onClick={handleDemoClick}>
                Book a demo →
              </a>
              <Link to="/personal" className="btn-ghost">
                See the live product
              </Link>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutHero;
