import { useEffect } from "react";
import { Helmet } from "react-helmet-async";
import { useLocation } from "react-router-dom";
import "@/styles/landing-focus-alignment.css";
import LandingNav from "@/components/landing-v2/layout/LandingNav";
import LandingFooter from "@/components/landing-v2/layout/LandingFooter";
import FocusHero from "@/components/landing-v2/pages/focus-alignment/FocusHero";
import FocusContextChat from "@/components/landing-v2/pages/focus-alignment/FocusContextChat";
import FocusTeamSection from "@/components/landing-v2/pages/focus-alignment/FocusTeamSection";
import FocusIntegrations from "@/components/landing-v2/pages/focus-alignment/FocusIntegrations";
import FocusDemoBand from "@/components/landing-v2/pages/focus-alignment/FocusDemoBand";

/**
 * LandingFocusAlignment — source mirror of Web-Infina-AI/focus-alignment.html.
 * Route: /focus-alignment (mounted under LandingLayout).
 *
 * Section render order (matches HTML source):
 *   FocusHero → FocusContextChat → FocusTeamSection → FocusIntegrations → FocusDemoBand
 *
 * Lead-section decision: HTML uses an inline-styled custom section (id="demo", no .lead-section class).
 * FocusDemoBand mirrors that section verbatim using .demo-band CSS class abstraction.
 * DIFF FROM HTML: HTML uses inline-styled custom lead (id="demo"), not shared .lead-section component.
 *
 * Hash anchor support: location.hash change → smooth scroll to matching id.
 */
const LandingFocusAlignment = () => {
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
    <div className="focus-alignment-page">
      <Helmet>
        <title>Focus &amp; Alignment · Infina AI Work</title>
        <meta
          name="description"
          content="The AI chief of staff for teams under 50. Connect your priorities, key results, and daily reports in one AI chat."
        />
        <meta
          property="og:title"
          content="Focus &amp; Alignment · Infina AI Work"
        />
        <meta
          property="og:description"
          content="The AI chief of staff for teams under 50. Connect your priorities, key results, and daily reports in one AI chat."
        />
        <meta property="og:type" content="website" />
      </Helmet>

      <LandingNav
        activePage="focus-alignment"
        ctaLabel="Start chatting"
        ctaHref="#demo"
      />
      <FocusHero />
      <FocusContextChat />
      <FocusTeamSection />
      <FocusIntegrations />
      {/* DIFF FROM HTML: HTML uses inline-styled <section style="..." id="demo">.
          FocusDemoBand abstracts those inline styles into .demo-band CSS class
          while preserving identical markup structure and id="demo" anchor. */}
      <FocusDemoBand />
      <LandingFooter />
    </div>
  );
};

export default LandingFocusAlignment;
