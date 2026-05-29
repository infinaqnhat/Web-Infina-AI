import { useEffect } from "react";
import { Helmet } from "react-helmet-async";
import { useLocation } from "react-router-dom";
// landing.css must load BEFORE landing-home.css so its .landing-root *
// universal reset (margin:0; padding:0) cannot override unscoped .hero,
// .section, etc. rules in landing-home.css (equal specificity → source
// order wins). Other landing pages avoid this by scoping selectors under
// .{page}-page, which gives them higher specificity than the reset.
import "@/styles/landing.css";
import "@/styles/landing-home.css";
import LandingNav from "@/components/landing-v2/layout/LandingNav";
import LandingFooter from "@/components/landing-v2/layout/LandingFooter";
import LeadSection from "@/components/landing-v2/sections/LeadSection";
import HomeHero from "@/components/landing-v2/pages/home/HomeHero";
import HomePartners from "@/components/landing-v2/pages/home/HomePartners";
import HomeProducts from "@/components/landing-v2/pages/home/HomeProducts";
import HomeAgents from "@/components/landing-v2/pages/home/HomeAgents";
import HomeSpeedBanner from "@/components/landing-v2/pages/home/HomeSpeedBanner";
import HomeCoreSection from "@/components/landing-v2/pages/home/HomeCoreSection";
import HomeWhyInfina from "@/components/landing-v2/pages/home/HomeWhyInfina";

/**
 * LandingHome — native React port of home.html.
 * Replaces the former iframe wrapper. Class names are preserved verbatim
 * so all landing.css selectors continue to work unchanged.
 *
 * Scripts converted:
 *  Script 1 (L4770) — lead form submit + custom combos → LeadSection (controlled state + fetch)
 *  Script 2 (L5039) — Rubik cube builder for #hv-cube — element absent from body HTML; omitted (no-op)
 *  Script 3 (L5066) — product-order tweaks panel (editor tool) — intentionally omitted (internal tool only)
 *  Script 4 (L5214) — mobile nav toggle → LandingNav (useState open/close)
 *
 * Hash anchor support: on location.hash change, smoothly scroll to the
 * matching element (handles #products, #core, #demo, #why-infina links).
 *
 * Render order mirrors home.html section order:
 *  LandingNav → HomeHero → HomePartners → HomeProducts → HomeAgents
 *  → HomeSpeedBanner → HomeCoreSection → HomeWhyInfina → LeadSection → LandingFooter
 *
 * Note: HomeSpeedBanner and HomeWhyInfina are inside HTML comments in home.html
 * (hidden, preserved for reuse). They are rendered here per spec.
 */
const LandingHome = () => {
  const { hash } = useLocation();

  // Hash anchor scroll — replaces html { scroll-behavior: smooth } for SPA navigation
  useEffect(() => {
    if (!hash) return;
    const id = hash.replace("#", "");
    const el = document.getElementById(id);
    if (el) {
      // Small delay to let React finish painting before scrolling
      const t = setTimeout(() => el.scrollIntoView({ behavior: "smooth" }), 50);
      return () => clearTimeout(t);
    }
  }, [hash]);

  return (
    <>
      <Helmet>
        <title>Infina AI — Specialist AI Agents That Get The Job Done</title>
        <meta
          name="description"
          content="Infina develops AI Specialist Agents that get the job done for people, products, and companies."
        />
        <meta
          property="og:title"
          content="Infina AI — Specialist AI Agents That Get The Job Done"
        />
        <meta
          property="og:description"
          content="Infina develops AI Specialist Agents that get the job done for people, products, and companies."
        />
        <meta property="og:type" content="website" />
      </Helmet>

      <LandingNav activePage="home" ctaLabel="Book a demo" ctaHref="#demo" />
      <HomeHero />
      <HomePartners />
      <HomeProducts />
      <HomeAgents />
      <HomeSpeedBanner />
      <HomeCoreSection />
      <HomeWhyInfina />
      <LeadSection source="infina-ai-main-v1" sectionId="demo" />
      <LandingFooter />
    </>
  );
};

export default LandingHome;
