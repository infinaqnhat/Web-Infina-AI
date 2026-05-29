import { useState, useRef } from "react";

/**
 * Shared "Book a Demo" lead-capture section used on Home, Work, About, Inside pages.
 *
 * Props:
 *   source    — value submitted to Google Sheets "source" field (per-page identifier)
 *   sectionId — HTML id of the <section> element (home/work/inside: "demo"; about: "lead-form")
 *
 * Form fields: 5 fields (fullName, email, company, phone, useCase). Matches
 * Web-Infina-AI/home.html L5441-5478 source markup exactly. about.html may use
 * the same 5-field structure — confirmed during Phase 04 port.
 */

const SHEETS_ENDPOINT =
  "https://script.google.com/macros/s/AKfycbyO618yfsKfO4nHni2qBe62GWp9fM0vEb0h-Gccw-1wV-w5wJpN3Zayhai1OFxPl98x/exec";

interface FieldErrors {
  fullName?: boolean;
  email?: boolean;
}

interface LeadSectionProps {
  source: string;
  sectionId?: string;
}

const LeadSection = ({ source, sectionId = "demo" }: LeadSectionProps) => {
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [company, setCompany] = useState("");
  const [phone, setPhone] = useState("");
  const [useCase, setUseCase] = useState("");

  const [fieldErrors, setFieldErrors] = useState<FieldErrors>({});
  const [status, setStatus] = useState<{ type: "success" | "error" | ""; text: string }>({
    type: "",
    text: "",
  });
  const [loading, setLoading] = useState(false);

  const formRef = useRef<HTMLFormElement>(null);

  const resetForm = () => {
    setFullName("");
    setEmail("");
    setCompany("");
    setPhone("");
    setUseCase("");
    setFieldErrors({});
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus({ type: "", text: "" });

    const errors: FieldErrors = {};
    if (!fullName.trim()) errors.fullName = true;
    if (!email.trim()) errors.email = true;

    if (Object.keys(errors).length > 0) {
      setFieldErrors(errors);
      setStatus({ type: "error", text: "Please fill in all required fields." });
      return;
    }

    setFieldErrors({});
    setLoading(true);

    const data = {
      fullName: fullName.trim(),
      email: email.trim(),
      company: company.trim(),
      phone: phone.trim(),
      useCase: useCase.trim(),
      source,
    };

    try {
      const fd = new FormData();
      Object.entries(data).forEach(([k, v]) => fd.append(k, String(v)));
      const res = await fetch(SHEETS_ENDPOINT, { method: "POST", body: fd });
      const txt = await res.text();
      if (!res.ok) throw new Error("HTTP " + res.status);
      if (txt.startsWith("<!DOCTYPE") || txt.includes("<html")) {
        throw new Error(
          'Endpoint not public — go to Apps Script → Deploy → Manage deployments → set "Who has access" to "Anyone".'
        );
      }
      if (txt.trim().length > 0) {
        let parsed: { ok?: boolean; error?: string } | null = null;
        try {
          parsed = JSON.parse(txt);
        } catch {
          parsed = null;
        }
        if (parsed && parsed.ok === false) {
          throw new Error(parsed.error || "Sheet error");
        }
        if (!parsed) throw new Error("Unexpected response from sheet endpoint");
      }

      setStatus({
        type: "success",
        text: "✓ Thank you! The Infina AI team will be in touch within 24 hours.",
      });
      resetForm();
    } catch {
      setStatus({
        type: "error",
        text: "An error occurred. Please try again or email contact@infina.ai.",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="lead-section" id={sectionId}>
      <div className="container lead-grid">
        {/* Left copy */}
        <div className="lead-copy">
          <h2>
            <span style={{ background: "#FFE066", padding: "2px 6px", borderRadius: "4px" }}>
              Book a demo
            </span>{" "}
            and watch your job get done by <span className="accent">Infina AI</span>
          </h2>
          <p className="lead-sub">
            30 minutes. We'll show you exactly how Infina AI works and map out what a
            live deployment looks like for your specific situation.
          </p>
        </div>

        {/* Right form */}
        <form
          className="lead-form"
          id={`${sectionId}-form`}
          noValidate
          ref={formRef}
          onSubmit={handleSubmit}
        >
          <div className="lead-form-header">
            <h3 className="lead-form-title">Contact us</h3>
            <p className="lead-form-sub">Infina AI team will respond within 24 hours.</p>
          </div>

          {/* Name */}
          <div className={`lead-field${fieldErrors.fullName ? " invalid" : ""}`}>
            <input
              type="text"
              id="lf-name"
              name="fullName"
              required
              autoComplete="name"
              placeholder=" "
              value={fullName}
              onChange={(e) => {
                setFullName(e.target.value);
                setFieldErrors((fe) => ({ ...fe, fullName: false }));
              }}
            />
            <label htmlFor="lf-name">Name</label>
          </div>

          {/* Work email */}
          <div className={`lead-field${fieldErrors.email ? " invalid" : ""}`}>
            <input
              type="email"
              id="lf-email"
              name="email"
              required
              autoComplete="email"
              placeholder=" "
              value={email}
              onChange={(e) => {
                setEmail(e.target.value);
                setFieldErrors((fe) => ({ ...fe, email: false }));
              }}
            />
            <label htmlFor="lf-email">Work email</label>
          </div>

          {/* Company */}
          <div className="lead-field">
            <input
              type="text"
              id="lf-company"
              name="company"
              autoComplete="organization"
              placeholder=" "
              value={company}
              onChange={(e) => setCompany(e.target.value)}
            />
            <label htmlFor="lf-company">Company (optional)</label>
          </div>

          {/* Phone */}
          <div className="lead-field">
            <input
              type="tel"
              id="lf-phone"
              name="phone"
              autoComplete="tel"
              placeholder=" "
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
            />
            <label htmlFor="lf-phone">Phone</label>
          </div>

          {/* Message */}
          <div className="lead-field lead-textarea">
            <textarea
              id="lf-usecase"
              name="useCase"
              rows={2}
              placeholder=" "
              value={useCase}
              onChange={(e) => setUseCase(e.target.value)}
            />
            <label htmlFor="lf-usecase">Message (optional)</label>
          </div>

          {/* Submit */}
          <button
            type="submit"
            className={`lead-submit${loading ? " loading" : ""}`}
            id="lf-submit"
            disabled={loading}
          >
            <span className="lead-submit-label">{loading ? "Sending..." : "Book a demo"}</span>
            <span className="lead-submit-spinner" aria-hidden="true" />
          </button>

          {/* Status */}
          <div
            className={`lead-status${status.type ? ` ${status.type}` : ""}`}
            id="lf-status"
            role="status"
            aria-live="polite"
          >
            {status.text}
          </div>
        </form>
      </div>
    </section>
  );
};

export default LeadSection;
