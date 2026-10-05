import { useLayoutEffect, useRef, useState } from "react";
import { AGENT_TAB_OPTIONS, UPLOADS } from "./realsalex-content-data";
import type { AgentTab } from "./realsalex-content-data";
import RealSaleXListingUrlInput from "./RealSaleXListingUrlInput";
import RealSaleXQrResult from "./RealSaleXQrResult";

/** Swipes shorter than this are treated as taps, as in the source. */
const SWIPE_THRESHOLD_PX = 50;

/** React 18 rejects the camelCase `fetchPriority` prop; the lowercase attribute passes through. */
const LCP_IMAGE_HINT = { fetchpriority: "high" };

interface RealSaleXHeroProps {
  tab: AgentTab;
  onTabChange: (tab: AgentTab) => void;
  onCreateConcierge: () => void;
  onCreateQr: () => void;
  qrRunNonce: number;
}

/**
 * Full-bleed hero slider: Buyer Agent (slide 0) and Listing Agent (slide 1).
 * Mirrors <header class="hero-slider" id="hero-slider"> in
 * Web-Infina-AI/realsalex-v2.html.
 *
 * The track is 200% wide and shifts by 50% per slide. The pill tabs above it
 * are mobile-only; on desktop the nav's center links drive the same `tab`.
 * A horizontal swipe on the header also switches slides.
 */
const RealSaleXHero = ({ tab, onTabChange, onCreateConcierge, onCreateQr, qrRunNonce }: RealSaleXHeroProps) => {
  const slideIndex = tab === "listing" ? 1 : 0;
  const tabRefs = useRef<Partial<Record<AgentTab, HTMLButtonElement | null>>>({});
  const touchStartX = useRef<number | null>(null);
  const [indicator, setIndicator] = useState({ width: 0, left: 0 });

  // The white pill slides under the active tab; re-measure on resize because
  // the tabs only have a size once the mobile breakpoint shows them.
  useLayoutEffect(() => {
    const measure = () => {
      const el = tabRefs.current[tab];
      if (el) setIndicator({ width: el.offsetWidth, left: el.offsetLeft });
    };
    measure();
    window.addEventListener("resize", measure);
    return () => window.removeEventListener("resize", measure);
  }, [tab]);

  const handleTouchEnd = (clientX: number) => {
    const startX = touchStartX.current;
    touchStartX.current = null;
    if (startX === null) return;
    const dx = clientX - startX;
    if (Math.abs(dx) < SWIPE_THRESHOLD_PX) return;
    const next = Math.max(0, Math.min(1, dx < 0 ? slideIndex + 1 : slideIndex - 1));
    onTabChange(next === 1 ? "listing" : "buying");
  };

  return (
    <header
      className="hero-slider"
      id="hero-slider"
      onTouchStart={(e) => {
        touchStartX.current = e.touches[0].clientX;
      }}
      onTouchEnd={(e) => handleTouchEnd(e.changedTouches[0].clientX)}
    >
      <div className="hero-tabs">
        <div className="hero-tabs-inner">
          <span
            className="hero-tab-indicator"
            style={{ width: `${indicator.width}px`, transform: `translateX(${indicator.left}px)` }}
          />
          {AGENT_TAB_OPTIONS.map((option) => (
            <button
              key={option.tab}
              type="button"
              ref={(el) => {
                tabRefs.current[option.tab] = el;
              }}
              className={`hero-tab${option.tab === tab ? " is-active" : ""}`}
              onClick={() => onTabChange(option.tab)}
            >
              {option.label}
            </button>
          ))}
        </div>
      </div>

      <div className="hero-track" style={{ transform: `translateX(-${slideIndex * 50}%)` }}>
        <div className={`hero-slide hero${slideIndex === 0 ? " is-active" : ""}`}>
          <img
            className="hero-photo"
            src={`${UPLOADS}/hero-boss-gen.jpg`}
            alt="A happy couple holding keys in front of their new home"
            {...LCP_IMAGE_HINT}
          />
          <div className="hero-scrim" />
          <div className="container">
            <div className="hero-copy">
              <h1>
                Don't just send a listing.
                <br className="mobile-break" /> Send a <span className="accent">Concierge.</span>
              </h1>
              <p className="hero-sub">
                Give every buyer a 24/7 Personal Home Concierge that learns what matters to them, helps them
                evaluate every home, and takes actions for them, with you still at the center of the
                relationship.
              </p>
              <div className="create-box" id="hero-create">
                <span className="create-label">Paste a property listing</span>
                <div className="create-row">
                  <RealSaleXListingUrlInput id="url-1" />
                  <button type="button" className="btn-primary" onClick={onCreateConcierge}>
                    Create Home Concierge →
                  </button>
                </div>
                <p className="create-note">No CRM connection. No setup. Create your first advisor in under a minute.</p>
              </div>
            </div>
          </div>
        </div>

        <div className={`hero-slide hero hero-seller${slideIndex === 1 ? " is-active" : ""}`}>
          <img
            className="hero-photo"
            src={`${UPLOADS}/hero-listing-new.jpg`}
            alt="A For Sale yard sign with a QR code sticker in front of a home"
            loading="lazy"
          />
          <div className="hero-scrim" />
          <div className="container">
            <div className="hero-copy">
              <h1>
                Turn every brochure and yard sign into a{" "}
                <span className="accent">
                  24/7
                  <br className="mobile-break" /> Property Expert.
                </span>
              </h1>
              <p className="hero-sub">
                Scan the QR Code to get an AI expert that knows everything about the property and help buyers
                instantly from details and disclosures to pricing and next steps at any time 24/7.
              </p>
              <div className="create-box" id="hero-create-qr">
                <span className="create-label">Paste link to your listing</span>
                <div className="create-row">
                  <RealSaleXListingUrlInput id="url-qr" />
                  <button type="button" className="btn-primary" onClick={onCreateQr}>
                    Create Property Expert →
                  </button>
                </div>
                <p className="create-note">No setup. No upload. Create your Property Expert in under a minute.</p>
              </div>
              <RealSaleXQrResult runNonce={qrRunNonce} />
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default RealSaleXHero;
