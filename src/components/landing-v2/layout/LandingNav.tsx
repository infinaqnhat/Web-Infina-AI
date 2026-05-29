import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

export type ActivePage = "home" | "work" | "personal" | "about" | "inside" | "focus-alignment";

/**
 * Shared navigation bar for all landing pages.
 *
 * activePage  — which nav link receives the .active class
 * ctaLabel    — CTA button label text
 * ctaHref     — CTA href (hash for scroll or /path for route)
 * ctaExternal — if true, renders an <a target="_blank"> instead of hash scroll
 *
 * The "AI Work" entry is a dropdown group: its toggle navigates to /work and is
 * active for both the work and focus-alignment pages; the menu links to
 * /focus-alignment. Menu opens on hover and on keyboard focus, closes on Esc.
 *
 * Source-of-truth: Web-Infina-AI/nav.js. Link set, labels, CTA text, and
 * dropdown structure match the vanilla custom-element implementation 1:1.
 */
interface LandingNavProps {
  activePage: ActivePage;
  ctaLabel: string;
  ctaHref: string;
  ctaExternal?: boolean;
}

const LandingNav = ({ activePage, ctaLabel, ctaHref, ctaExternal = false }: LandingNavProps) => {
  const isWorkGroup = activePage === "work" || activePage === "focus-alignment";
  const isFocus = activePage === "focus-alignment";

  const [menuOpen, setMenuOpen] = useState(false);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [workOpen, setWorkOpen] = useState(isWorkGroup);
  const navigate = useNavigate();

  const closeMenu = () => setMenuOpen(false);

  const handleCtaClick = (e: React.MouseEvent<HTMLAnchorElement>) => {
    if (ctaExternal) return;
    e.preventDefault();
    closeMenu();
    const hashId = ctaHref.replace("#", "");
    const el = document.getElementById(hashId);
    if (el) {
      el.scrollIntoView({ behavior: "smooth" });
    } else if (ctaHref.startsWith("/")) {
      navigate(ctaHref);
    } else {
      navigate("/" + ctaHref);
    }
  };

  const handleDropdownBlur = (e: React.FocusEvent<HTMLDivElement>) => {
    if (!e.currentTarget.contains(e.relatedTarget as Node)) setDropdownOpen(false);
  };

  return (
    <nav>
      <div className="container nav-inner">
        <Link to="/" className="logo" onClick={closeMenu}>
          <img
            src="/landing-html/uploads/infina-ai-logo-web-329e3857.png"
            alt="Infina AI"
            className="logo-img"
          />
        </Link>

        <div className="nav-center">
          <Link to="/inside" className={activePage === "inside" ? "active" : undefined}>
            AI Inside
          </Link>

          <div
            className={`nav-dropdown${dropdownOpen ? " open" : ""}`}
            onMouseEnter={() => setDropdownOpen(true)}
            onMouseLeave={() => setDropdownOpen(false)}
            onFocus={() => setDropdownOpen(true)}
            onBlur={handleDropdownBlur}
            onKeyDown={(e) => {
              if (e.key === "Escape") setDropdownOpen(false);
            }}
          >
            <Link
              to="/work"
              className={`nav-dropdown-toggle${isWorkGroup ? " active" : ""}`}
              aria-haspopup="true"
              aria-expanded={dropdownOpen}
            >
              AI Work
              <svg
                width="12"
                height="12"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2.5"
              >
                <polyline points="6 9 12 15 18 9" />
              </svg>
            </Link>
            <div className="nav-dropdown-menu" role="menu">
              <Link
                to="/focus-alignment"
                role="menuitem"
                className={isFocus ? "active" : undefined}
              >
                Focus &amp; Alignment
              </Link>
            </div>
          </div>

          <Link to="/personal" className={activePage === "personal" ? "active" : undefined}>
            AI Personal
          </Link>
        </div>

        {ctaExternal ? (
          <a href={ctaHref} target="_blank" rel="noopener noreferrer" className="nav-cta">
            {ctaLabel}
          </a>
        ) : (
          <a href={ctaHref} className="nav-cta" onClick={handleCtaClick}>
            {ctaLabel}
          </a>
        )}

        <button
          className="nav-toggle"
          aria-label="Menu"
          aria-expanded={menuOpen}
          onClick={() => setMenuOpen((v) => !v)}
        >
          <svg
            viewBox="0 0 24 24"
            width="24"
            height="24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            {menuOpen ? (
              <>
                <line x1="18" y1="6" x2="6" y2="18" />
                <line x1="6" y1="6" x2="18" y2="18" />
              </>
            ) : (
              <>
                <line x1="3" y1="6" x2="21" y2="6" />
                <line x1="3" y1="12" x2="21" y2="12" />
                <line x1="3" y1="18" x2="21" y2="18" />
              </>
            )}
          </svg>
        </button>
      </div>

      <div className={`nav-mobile-panel${menuOpen ? " open is-open" : ""}`} aria-hidden={!menuOpen}>
        <Link to="/inside" className={activePage === "inside" ? "active" : undefined} onClick={closeMenu}>
          AI Inside
        </Link>

        <div className="nav-mobile-group">
          <div className="nav-mobile-group-row">
            <Link
              to="/work"
              className={activePage === "work" ? "active" : undefined}
              onClick={closeMenu}
            >
              AI Work
            </Link>
            <button
              className={`nav-mobile-chevron${workOpen ? " open" : ""}`}
              aria-label="Toggle AI Work sub-menu"
              aria-expanded={workOpen}
              onClick={(e) => {
                e.stopPropagation();
                setWorkOpen((v) => !v);
              }}
            >
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                <polyline points="6 9 12 15 18 9" />
              </svg>
            </button>
          </div>
          <div className={`nav-mobile-children${workOpen ? " open" : ""}`}>
            <Link
              to="/focus-alignment"
              className={isFocus ? "active" : undefined}
              onClick={closeMenu}
            >
              Focus &amp; Alignment
            </Link>
          </div>
        </div>

        <Link to="/personal" className={activePage === "personal" ? "active" : undefined} onClick={closeMenu}>
          AI Personal
        </Link>
        {ctaExternal ? (
          <a
            href={ctaHref}
            target="_blank"
            rel="noopener noreferrer"
            className="nav-cta nav-mobile-cta"
            onClick={closeMenu}
          >
            {ctaLabel}
          </a>
        ) : (
          <a href={ctaHref} className="nav-cta nav-mobile-cta" onClick={handleCtaClick}>
            {ctaLabel}
          </a>
        )}
      </div>
    </nav>
  );
};

export default LandingNav;
