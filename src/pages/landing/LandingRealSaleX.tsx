import { useEffect } from "react";
import { Helmet } from "react-helmet-async";
import { useLocation } from "react-router-dom";
import "@/styles/landing.css";
import "@/styles/landing-realsalex.css";
import LandingNav from "@/components/landing-v2/layout/LandingNav";
import LandingFooter from "@/components/landing-v2/layout/LandingFooter";
import RealSaleXHero from "@/components/landing-v2/pages/realsalex/RealSaleXHero";
import RealSaleXProblem from "@/components/landing-v2/pages/realsalex/RealSaleXProblem";
import RealSaleXJourney from "@/components/landing-v2/pages/realsalex/RealSaleXJourney";
import RealSaleXShowcase from "@/components/landing-v2/pages/realsalex/RealSaleXShowcase";
import RealSaleXIntentEngine from "@/components/landing-v2/pages/realsalex/RealSaleXIntentEngine";
import RealSaleXResults from "@/components/landing-v2/pages/realsalex/RealSaleXResults";
import RealSaleXFaq from "@/components/landing-v2/pages/realsalex/RealSaleXFaq";
import RealSaleXDemo from "@/components/landing-v2/pages/realsalex/RealSaleXDemo";

const TITLE = "Real Sale X · Your Real Estate Sales Companion";
const DESCRIPTION =
  "Real Sale X works alongside you: it answers your buyers 24/7, nurtures every deal, and pings you the moment a buyer is ready to act, so you close more, not chase.";

/**
 * LandingRealSaleX — native React port of Web-Infina-AI/realsalex.html.
 *
 * Section order (matches the HTML source):
 *   RealSaleXHero → RealSaleXProblem → RealSaleXJourney#how → RealSaleXShowcase
 *   → RealSaleXIntentEngine → RealSaleXResults → RealSaleXFaq
 *   → RealSaleXDemo#see-it-work (+ its success modal)
 *
 * The nav CTA targets #see-it-work, this page's demo anchor. The static page
 * inherits nav.js's hard-coded #demo target, which no element on that page
 * carries, so the button is inert there.
 *
 * Hash anchor support: location.hash change → smooth scroll to matching id.
 */
const LandingRealSaleX = () => {
  const { hash } = useLocation();

  useEffect(() => {
    if (!hash) return;
    const id = hash.replace("#", "");
    const el = document.getElementById(id);
    if (el) {
      const t = setTimeout(() => el.scrollIntoView({ behavior: "smooth" }), 50);
      return () => clearTimeout(t);
    }
  }, [hash]);

  return (
    <div className="realsalex-page">
      <Helmet>
        <title>{TITLE}</title>
        <meta name="description" content={DESCRIPTION} />
        <meta property="og:title" content={TITLE} />
        <meta property="og:description" content={DESCRIPTION} />
        <meta property="og:type" content="website" />
      </Helmet>

      <LandingNav activePage="realsalex" ctaLabel="Book a demo" ctaHref="#see-it-work" />
      <RealSaleXHero />
      <RealSaleXProblem />
      <RealSaleXJourney />
      <RealSaleXShowcase />
      <RealSaleXIntentEngine />
      <RealSaleXResults />
      <RealSaleXFaq />
      <RealSaleXDemo />
      <LandingFooter />
    </div>
  );
};

export default LandingRealSaleX;
