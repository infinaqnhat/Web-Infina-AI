/**
 * About page "Our Story" timeline section — mirrors about.html L1149–1192.
 * No interactive JS — pure static markup. CSS handles fade-up animations
 * via nth-child animation-delay rules in landing-about.css.
 */
const AboutStorySection = () => (
  <section className="story">
    <div className="container">
      <div className="story-header">
        <h2>Our Story</h2>
      </div>

      <div className="timeline">
        <div className="timeline-item">
          <div className="timeline-dot" />
          <div className="timeline-date">January 2024</div>
          <h3 className="timeline-title">Infina.ai web app launched</h3>
          <p className="timeline-desc">
            Introduced Infina.ai as a chatbot for "Personal Finance" in Vietnam
            — a production product loved by real everyday users.
          </p>
        </div>

        <div className="timeline-item">
          <div className="timeline-dot" />
          <div className="timeline-date">March 2024</div>
          <h3 className="timeline-title">Infina.ai mobile app launched</h3>
          <p className="timeline-desc">
            Expanded to mobile, delivering immersive AI-powered financial
            guidance and deeper insights.
          </p>
        </div>

        <div className="timeline-item">
          <div className="timeline-dot" />
          <div className="timeline-date">August 2024</div>
          <h3 className="timeline-title">Infina AI Inside launched</h3>
          <p className="timeline-desc">
            Introduced Infina AI Inside, the embedded AI sensory platform for
            financial institutions — built on our own tech, tested behind
            Infina.ai.
          </p>
        </div>

        <div className="timeline-item">
          <div className="timeline-dot" />
          <div className="timeline-date">November 2024</div>
          <h3 className="timeline-title">
            Introduced Infina AI Inside to securities firms
          </h3>
          <p className="timeline-desc">
            Presented our embedded AI platform for institutional integrations.
          </p>
        </div>

        <div className="timeline-item">
          <div className="timeline-dot" />
          <div className="timeline-date">January 2025</div>
          <h3 className="timeline-title">First embedded production deployment</h3>
          <p className="timeline-desc">
            Infina AI Inside went live inside a securities firm, delivering
            AI-powered goal-based investing to production.
          </p>
        </div>
      </div>
    </div>
  </section>
);

export default AboutStorySection;
