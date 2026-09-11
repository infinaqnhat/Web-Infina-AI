import { useEffect, useRef, useState } from "react";
import type { FormEvent } from "react";

const SAMPLE_ZILLOW_URL =
  "https://www.zillow.com/homedetails/123-Main-St-Austin-TX-78701/12345678_zpid/";
const SUBMIT_LABEL = "Show me the Deal Room";

/**
 * RealSaleXDemo — "See it work on a real listing" form plus its success modal.
 * Mirrors <section class="lead-section" id="see-it-work"> and the
 * .demo-modal-backdrop block in Web-Infina-AI/realsalex.html.
 *
 * FRONT-END ONLY: nothing is submitted anywhere and no email is sent. The
 * 600ms delay and the modal are a scripted preview of the real flow, matching
 * the source page exactly.
 *
 * Inputs stay uncontrolled so the source's two native behaviors survive the
 * port: checkValidity() drives the error state, and the floating labels rely
 * on `placeholder=" "` with `:not(:placeholder-shown)`.
 */
const RealSaleXDemo = () => {
  const formRef = useRef<HTMLFormElement>(null);
  const timerRef = useRef<number>();
  const [status, setStatus] = useState("");
  const [loading, setLoading] = useState(false);
  const [modalEmail, setModalEmail] = useState<string | null>(null);

  // Unmounting mid-delay would otherwise reset a detached form and set state
  // on a gone component.
  useEffect(() => () => window.clearTimeout(timerRef.current), []);

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const form = formRef.current;
    if (!form || loading) return;

    setStatus("");

    let firstInvalid: HTMLInputElement | undefined;
    for (const el of Array.from(form.querySelectorAll<HTMLInputElement>("[required]"))) {
      const ok = el.checkValidity();
      el.classList.toggle("invalid", !ok);
      if (!ok && !firstInvalid) firstInvalid = el;
    }
    if (firstInvalid) {
      setStatus("Please fill in all required fields.");
      firstInvalid.focus();
      return;
    }

    const enteredEmail = new FormData(form).get("email")?.toString().trim() ?? "";
    setLoading(true);

    timerRef.current = window.setTimeout(() => {
      setLoading(false);
      form.reset();
      setModalEmail(enteredEmail);
    }, 600);
  };

  const closeModal = () => setModalEmail(null);

  return (
    <>
      <section className="lead-section" id="see-it-work">
        <div className="container lead-grid">
          <div className="lead-copy">
            <h2>
              See it work on a <span className="lead-highlight">real listing.</span>
            </h2>
            <p className="lead-sub">
              Paste a live Zillow listing and your email, we&apos;ll show you what your
              buyer&apos;s Deal Room looks like.
            </p>
          </div>

          <form className="lead-form" ref={formRef} onSubmit={handleSubmit} noValidate>
            <div className="lead-form-header">
              <h3 className="lead-form-title">See how it works</h3>
              <p className="lead-form-sub">
                Drop in one of your active listings and see your buyer&apos;s Deal Room in seconds.
              </p>
            </div>
            <div className="lead-field">
              <input
                type="url"
                id="lf-zillow"
                name="zillowUrl"
                autoComplete="off"
                placeholder=" "
                defaultValue={SAMPLE_ZILLOW_URL}
              />
              <label htmlFor="lf-zillow">Zillow listing URL</label>
            </div>
            <div className="lead-field">
              <input type="email" id="lf-email" name="email" required autoComplete="email" placeholder=" " />
              <label htmlFor="lf-email">Email</label>
            </div>
            <button
              type="submit"
              className={`lead-submit${loading ? " loading" : ""}`}
              id="lf-submit"
              disabled={loading}
            >
              <span className="lead-submit-label">{loading ? "Loading..." : SUBMIT_LABEL}</span>
              <span className="lead-submit-spinner" aria-hidden="true" />
            </button>
            <div className={`lead-status${status ? " error" : ""}`} role="status" aria-live="polite">
              {status}
            </div>
          </form>
        </div>
      </section>

      <div
        className={`demo-modal-backdrop${modalEmail !== null ? " open" : ""}`}
        onClick={(e) => {
          if (e.target === e.currentTarget) closeModal();
        }}
      >
        <div className="demo-modal" role="dialog" aria-modal="true" aria-labelledby="demo-modal-title">
          <button type="button" className="demo-modal-close" onClick={closeModal} aria-label="Close">
            &times;
          </button>
          <div className="demo-modal-icon">✓</div>
          <h3 className="demo-modal-title" id="demo-modal-title">
            Your Deal Room preview is ready.
          </h3>
          <p className="demo-modal-text">
            Here&apos;s a sample of what your buyer would see for this listing. We&apos;ve also sent
            a copy to <strong>{modalEmail}</strong>.
          </p>
          {/* TODO: render the buyer's Deal Room link here once the backend
              preview API (listing URL + email -> Deal Room URL) is live. The
              static sample mockup that used to sit here was removed. */}
        </div>
      </div>
    </>
  );
};

export default RealSaleXDemo;
