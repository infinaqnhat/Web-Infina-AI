import type { RealSaleXIconName } from "./realsalex-icons";

/**
 * Static content for the /realsalex page.
 * Sourced verbatim from Web-Infina-AI/realsalex-v2.html (the canonical page).
 *
 * The page has two audiences behind one tab switch: "buying" (Buyer Agent,
 * Home Concierge) and "listing" (Listing Agent, Property Expert). Copy that
 * differs per tab is keyed by AgentTab so a copy edit on the static page maps
 * to one diff here.
 */

/** Asset root: mirrors the harness public path (see scripts/setup-harness-assets.mjs). */
export const UPLOADS = "/landing-html/uploads";

export type AgentTab = "buying" | "listing";

/** Tab switches in display order. The hero tabs, nav and footer all list Listing first. */
export const AGENT_TAB_OPTIONS: { tab: AgentTab; label: string }[] = [
  { tab: "listing", label: "For Listing Agent" },
  { tab: "buying", label: "For Buyer Agent" },
];

export const LISTING_URL_PLACEHOLDER =
  "https://www.zillow.com/homedetails/8310-Regents-Rd-UNIT-2A-San-Diego-CA-92122/16836646_zpid/";

/** Per-tab CTA: label shared by the nav, sticky and final CTAs; anchor is the hero create box. */
export const tabCta: Record<AgentTab, { label: string; anchorId: string }> = {
  buying: { label: "Create Home Concierge →", anchorId: "hero-create" },
  listing: { label: "Create Property Expert →", anchorId: "hero-create-qr" },
};

/** A heading whose tail is the animated gradient `.accent` span. */
export interface AccentHeading {
  title: string;
  accent: string;
}

/* ── Today vs With … comparison ───────────────────────────────────────────── */

export interface CompareCopy {
  eyebrow: string;
  today: { head: string; sub: string };
  advisor: { head: string; sub: string };
  rows: { today: string; advisor: string }[];
  quote: string;
}

export const compareCopy: Record<AgentTab, CompareCopy> = {
  buying: {
    eyebrow: "The same buyer, two experiences",
    today: { head: "Today", sub: "Your buyer is on their own" },
    advisor: { head: "With Home Concierge", sub: "Your buyer has you" },
    rows: [
      { today: "Agent sends a listing link", advisor: "Agent sends an advisor" },
      {
        today: "Buyer browses Zillow, searches elsewhere, asks ChatGPT or Claude",
        advisor: "Buyer asks everything in one place",
      },
      {
        today:
          "Often, buyer connects with another agent. If buyer eventually comes back, they need to brief you all the details",
        advisor: "Agent stays connected to the conversation",
      },
    ],
    quote: "You remain the trusted advisor even when you're not available.",
  },
  listing: {
    eyebrow: "The same yard sign, two outcomes",
    today: { head: "Today", sub: "Buyers drive by and guess" },
    advisor: { head: "With Property Expert", sub: "Buyers get real answers" },
    rows: [
      { today: "Yard sign shows a phone number", advisor: "Yard sign links to a Property Expert" },
      {
        today: "Buyers look up the property on a portal",
        advisor: "Buyers get all their questions answered by Property Expert",
      },
      {
        today:
          "You wouldn't know who and how many were interested and what made each lose interest in the property",
        advisor: "Property Expert keeps them engaged and flags you when they're ready to act",
      },
    ],
    quote: "Every listing works for you even when you're not available.",
  },
};

/* ── Three-card sections ──────────────────────────────────────────────────── */

export interface ThreeCardSectionCopy extends AccentHeading {
  eyebrow?: string;
  sub?: string;
  cards: { title: string; text: string }[];
}

export const listingReasons: ThreeCardSectionCopy = {
  title: "Three reasons agents ",
  accent: "send a Property Expert.",
  cards: [
    {
      title: "Always available.",
      text: "Answer every buyer 24/7, even at night, on weekends, or while you're with another client.",
    },
    {
      title: "Moves buyers forward.",
      text: "Help buyers request disclosures, book a showing, or compare the property, not just answer questions.",
    },
    {
      title: "Helps you win listings.",
      text: "Show sellers their home gets its own 24/7 expert, not just another listing page.",
    },
  ],
};

export const buyingNextSteps: ThreeCardSectionCopy = {
  eyebrow: "Before the first showing",
  title: "Give every question ",
  accent: "a next step.",
  sub: "As buyers ask about 123 Main Street, you learn what matters to them, and when to step in.",
  cards: [
    {
      title: "Make replying easy.",
      text: "Start with one approachable question about the property. Buyers can answer by text or voice, at their own pace.",
    },
    {
      title: "Discover needs and readiness.",
      text: "As they ask about this home, learn their must-haves, budget comfort, and timing. Unanswered questions stay visible so you know what to ask next.",
    },
    {
      title: "Match the next step to the buyer.",
      text: "Help early browsers clarify what they want, and connect ready buyers to a tour or a call.",
    },
  ],
};

/* ── Data trust (buyer agent) ─────────────────────────────────────────────── */

export const trustPoints = [
  "The advisor cites its sources.",
  "It does not invent answers when information is unavailable.",
  "You control the information supplied to the advisor.",
  "Your relationship data is not sold.",
  "You can delete your data at any time.",
];

/* ── Buyer-intent staircase (listing agent) ───────────────────────────────── */

export const intentSteps: { count: string; stage: string; example: string; icon: RealSaleXIconName }[] = [
  { count: "42 buyers", stage: "Exploration", example: "\"When was the home built?\"", icon: "search" },
  { count: "27 buyers", stage: "Intent", example: "\"How does this compare with nearby homes?\"", icon: "house" },
  {
    count: "14 buyers",
    stage: "Negotiation",
    example: "\"What does the disclosure say about foundation work?\"",
    icon: "doc",
  },
  {
    count: "8 buyers",
    stage: "Transaction",
    example:
      "\"When are offers due?\" · \"Can I tour tomorrow?\" · \"What's the inspection deadline?\" · \"When do we get the keys?\"",
    icon: "calendar",
  },
];

/* ── Testimonials ─────────────────────────────────────────────────────────── */

export const testimonials = [
  {
    quote: "\"I sent this instead of a Zillow link and my buyer asked 14 questions that night.\"",
    name: "Dana Whitfield",
    meta: "Compass · Austin, TX · $31M closed in the last 12 months",
    avatar: `${UPLOADS}/testi-dana.jpg`,
  },
  {
    quote: "\"My clients stopped calling at 9 PM with questions I had already answered twice.\"",
    name: "Marcus Ellery",
    meta: "Coldwell Banker · Nashville, TN · $18M closed in the last 12 months",
    avatar: `${UPLOADS}/testi-marcus.jpg`,
  },
  {
    quote:
      "\"The questions it got asked told me exactly what to negotiate on before I called the listing agent.\"",
    name: "Priya Raman",
    meta: "Douglas Elliman · Denver, CO · $44M closed in the last 12 months",
    avatar: `${UPLOADS}/testi-priya.jpg`,
  },
];

/* ── Final CTA ────────────────────────────────────────────────────────────── */

export const finalCtaCopy: Record<AgentTab, AccentHeading & { line: string; note: string }> = {
  buying: {
    title: "Your next client doesn't need",
    accent: "another listing link.",
    line: "Give them an advisor they can talk to.",
    note: "No signup required to see your first advisor.",
  },
  listing: {
    title: "Your next listing doesn't need",
    accent: "another static page.",
    line: "Property Expert doesn't replace you. It extends you.",
    note: "No CRM connection. No complicated setup. Start with one listing.",
  },
};
