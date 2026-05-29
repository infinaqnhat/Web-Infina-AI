import { useEffect } from "react";
import { Helmet } from "react-helmet-async";
import { useLocation } from "react-router-dom";
import "@/styles/landing-work.css";
import LandingNav from "@/components/landing-v2/layout/LandingNav";
import LandingFooter from "@/components/landing-v2/layout/LandingFooter";
import LeadSection from "@/components/landing-v2/sections/LeadSection";
import WorkHero from "@/components/landing-v2/pages/work/WorkHero";
import WorkAgentsSection from "@/components/landing-v2/pages/work/WorkAgentsSection";
import WorkCoworkersSection from "@/components/landing-v2/pages/work/WorkCoworkersSection";
// import WorkAgentsHidden from "@/components/landing-v2/pages/work/WorkAgentsHidden";
// import WorkSalesSection from "@/components/landing-v2/pages/work/WorkSalesSection";
// import WorkContextAISection from "@/components/landing-v2/pages/work/WorkContextAISection";

/**
 * LandingWork — native React port of Web-Infina-AI/work.html.
 *
 * Section order (matches HTML source):
 *   WorkHero (L940) → WorkCoworkersSection (L981) → WorkAgentsSection (L1519)
 *   → LeadSection#demo (L1888)
 *
 * Three hidden sections (display:none in source HTML) are commented out below.
 * Uncomment to enable once content is approved:
 *   WorkAgentsHidden  — Web-Infina-AI/work.html L1637–1711
 *   WorkSalesSection  — Web-Infina-AI/work.html L1714–1771
 *   WorkContextAISection — Web-Infina-AI/work.html L1775–1885
 *
 * Hash anchor support: location.hash change → smooth scroll to matching id.
 */
const LandingWork = () => {
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
    <div className="work-page">
      <Helmet>
        <title>Infina AI Work · Specialist Agents for Your Company</title>
        <meta
          name="description"
          content="AI Specialist Agents designed for company workflows. Automate repetitive tasks, empower your team, and accelerate business outcomes."
        />
        <meta
          property="og:title"
          content="Infina AI Work · Specialist Agents for Your Company"
        />
        <meta
          property="og:description"
          content="AI Specialist Agents designed for company workflows. Automate repetitive tasks, empower your team, and accelerate business outcomes."
        />
        <meta property="og:type" content="website" />
      </Helmet>

      <LandingNav activePage="work" ctaLabel="Book a demo" ctaHref="#demo" />
      <WorkHero />
      <WorkCoworkersSection />
      <WorkAgentsSection />

      {/* HIDDEN in source HTML — uncomment to enable */}
      {/* <WorkAgentsHidden /> */}
      {/* <WorkSalesSection /> */}
      {/* <WorkContextAISection /> */}

      <LeadSection source="ai-work-en" sectionId="demo" />
      <LandingFooter />
    </div>
  );
};

export default LandingWork;
