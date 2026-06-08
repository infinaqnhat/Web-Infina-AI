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

export interface WorkAudience {
  label: string;
  cards: (AgentsCard & { wide?: boolean })[];
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

export const workAudiences: WorkAudience[] = [
  {
    label: "For Sales Teams",
    cards: [
      {
        wide: true,
        titleMain: "CRM & Sales Pipeline",
        contextBadge: "Inside your CRM",
        bullets: [
          "Works alongside your existing CRM and tools. No migration required.",
          "Handles CRM updates, follow-up emails, and task logging automatically",
          "Pre-configured for your industry: real estate, insurance, finance, and more",
          "Accessible via Slack, WhatsApp, web, or your own app",
        ],
      },
    ],
  },
  {
    label: "For Operations & Company",
    cards: [
      {
        titleMain: "Focus & Alignment",
        contextBadge: "Across your organization",
        bullets: [
          "Aligns weekly priorities across team, department, and company goals",
          "Resolves conflicts by understanding where OKRs overlap or clash",
        ],
      },
      {
        titleMain: "Expense Management",
        contextBadge: "Across your tools and accounts",
        bullets: [
          "Analyzes all spending across SaaS, cloud, credit card, and bank statements",
          "Surfaces ways to cut costs across your accounts",
        ],
      },
      {
        titleMain: "Expertise",
        contextBadge: "Across your data sources",
        bullets: [
          "Slack threads explained, company context surfaced. Answers ready instantly.",
          "Research pulled from internal data sources and the web in one place",
        ],
      },
      {
        titleMain: "Workflow",
        contextBadge: "Any repeatable process",
        bullets: [
          "Any repeatable workflow gets fully automated with a dedicated agent",
          "Built and customized to fit exactly what your team needs",
        ],
      },
    ],
  },
];
