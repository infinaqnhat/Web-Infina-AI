import { useEffect, useState } from "react";
import { tabCta } from "./realsalex-content-data";
import type { AgentTab } from "./realsalex-content-data";

/** Lets the smooth scroll settle before focusing, as in the source. */
const FOCUS_DELAY_MS = 420;

/**
 * Mobile-only sticky CTA bar (CSS shows it ≤760px). It appears once the
 * active tab's hero create box scrolls out of view and scrolls back to it,
 * focusing the URL field. Mirrors #sticky-cta in Web-Infina-AI/realsalex-v2.html.
 */
const RealSaleXStickyCta = ({ tab }: { tab: AgentTab }) => {
  const { label, anchorId } = tabCta[tab];
  const [show, setShow] = useState(false);

  useEffect(() => {
    const box = document.getElementById(anchorId);
    if (!box) return;
    // Sync once right away so a tab switch never flashes the wrong state.
    const rect = box.getBoundingClientRect();
    setShow(!(rect.bottom > 0 && rect.top < window.innerHeight));
    const observer = new IntersectionObserver(
      (entries) => entries.forEach((entry) => setShow(!entry.isIntersecting)),
      { threshold: 0 }
    );
    observer.observe(box);
    return () => observer.disconnect();
  }, [anchorId]);

  const backToHeroInput = () => {
    const box = document.getElementById(anchorId);
    if (!box) return;
    box.scrollIntoView({ behavior: "smooth", block: "center" });
    const input = box.querySelector("input");
    if (input) window.setTimeout(() => input.focus(), FOCUS_DELAY_MS);
  };

  return (
    <div id="sticky-cta" className={show ? "show" : undefined}>
      <button type="button" className="btn-primary" onClick={backToHeroInput}>
        {label}
      </button>
    </div>
  );
};

export default RealSaleXStickyCta;
