/**
 * FocusDemoBand — gradient demo band at the bottom of /focus-alignment.
 * Source-mirrored from Web-Infina-AI/focus-alignment.html #demo section (lines 622–633).
 *
 * HTML uses inline styles with `id="demo"` — NOT the shared .lead-section class pattern.
 * This component preserves the inline-style approach verbatim from HTML source.
 * Both CTAs link to work.html#demo (cross-page); in React these become /work#demo via Link.
 *
 * DIFF FROM infina-pfa-80389: uses className="demo-band" + CSS class abstraction.
 * Mirror keeps the same className approach (CSS must define .demo-band to match HTML inline styles).
 */
import { Link } from "react-router-dom";

const FocusDemoBand = () => (
  <section className="demo-band" id="demo">
    <div className="container demo-band-inner">
      <h2>Ready to get your team aligned?</h2>
      <p>Start in minutes. No setup fees. No seat minimums.</p>
      <div className="demo-band-btns">
        <Link to="/work#demo" className="demo-btn-primary">
          Start for free →
        </Link>
        <Link to="/work#demo" className="demo-btn-secondary">
          Sign in to dashboard
        </Link>
      </div>
    </div>
  </section>
);

export default FocusDemoBand;
