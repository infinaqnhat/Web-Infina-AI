import { Link } from "react-router-dom";

/**
 * Shared footer for all landing pages — one canonical set of 4 short-label
 * links and the standard logo, identical on every page.
 *
 * Source-of-truth: Web-Infina-AI/footer.js. Link set, labels, and copyright
 * line match the vanilla custom-element implementation 1:1.
 */

const FOOTER_LINKS = [
  { to: "/inside", label: "Inside" },
  { to: "/work", label: "Work" },
  { to: "/personal", label: "Personal" },
];

const LandingFooter = () => (
  <footer>
    <div className="container footer-inner">
      <div className="footer-logo">
        <img
          src="/landing-html/uploads/infina-ai-logo-web-329e3857.png"
          alt="Infina AI"
          className="logo-img"
        />
      </div>
      <div className="footer-links">
        {FOOTER_LINKS.map((l) => (
          <Link key={l.to} to={l.to}>
            {l.label}
          </Link>
        ))}
      </div>
      <p className="footer-copy">© 2026 Infina. All rights reserved.</p>
    </div>
  </footer>
);

export default LandingFooter;
