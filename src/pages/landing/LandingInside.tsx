import { useEffect } from "react";
import { Helmet } from "react-helmet-async";
import { useLocation } from "react-router-dom";
import "@/styles/landing-inside.css";
import LandingNav from "@/components/landing-v2/layout/LandingNav";
import LandingFooter from "@/components/landing-v2/layout/LandingFooter";
import LeadSection from "@/components/landing-v2/sections/LeadSection";
import InsideHero from "@/components/landing-v2/pages/inside/InsideHero";
import InsideWhyInside from "@/components/landing-v2/pages/inside/InsideWhyInside";
import InsideCoreSection from "@/components/landing-v2/pages/inside/InsideCoreSection";
import InsideAiQuality from "@/components/landing-v2/pages/inside/InsideAiQuality";
import InsideMeetSpecialists from "@/components/landing-v2/pages/inside/InsideMeetSpecialists";
// Hidden section imports — components are valid JSX; uncomment render below to enable
import InsideSurfaces from "@/components/landing-v2/pages/inside/InsideSurfaces";
import InsideDataProtection from "@/components/landing-v2/pages/inside/InsideDataProtection";
import InsideAdminPortal from "@/components/landing-v2/pages/inside/InsideAdminPortal";

/**
 * LandingInside — native React port of inside.html.
 * Section render order mirrors HTML source order exactly:
 *   Hero → WhyInside → Core (step-journey) → AiQuality → MeetSpecialists
 *   → [HIDDEN: Surfaces, DataProtection, AdminPortal] → Lead (demo)
 *
 * The 3 hidden sections are commented out in the render tree below.
 * Their components are fully implemented — uncomment to enable.
 *
 * Hash anchor support: smoothly scrolls to #demo, #how-it-works, etc. on navigation.
 */
const LandingInside = () => {
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

  // Suppress unused-import warnings for hidden components until enabled
  void InsideSurfaces;
  void InsideDataProtection;
  void InsideAdminPortal;

  return (
    <>
      <Helmet>
        <title>Infina AI Inside · Bring AI Specialists inside your app</title>
        <meta
          name="description"
          content="Embed vertical AI specialists directly into your financial app. White-labeled, compliance-ready, live in 2–3 weeks."
        />
        <meta
          property="og:title"
          content="Infina AI Inside · Bring AI Specialists inside your app"
        />
        <meta
          property="og:description"
          content="Embed vertical AI specialists directly into your financial app. White-labeled, compliance-ready, live in 2–3 weeks."
        />
        <meta property="og:type" content="website" />
      </Helmet>

      <div className="inside-page">
        <LandingNav activePage="inside" ctaLabel="Book a demo" ctaHref="#demo" />
        <InsideHero />
        <InsideWhyInside />
        <InsideCoreSection />
        <InsideAiQuality />
        <InsideMeetSpecialists />
        {/* HIDDEN in source HTML — uncomment to enable */}
        {/* <InsideSurfaces /> */}
        {/* <InsideDataProtection /> */}
        {/* <InsideAdminPortal /> */}
        <LeadSection source="infina-ai-inside-v1" sectionId="demo" />
        <LandingFooter />
      </div>
    </>
  );
};

export default LandingInside;
