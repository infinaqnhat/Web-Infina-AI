import type { ReactNode } from "react";

/**
 * Static content for the /realsalex page.
 * Sourced verbatim from Web-Infina-AI/realsalex.html (the canonical static page).
 *
 * Copy lives here rather than inline in the section components so a copy edit
 * on the static page maps to one diff here. Entries that carry inline SVG or
 * mixed markup are typed as ReactNode.
 */

/** Asset root — mirrors the harness/PFA public path (see scripts/setup-harness-assets.mjs). */
export const UPLOADS = "/landing-html/uploads";

/* ── Hero ─────────────────────────────────────────────────────────────────── */

export const heroStats = [
  { value: "2×", label: "Selling power" },
  { value: "24/7", label: "Active nurturing" },
  { value: "30% → 90%", label: "Follow-up rate" },
];

/* ── Problem ──────────────────────────────────────────────────────────────── */

export const problemStats = [
  { stat: "40–50%", text: "of leads are never followed up" },
  { stat: "~9%", text: "get a reply within 5 minutes, the average agent takes 15 hours" },
  { stat: "~3 mo", text: "average residential buyer journey, mostly silent" },
];

/* ── Journey (4 stages, one connected arrow) ──────────────────────────────── */

export interface JourneyStage {
  num: string;
  name: string;
  sub: string;
  image: string;
  imageAlt: string;
  chipIcon: ReactNode;
  chipText: ReactNode;
}

export const journeyStages: JourneyStage[] = [
  {
    num: "01",
    name: "Explore",
    sub: "Buyer begins their journey",
    image: `${UPLOADS}/realsalex-agent1.png`,
    imageAlt: "A home buyer exploring listings at home",
    chipIcon: (
      <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <rect x="4" y="8" width="16" height="11" rx="3" />
        <path d="M12 4v4M9 13v.01M15 13v.01" />
      </svg>
    ),
    chipText: <>Ask me anything about homes &amp; financing</>,
  },
  {
    num: "02",
    name: "Compare",
    sub: "Buyer evaluates options",
    image: `${UPLOADS}/stage-compare.png`,
    imageAlt: "A buyer comparing two listings on a laptop",
    chipIcon: (
      <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M4 20V11M10 20V5M16 20v-6M21 20H3" />
      </svg>
    ),
    chipText: (
      <>
        Scoring Buyer Intent: 86 · <b className="hi">High</b>
      </>
    ),
  },
  {
    num: "03",
    name: "You step in",
    sub: "You get the right signal to act",
    image: `${UPLOADS}/stage-david.png`,
    imageAlt: "Agent David reviewing buyer signals",
    chipIcon: (
      <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M22 2 11 13M22 2l-7 20-4-9-9-4z" />
      </svg>
    ),
    chipText: <>Next best action: Send home viewing schedule</>,
  },
  {
    num: "04",
    name: "Close",
    sub: "Deal is closed successfully",
    image: `${UPLOADS}/stage-close.png`,
    imageAlt: "A couple receiving keys from their agent",
    chipIcon: (
      <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M20 6 9 17l-5-5" />
      </svg>
    ),
    chipText: <>Deal closed · happy homeowner</>,
  },
];

/** The three agents behind the journey. */
export const journeyAgents: { icon: ReactNode; title: string; text: ReactNode }[] = [
  {
    icon: (
      <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <rect x="3" y="8" width="18" height="12" rx="3" />
        <path d="M12 4v4M8 2v2M16 2v2" />
        <circle cx="9" cy="14" r="1" />
        <circle cx="15" cy="14" r="1" />
      </svg>
    ),
    title: "24/7 Buyer Companion",
    text: (
      <>
        Answers property, legal &amp; finance questions 24/7 and guides the buyer&apos;s research
        inside their own Deal Room.
      </>
    ),
  },
  {
    icon: (
      <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <circle cx="6" cy="12" r="2.5" />
        <circle cx="18" cy="6" r="2.5" />
        <circle cx="18" cy="18" r="2.5" />
        <path d="M8.2 10.8 15.6 7.2M8.2 13.2 15.6 16.8" />
      </svg>
    ),
    title: "Smart Pipeline + Intent Signals",
    text: <>Captures behavior, scores buyer intent, and hands you the signal and the next best action.</>,
  },
  {
    icon: (
      <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M22 2 11 13M22 2l-7 20-4-9-9-4z" />
      </svg>
    ),
    title: "Your Closing Companion",
    text: <>Drafts the message, recommends the next step, and helps you close the deal.</>,
  },
];

/* ── Showcase ─────────────────────────────────────────────────────────────── */

export interface ShowcaseBlock {
  tag: string;
  heading: ReactNode;
  bullets: ReactNode[];
  frameUrl: string;
  image: string;
  imageMobile: string;
  imageAlt: string;
}

export const showcaseBlocks: ShowcaseBlock[] = [
  {
    tag: "What the buyer gets",
    heading: "A private Deal Room, with a smart companion beside you.",
    bullets: [
      "A private page of the exact units discussed",
      <>Ask price, legal &amp; financing, 24/7</>,
      "Compare units right inside the chat",
      "You and your companion, in one conversation",
    ],
    frameUrl: "realsale.companion/deal-room",
    image: `${UPLOADS}/realsalex-buyer.png`,
    imageMobile: `${UPLOADS}/realsalex-buyer-mobile.png`,
    imageAlt: "Real Sale X Deal Room, units and a live companion chat beside you",
  },
  {
    tag: "What you run",
    heading: "Every buyer, scored by intent, in one dashboard.",
    bullets: [
      <>Every customer &amp; Deal Room in one place</>,
      "Activity + intent score per buyer",
      <>Instant report &amp; recommended next step</>,
      <>Runs over SMS &amp; WhatsApp, synced to your CRM</>,
    ],
    frameUrl: "realsale.companion/pipeline",
    image: `${UPLOADS}/realsalex-agent.png`,
    imageMobile: `${UPLOADS}/realsalex-agent-mobile.png`,
    imageAlt: "Real Sale X agent dashboard, intent-scored pipeline and drafted messages",
  },
];

/* ── Intent-signal engine ─────────────────────────────────────────────────── */

export const engineCards: { k: string; text: ReactNode }[] = [
  { k: "READS", text: <>Page &amp; unit views, dwell time, and the questions asked: price, legal, finance.</> },
  { k: "SCORES", text: "Turns behavior into a readiness score and ranks who is worth acting on right now." },
  { k: "TRIGGERS", text: "Alerts the right agent instantly, and drafts the message to send." },
];

export const engineLoopSteps = [
  "Buyers interact",
  "Intent + outcome logged",
  "Companion gets smarter",
  "Agents close more",
];

/* ── Results ──────────────────────────────────────────────────────────────── */

export interface ResultCard {
  icon: ReactNode;
  stat: string;
  label: string;
  desc: string;
}

export const resultCards: ResultCard[] = [
  {
    icon: (
      <svg viewBox="0 0 24 24" fill="none">
        <path d="M3 4h18l-7 8v6l-4 2v-8L3 4z" stroke="#1863dc" strokeWidth="1.8" strokeLinejoin="round" />
      </svg>
    ),
    stat: "+10–15%",
    label: "Conversion rate",
    desc: "Convert more high-intent leads into clients.",
  },
  {
    icon: (
      <svg viewBox="0 0 24 24" fill="none">
        <circle cx="12" cy="12" r="9" stroke="#1863dc" strokeWidth="1.8" />
        <path d="M12 7v5l3.5 2" stroke="#1863dc" strokeWidth="1.8" strokeLinecap="round" />
      </svg>
    ),
    stat: "−15–20%",
    label: "Sales-cycle time",
    desc: "Close deals faster with a smarter pipeline.",
  },
  {
    icon: (
      <svg viewBox="0 0 24 24" fill="none">
        <circle cx="12" cy="8" r="4" stroke="#1863dc" strokeWidth="1.8" />
        <path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7" stroke="#1863dc" strokeWidth="1.8" strokeLinecap="round" />
        <path d="M9 16.5l2 2 3-3" stroke="#1863dc" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    ),
    stat: "30% → 90%",
    label: "Qualified-buyer follow-up",
    desc: "Consistent, timely follow-ups that actually connect.",
  },
  {
    icon: (
      <svg viewBox="0 0 24 24" fill="none">
        <path d="M6 3h9l3 3v15H6V3z" stroke="#1863dc" strokeWidth="1.8" strokeLinejoin="round" />
        <path d="M9 12l2 2 4-4" stroke="#1863dc" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    ),
    stat: "−50%",
    label: "Time on admin",
    desc: "Automate the busywork that slows you down.",
  },
];

/* ── FAQ ──────────────────────────────────────────────────────────────────── */

export const faqItems: { q: string; a: ReactNode }[] = [
  {
    q: "Will this replace me?",
    a: "No. Real Sale X does the repetitive follow-up and admin so you focus on relationships and closing. Every hot lead stays yours to act on, with the context to close it.",
  },
  {
    q: "Does it replace my CRM?",
    a: (
      <>
        No, Real Sale X integrates with your CRM &amp; MLS and complements them. It adds the live
        intent layer they&apos;re missing.
      </>
    ),
  },
  {
    q: "How fast can we start?",
    a: "Start with one small sales team on live deals, no commitment beyond that. The results make the decision.",
  },
  {
    q: "Where does it talk to buyers?",
    a: "Right inside the Deal Room, where you and your buyer share one conversation. Buyers can also reply by SMS or WhatsApp, and everything stays in sync, no new portal to log into.",
  },
  {
    q: "Who owns the data?",
    a: "You do. Every conversation becomes structured, company-owned buyer-intent data that stays with you.",
  },
  {
    q: "Is it secure?",
    a: "Enterprise-grade security and access controls; we work with your IT, Security, and Legal teams on deployment and compliance.",
  },
];
