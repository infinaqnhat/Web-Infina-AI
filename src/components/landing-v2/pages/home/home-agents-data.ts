/**
 * Static panel data for the HomeAgents tabbed section.
 * Sourced verbatim from home.html agents-section (lines 4312–4543).
 */

export type TabKey = "inside" | "work" | "personal";

export interface AgentsCard {
  agent?: string;
  titleMain: string;
  titleSub: string;
  contextBadge: string;
  bullets: string[];
}

export interface PersonalRow {
  titleMain: string;
  titleSub: string;
  tags?: string[];
  ctaHref?: string;
  muted?: boolean;
}

export interface WorkAudience {
  label: string;
  cards: (AgentsCard & { wide?: boolean })[];
}

// ── Inside tab ──────────────────────────────────────────────────────────────

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

// ── Personal tab ─────────────────────────────────────────────────────────────

export const personalRows: PersonalRow[] = [
  {
    titleMain: "Finance",
    titleSub: "Personal Specialist",
    tags: [
      "Stock analysis",
      "Market signals",
      "Budgeting",
      "Loans & credit",
      "Insurance",
      "Tax planning",
      "Savings goals",
    ],
    ctaHref: "/personal",
  },
  {
    titleMain: "Lifestyle",
    titleSub: "Personal Specialist",
    tags: ["Trip planning", "Meal planning"],
    ctaHref: "/personal",
  },
  {
    titleMain: "More coming soon",
    titleSub: "New specialists and verticals on the way.",
    muted: true,
  },
];

// ── Work tab ─────────────────────────────────────────────────────────────────

export const workAudiences: WorkAudience[] = [
  {
    label: "For Sales Teams",
    cards: [
      {
        wide: true,
        titleMain: "CRM & Sales Pipeline",
        titleSub: "Specialist Agent",
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
        titleSub: "Specialist Agent",
        contextBadge: "Across your org",
        bullets: [
          "Aligns weekly priorities across team, department, and company goals",
          "Resolves conflicts by understanding where OKRs overlap or clash",
        ],
      },
      {
        titleMain: "Expense Management",
        titleSub: "Specialist Agent",
        contextBadge: "Across your tools and accounts",
        bullets: [
          "Analyzes all spending across SaaS, cloud, credit card, and bank statements",
          "Surfaces ways to cut costs across your accounts",
        ],
      },
      {
        titleMain: "Expertise",
        titleSub: "Specialist Agent",
        contextBadge: "Across your data sources",
        bullets: [
          "Slack threads explained, company context surfaced. Answers ready instantly.",
          "Research pulled from internal data sources and the web in one place",
        ],
      },
      {
        titleMain: "Workflow",
        titleSub: "Specialist Agent",
        contextBadge: "Any repeatable process",
        bullets: [
          "Any repeatable workflow gets fully automated with a dedicated agent",
          "Built and customized to fit exactly what your team needs",
        ],
      },
    ],
  },
];
