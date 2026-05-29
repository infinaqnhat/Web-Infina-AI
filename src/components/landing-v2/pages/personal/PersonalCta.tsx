// NEW component — mirrors personal.html L1663-1670 <section class="cta" style="display:none">

/**
 * PersonalCta
 * Hidden gradient call-to-action section.
 * Preserved verbatim from personal.html L1663–1670.
 * All class names and copy match source exactly.
 */
const PersonalCta = () => {
  return (
    <section className="cta">
      <div className="container">
        <h2>
          Start a conversation
          <br />
          with your specialist
        </h2>
        <div className="cta-btns">
          <a
            href="https://infina.ai"
            target="_blank"
            rel="noopener noreferrer"
            className="btn-w"
          >
            Chat with AI Specialist ↑
          </a>
        </div>
      </div>
    </section>
  );
};

export default PersonalCta;
