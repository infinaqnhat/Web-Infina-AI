/**
 * Hero section — mirrors home.html L4221–4237.
 * No CTA buttons — new design has text-only hero.
 *
 * DIFF FROM infina-pfa-80389: hero-sub span text changed from
 * "AI financial specialists" → "AI specialists" to match HTML source.
 */
const HomeHero = () => (
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
            <span className="line">State your problem.</span>
            <br />
            <span className="line line-accent">Watch it get done.</span>
          </h1>
          <p className="hero-sub">
            Not a chatbot. But{" "}
            <span style={{ fontWeight: 700, color: "var(--accent)" }}>
              AI specialists
            </span>{" "}
            that understand your problem, work through it, and get it done for
            you, your team, and your business.
          </p>
        </div>
      </div>
    </div>
  </section>
);

export default HomeHero;
