import { useEffect } from "react";
import { Helmet } from "react-helmet-async";
import { useLocation } from "react-router-dom";
import "@/styles/landing-about.css";
import LandingNav from "@/components/landing-v2/layout/LandingNav";
import LandingFooter from "@/components/landing-v2/layout/LandingFooter";
import LeadSection from "@/components/landing-v2/sections/LeadSection";
import AboutHero from "@/components/landing-v2/pages/about/AboutHero";
import AboutStorySection from "@/components/landing-v2/pages/about/AboutStorySection";
import AboutMissionSection from "@/components/landing-v2/pages/about/AboutMissionSection";
import AboutDifferentSection from "@/components/landing-v2/pages/about/AboutDifferentSection";
import AboutCtaSection from "@/components/landing-v2/pages/about/AboutCtaSection";

/**
 * LandingAbout — native React port of about.html.
 * Class names preserved verbatim so landing-about.css selectors apply.
 *
 * Render order mirrors about.html DOM:
 *   LandingNav → AboutHero → AboutStorySection → AboutMissionSection
 *   → AboutDifferentSection → AboutCtaSection → LeadSection → LandingFooter
 *
 * Hash anchor support: location.hash change → smooth scroll to matching id.
 * Handles #lead-form links from nav CTA and hero/CTA buttons.
 *
 * Scoped styles: all selectors wrapped under .about-page in landing-about.css
 * to prevent bleed with other landing pages sharing the same DOM.
 */
const LandingAbout = () => {
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
    <div className="about-page">
      <Helmet>
        <title>About Us - Infina AI · We Built the AI First. Then We Made It Available to You.</title>
        <meta
          name="description"
          content="Infina AI started as a production personal finance chatbot in Vietnam. Now we embed that same AI into financial institutions worldwide."
        />
        <meta
          property="og:title"
          content="About Us - Infina AI · We Built the AI First. Then We Made It Available to You."
        />
        <meta
          property="og:description"
          content="Infina AI started as a production personal finance chatbot in Vietnam. Now we embed that same AI into financial institutions worldwide."
        />
        <meta property="og:type" content="website" />
      </Helmet>

      <LandingNav activePage="about" ctaLabel="Book a demo" ctaHref="#lead-form" />
      <AboutHero />
      <AboutStorySection />
      <AboutMissionSection />
      <AboutDifferentSection />
      <AboutCtaSection />
      <LeadSection source="infina-ai-about-us" sectionId="lead-form" />
      <LandingFooter />
    </div>
  );
};

export default LandingAbout;
