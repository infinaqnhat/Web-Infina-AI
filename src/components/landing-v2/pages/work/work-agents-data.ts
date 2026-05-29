/**
 * Static data for WorkAgentsSection — specialists-grid layout.
 * Sourced verbatim from Web-Infina-AI/work.html L1519–1634.
 *
 * Divergences from infina-pfa-80389 reference:
 *  - "1 thing" titleMain rendered with inline color on "1 thing" text (see WorkAgentsSection)
 *  - "Explore 1 thing →" link points to "focus-alignment.html" (HTML relative href),
 *    stored here as-is; WorkAgentsSection routes via <a href> not <Link>.
 *  - crm-video-wrap (toggle + collapsible iframe) is a runtime concern — data-only here,
 *    rendered in WorkAgentsSection with state.
 */

export type AgentBullet = { text: string };

export type AgentCard = {
  titleMain: string;
  /** optional: "1 thing" prefix rendered with muted color — signal via hasMutedPrefix */
  hasMutedPrefix?: boolean;
  titleSub: string;
  contextBadge: string;
  bullets: AgentBullet[];
  exploreLink?: string;
  exploreLinkText?: string;
  /** row layout (horizontal) instead of column layout */
  isRow?: boolean;
};

export type AgentGroup = {
  audienceLabel: string;
  cards: AgentCard[];
  /** render cards in 4-col grid */
  gridFour?: boolean;
  /** show CRM video toggle after the cards */
  showCrmVideo?: boolean;
};

export const AGENT_GROUPS: AgentGroup[] = [
  {
    // work.html L1533–1562
    audienceLabel: "For Sales Teams",
    showCrmVideo: true,
    cards: [
      {
        titleMain: "CRM & Sales Pipeline",
        titleSub: "AI Specialist",
        contextBadge: "Inside your CRM",
        bullets: [
          { text: "Logs updates, sends follow-ups, and tracks tasks. Automatically." },
          { text: "Works inside your existing CRM. No migration, no disruption." },
          { text: "Pre-configured for real estate, insurance, finance, and more." },
        ],
        isRow: true,
      },
    ],
    gridFour: false,
  },
  {
    // work.html L1564–1629
    audienceLabel: "For Operations & Company",
    cards: [
      {
        titleMain: "1 thing | Focus & Alignment",
        hasMutedPrefix: true,
        titleSub: "AI Specialist",
        contextBadge: "Across your org",
        bullets: [
          { text: "One priority per person, aligned to team and company goals." },
          { text: "Catches OKR conflicts before they slow you down." },
        ],
        exploreLink: "focus-alignment.html",
        exploreLinkText: "Explore 1 thing →",
      },
      {
        titleMain: "Expense Management",
        titleSub: "AI Specialist",
        contextBadge: "Across your tools and accounts",
        bullets: [
          { text: "Full spend visibility: SaaS, cloud, cards, and bank in one view." },
          { text: "Surfaces where to cut, and exactly what to do about it." },
        ],
      },
      {
        titleMain: "Expertise",
        titleSub: "AI Specialist",
        contextBadge: "Across your data sources",
        bullets: [
          { text: "Instant answers from your data, docs, and Slack threads." },
          { text: "No more digging. Context surfaces automatically." },
        ],
      },
      {
        titleMain: "Workflow",
        titleSub: "AI Specialist",
        contextBadge: "Any repeatable process",
        bullets: [
          { text: "Any repeatable process, fully automated." },
          { text: "Built to your exact workflow, not a generic template." },
        ],
      },
    ],
    gridFour: true,
  },
];
