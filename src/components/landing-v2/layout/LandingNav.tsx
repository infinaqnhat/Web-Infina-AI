import { useEffect, useState } from "react";
import type { MouseEvent } from "react";
import { Link, useNavigate } from "react-router-dom";

export type ActivePage =
  | "home"
  | "work"
  | "personal"
  | "about"
  | "inside"
  | "focus-alignment"
  | "realsalex";

/**
 * Shared navigation bar for all landing pages.
 *
 * activePage  — which nav link receives the .active class
 * ctaLabel    — CTA button label text
 * ctaHref     — CTA href (hash for scroll or /path for route)
 * ctaExternal — if true, renders an <a target="_blank"> instead of hash scroll
 *
 * Opt-in extras, mirroring nav.js attributes (no other page passes them):
 * centerLinks:      replaces the AI Inside/Work/Personal links (desktop and
 *                   mobile panel) with page-level actions, e.g. tab switches
 * transparentUntil: CSS selector; the bar floats transparently until the
 *                   page scrolls past that element (nav.js transparent-until)
 * logoLarge:        bigger logo on desktop only (nav.js logo-lg)
 *
 * "AI Work" is a plain link to /work. The /focus-alignment and /realsalex
 * routes are still reachable by direct URL but are not surfaced in the nav
 * menu, so on those pages no nav link is highlighted (same as the static
 * pages, whose nav.js has no entry for them either).
 */
export interface LandingActionLink {
  label: string;
  href: string;
  onClick: () => void;
  isActive?: boolean;
}

interface LandingNavProps {
  activePage: ActivePage;
  ctaLabel: string;
  ctaHref: string;
  ctaExternal?: boolean;
  centerLinks?: LandingActionLink[];
  transparentUntil?: string;
  logoLarge?: boolean;
}

/** nav.js switches to solid 80px before the target's bottom edge reaches the top. */
const SOLID_OFFSET_PX = 80;

const LandingNav = ({
  activePage,
  ctaLabel,
  ctaHref,
  ctaExternal = false,
  centerLinks,
  transparentUntil,
  logoLarge = false,
}: LandingNavProps) => {
  const isWork = activePage === "work";

  const [menuOpen, setMenuOpen] = useState(false);
  const [transparent, setTransparent] = useState(Boolean(transparentUntil));
  const navigate = useNavigate();

  const closeMenu = () => setMenuOpen(false);

  useEffect(() => {
    if (!transparentUntil) return;
    const updateSolidity = () => {
      let threshold = window.innerHeight * 0.7;
      const untilEl = document.querySelector(transparentUntil);
      if (untilEl) {
        threshold = untilEl.getBoundingClientRect().bottom + window.scrollY - SOLID_OFFSET_PX;
      }
      setTransparent(window.scrollY < threshold);
    };
    updateSolidity();
    window.addEventListener("scroll", updateSolidity, { passive: true });
    window.addEventListener("resize", updateSolidity);
    return () => {
      window.removeEventListener("scroll", updateSolidity);
      window.removeEventListener("resize", updateSolidity);
    };
  }, [transparentUntil]);

  const navClassName =
    [transparent && "is-transparent", logoLarge && "logo-lg"].filter(Boolean).join(" ") || undefined;

  const renderActionLink = (link: LandingActionLink, afterClick?: () => void) => (
    <a
      key={link.label}
      href={link.href}
      className={link.isActive ? "is-active" : undefined}
      onClick={(e) => {
        e.preventDefault();
        afterClick?.();
        link.onClick();
      }}
    >
      {link.label}
    </a>
  );

  const handleCtaClick = (e: MouseEvent<HTMLAnchorElement>) => {
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

  return (
    <nav className={navClassName}>
      <div className="container nav-inner">
        <Link to="/" className="logo" onClick={closeMenu}>
          <img
            src="/landing-html/uploads/infina-ai-logo-web-329e3857.png"
            alt="Infina AI"
            className="logo-img"
          />
        </Link>

        <div className="nav-center">
          {centerLinks ? (
            centerLinks.map((link) => renderActionLink(link))
          ) : (
            <>
              <Link to="/inside" className={activePage === "inside" ? "active" : undefined}>
                AI Inside
              </Link>

              <Link to="/work" className={isWork ? "active" : undefined}>
                AI Work
              </Link>

              <Link to="/personal" className={activePage === "personal" ? "active" : undefined}>
                AI Personal
              </Link>
            </>
          )}
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
        {centerLinks ? (
          centerLinks.map((link) => renderActionLink(link, closeMenu))
        ) : (
          <>
            <Link to="/inside" className={activePage === "inside" ? "active" : undefined} onClick={closeMenu}>
              AI Inside
            </Link>

            <Link to="/work" className={isWork ? "active" : undefined} onClick={closeMenu}>
              AI Work
            </Link>

            <Link to="/personal" className={activePage === "personal" ? "active" : undefined} onClick={closeMenu}>
              AI Personal
            </Link>
          </>
        )}

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
