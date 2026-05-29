import { useEffect } from "react";
import { Helmet } from "react-helmet-async";
import { useLocation } from "react-router-dom";
import "@/styles/landing.css";
import "@/styles/landing-personal.css";
import LandingNav from "@/components/landing-v2/layout/LandingNav";
import LandingFooter from "@/components/landing-v2/layout/LandingFooter";
import PersonalHero from "@/components/landing-v2/pages/personal/PersonalHero";

/**
 * LandingPersonal — native React port of personal.html.
 * Class names preserved verbatim so landing-personal.css selectors apply.
 *
 * Page is hero-only (visible section).
 * Jobs, Usecases, and CTA sections are hidden in source HTML (style="display:none").
 * They are ported as valid components and left commented below — uncomment to enable.
 *
 * LeadSection: absent — personal.html contains no <section class="lead-section"> (verified by grep).
 *
 * Scripts converted:
 *  Typewriter cycling prompts → PersonalHero (useEffect + setTimeout stepper)
 *  Mock Chat → PersonalMockChat + personal-mock-chat-data.ts
 *  Job Picker → PersonalJobPicker + personal-mock-chat-data.ts
 *  planStepper / Slack demo / waitlist modal — dead code in source HTML; omitted.
 *
 * Hash anchor support: location.hash → smooth scroll to matching element id.
 *
 * Render order mirrors personal.html section order:
 *  LandingNav → PersonalHero
 *  → [HIDDEN] PersonalJobs → PersonalUsecases → PersonalCta
 *  → LandingFooter
 */
const LandingPersonal = () => {
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
    <div className="personal-page">
      <Helmet>
        <title>Infina AI Personal · AI Specialists for every decision</title>
        <meta
          name="description"
          content="AI Specialist Agents for personal finance — stock analysis, investment advice, budget planning and more."
        />
        <meta
          property="og:title"
          content="Infina AI Personal · AI Specialists for every decision"
        />
        <meta
          property="og:description"
          content="AI Specialist Agents for personal finance — stock analysis, investment advice, budget planning and more."
        />
        <meta property="og:type" content="website" />
      </Helmet>

      <LandingNav
        activePage="personal"
        ctaLabel="Chat with AI"
        ctaHref="https://infina.ai"
        ctaExternal
      />
      <PersonalHero />

      {/* HIDDEN in source HTML — uncomment to enable */}
      {/* <PersonalJobs /> */}
      {/* <PersonalUsecases /> */}
      {/* <PersonalCta /> */}

      <LandingFooter />
    </div>
  );
};

export default LandingPersonal;
