/**
 * About page mission quote section — mirrors about.html L1195–1202.
 * Pure static markup — no JS conversion needed.
 */
const AboutMissionSection = () => (
  <section className="mission">
    <div className="container">
      <blockquote>
        <span className="accent-quote">
          Democratize financial advice and services through AI
        </span>
      </blockquote>
      <p className="mission-sub">
        In most markets, personalized financial advice is only available to the
        wealthy. A couple banker for every retail investor isn't economically
        viable — until now. We believe AI can close that gap. Not by replacing
        human advisors, but by making good-enough advice accessible to anyone
        at a manageable cost.
      </p>
    </div>
  </section>
);

export default AboutMissionSection;
