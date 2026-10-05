import { useEffect, useState } from "react";
import { Helmet } from "react-helmet-async";
import { useLocation } from "react-router-dom";
import "@/styles/landing.css";
import "@/styles/landing-realsalex.css";
import LandingNav from "@/components/landing-v2/layout/LandingNav";
import type { LandingActionLink } from "@/components/landing-v2/layout/LandingNav";
import LandingFooter from "@/components/landing-v2/layout/LandingFooter";
import { useRevealOnScroll } from "@/components/landing-v2/hooks/use-reveal-on-scroll";
import {
  AGENT_TAB_OPTIONS,
  buyingNextSteps,
  listingReasons,
  tabCta,
} from "@/components/landing-v2/pages/realsalex/realsalex-content-data";
import type { AgentTab } from "@/components/landing-v2/pages/realsalex/realsalex-content-data";
import { buyingJourney, listingJourney } from "@/components/landing-v2/pages/realsalex/realsalex-journey-data";
import RealSaleXHero from "@/components/landing-v2/pages/realsalex/RealSaleXHero";
import RealSaleXCompare from "@/components/landing-v2/pages/realsalex/RealSaleXCompare";
import RealSaleXDemo from "@/components/landing-v2/pages/realsalex/RealSaleXDemo";
import RealSaleXThreeCards from "@/components/landing-v2/pages/realsalex/RealSaleXThreeCards";
import RealSaleXBuyerProfile from "@/components/landing-v2/pages/realsalex/RealSaleXBuyerProfile";
import RealSaleXJourney from "@/components/landing-v2/pages/realsalex/RealSaleXJourney";
import RealSaleXTrust from "@/components/landing-v2/pages/realsalex/RealSaleXTrust";
import RealSaleXIntentEngine from "@/components/landing-v2/pages/realsalex/RealSaleXIntentEngine";
import RealSaleXTestimonials from "@/components/landing-v2/pages/realsalex/RealSaleXTestimonials";
import RealSaleXFinalCta from "@/components/landing-v2/pages/realsalex/RealSaleXFinalCta";
import RealSaleXStickyCta from "@/components/landing-v2/pages/realsalex/RealSaleXStickyCta";

const TITLE = "Send a 24/7 Home Concierge";
const DESCRIPTION =
  "Don't send your client a link, send a 24/7 Home Concierge. Turn any property listing into a private AI Concierge that answers your buyer's questions around the clock, with you still at the center of the relationship.";

/** Lets the smooth scroll back to the hero settle before the QR panel starts. */
const HERO_SCROLL_DELAY_MS = 420;

/** The page opens on the Listing Agent tab unless the URL asks for the buyer one. */
const tabFromHash = (hash: string): AgentTab => {
  const h = hash.toLowerCase();
  return h === "#buyer-agent" || h === "#buyer" ? "buying" : "listing";
};

const scrollToId = (id: string) =>
  document.getElementById(id)?.scrollIntoView({ behavior: "smooth", block: "start" });

/**
 * LandingRealSaleX: native React port of Web-Infina-AI/realsalex-v2.html.
 *
 * One page, two audiences: `tab` switches every section between the Buyer
 * Agent (Home Concierge) and Listing Agent (Property Expert) story. Sections
 * for both tabs stay mounted and the inactive ones are `hidden`, like the
 * source, so one reveal observer covers the whole page.
 *
 * Section order (matches the HTML source):
 *   Hero slider → Compare → Demo#see-it-work → ThreeCards (listing) →
 *   ThreeCards (buying) → BuyerProfile (buying) → Journey (buying) → Trust →
 *   Journey (listing) → IntentEngine (listing) → Testimonials → FinalCta
 * The source's hidden film section (.hero-video-section, display:none) is
 * not ported.
 *
 * Every "create" flow is FRONT-END ONLY: nothing is submitted anywhere.
 */
const LandingRealSaleX = () => {
  const { hash } = useLocation();
  const [tab, setTab] = useState<AgentTab>(() => tabFromHash(hash));
  const [buildRunNonce, setBuildRunNonce] = useState(0);
  const [qrRunNonce, setQrRunNonce] = useState(0);
  const revealRef = useRevealOnScroll<HTMLDivElement>();

  // Hash anchors that name an element (e.g. #see-it-work) scroll to it.
  useEffect(() => {
    if (!hash) return;
    const el = document.getElementById(hash.replace("#", ""));
    if (el) {
      const t = setTimeout(() => el.scrollIntoView({ behavior: "smooth" }), 50);
      return () => clearTimeout(t);
    }
  }, [hash]);

  const goToTab = (next: AgentTab) => {
    scrollToId("hero-slider");
    setTab(next);
  };

  // Buying: build the advisor in the demo card. Listing: generate the QR
  // code under the listing hero, which is where that flow lives.
  const startCreate = () => {
    if (tab === "listing") {
      scrollToId("hero-slider");
      window.setTimeout(() => setQrRunNonce((n) => n + 1), HERO_SCROLL_DELAY_MS);
      return;
    }
    scrollToId("see-it-work");
    setBuildRunNonce((n) => n + 1);
  };

  const tabLinks: LandingActionLink[] = AGENT_TAB_OPTIONS.map((option) => ({
    label: option.label,
    href: "#hero-slider",
    isActive: option.tab === tab,
    onClick: () => goToTab(option.tab),
  }));

  return (
    <div className="realsalex-page" ref={revealRef}>
      <Helmet>
        <title>{TITLE}</title>
        <meta name="description" content={DESCRIPTION} />
        <meta property="og:title" content={TITLE} />
        <meta property="og:description" content={DESCRIPTION} />
        <meta property="og:type" content="website" />
      </Helmet>

      <LandingNav
        activePage="realsalex"
        ctaLabel={tabCta[tab].label}
        ctaHref={`#${tabCta[tab].anchorId}`}
        centerLinks={tabLinks}
        transparentUntil="#hero-slider"
        logoLarge
      />
      <RealSaleXHero
        tab={tab}
        onTabChange={setTab}
        onCreateConcierge={startCreate}
        onCreateQr={() => setQrRunNonce((n) => n + 1)}
        qrRunNonce={qrRunNonce}
      />
      <RealSaleXCompare tab={tab} />
      <RealSaleXDemo tab={tab} buildRunNonce={buildRunNonce} />
      <RealSaleXThreeCards copy={listingReasons} hidden={tab !== "listing"} />
      <RealSaleXThreeCards copy={buyingNextSteps} hidden={tab !== "buying"} />
      <RealSaleXBuyerProfile hidden={tab !== "buying"} />
      <RealSaleXJourney copy={buyingJourney} hidden={tab !== "buying"} />
      <RealSaleXTrust tab={tab} />
      <RealSaleXJourney copy={listingJourney} hidden={tab !== "listing"} />
      <RealSaleXIntentEngine hidden={tab !== "listing"} />
      <RealSaleXTestimonials />
      <RealSaleXFinalCta tab={tab} onCreate={startCreate} />
      <LandingFooter links={tabLinks} />
      <RealSaleXStickyCta tab={tab} />
    </div>
  );
};

export default LandingRealSaleX;
