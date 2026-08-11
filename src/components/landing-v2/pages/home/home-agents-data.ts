/**
 * Static panel data for the product-accordion specialist grids.
 * Sourced verbatim from home.html product panels (#tab-inside / #tab-work / #tab-personal).
 */

export type TabKey = "inside" | "work" | "personal";

export interface AgentsCard {
  agent?: string;
  titleMain: string;
  /** Hidden via CSS (.agents-title-sub{display:none}); kept only where the HTML markup has it. */
  titleSub?: string;
  contextBadge: string;
  bullets: string[];
}

export interface PersonalRow {
  titleMain: string;
  bullets?: string[];
  /** "More features coming." line under the bullets. */
  moreText?: string;
  ctaHref?: string;
  muted?: boolean;
  /** Sub text for the muted "More coming soon" row. */
  subText?: string;
}

export interface WorkSpecialist {
  groupLabel: string;
  titleMain: string;
  tagline: string;
  bullets: string[];
  exploreLabel: string;
}

// ── Inside panel ──────────────────────────────────────────────────────────────

export const insideCards: AgentsCard[] = [
  {
    agent: "stock",
    titleMain: "Stock",
    titleSub: "Specialist Agent",
    contextBadge: "Inside stock trading apps",
    bullets: [
      "Market insights tailored to each user's holdings",
      "Surfaces risks and opportunities in their portfolio",
      "Alerts on moves that matter, nothing else",
    ],
  },
  {
    agent: "wealth",
    titleMain: "Wealth Management",
    titleSub: "Specialist Agent",
    contextBadge: "Inside fund management apps/web",
    bullets: [
      "Fund questions answered instantly",
      "Investing plans built around real goals",
      "Asset mix matched to risk profile and timeline",
      "Flags when to rebalance, and why",
    ],
  },
  {
    agent: "personal",
    titleMain: "Personal Finance",
    titleSub: "Specialist Agent",
    contextBadge: "Inside banking/e-wallet apps",
    bullets: [
      "Matches users to products that fit their situation",
      "Shows where money goes and where to improve",
      "Clarifies loan options and credit improvement steps",
      "Builds financial confidence in plain language",
    ],
  },
  {
    agent: "insurance",
    titleMain: "Insurance",
    titleSub: "Specialist Agent",
    contextBadge: "Inside insurance apps/web",
    bullets: [
      "Finds coverage that fits, not just what's available",
      "Answers policy questions any time, in plain language",
      "Guides users through claims to get what they're entitled to",
    ],
  },
];

// ── Personal panel ───────────────────────────────────────────────────────────

export const personalRows: PersonalRow[] = [
  {
    titleMain: "Finance",
    bullets: [
      "Answers questions about your money in plain language",
      "Tracks your budget and flags where to cut back",
      "Guides you on loans, insurance, tax planning, and more",
    ],
    moreText: "More features coming.",
    ctaHref: "/personal",
  },
  {
    titleMain: "Lifestyle",
    bullets: [
      "Plans trips around your preferences and budget",
      "Builds weekly meal plans with recipes and shopping lists",
    ],
    moreText: "More features coming.",
    ctaHref: "/personal",
  },
  {
    titleMain: "More coming soon",
    muted: true,
    subText: "New specialists and verticals on the way.",
  },
];

// ── Work panel ─────────────────────────────────────────────────────────────────

/** Single "Your AI workforce" audience — 3 specialists, synced with work.html. */
export const workAudienceLabel = "Your AI workforce";

export const workSpecialists: WorkSpecialist[] = [
  {
    groupLabel: "Front Office · Customer-facing growth",
    titleMain: "AI SalesX",
    tagline: "AI sells. You show up to close.",
    bullets: [
      "Live AI brochure built per prospect, mid-conversation",
      "WhatsApp agent qualifies leads & books meetings 24/7",
      "Briefs you before you step in — leads arrive warm",
    ],
    exploreLabel: "Explore AI SalesX →",
  },
  {
    groupLabel: "Leadership · Decisions & intelligence",
    titleMain: "AI ManageX",
    tagline: "Decide faster.",
    bullets: [
      "OKRs aligned, conflicts flagged early",
      "Ask any business question, get an instant answer",
      "Reports & emails drafted on command",
    ],
    exploreLabel: "Explore AI ManageX →",
  },
  {
    groupLabel: "Back Office · Operations & efficiency",
    titleMain: "AI OperateX",
    tagline: "The work runs itself.",
    bullets: [
      "Repeatable workflows fully automated",
      "Procurement & approvals handled end-to-end",
      "Full spend visibility across every account",
    ],
    exploreLabel: "Explore AI OperateX →",
  },
];
