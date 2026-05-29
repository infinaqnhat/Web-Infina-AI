/**
 * Scenario + feature-tab data for WorkCoworkersSection.
 * Panel content ported verbatim from Web-Infina-AI/work.html L1018–1184.
 * Scenario 1: finance-team / Q4 budget / Michael T.
 * Scenario 2 (Panel 2): "Resolved this week" rendered white in React data;
 *   HTML uses inline color:#22c55e — noted divergence, data structure matches.
 */

export type CardItem = { label: string; value: string; highlight?: boolean };
export type CardCheck = { text: string; done: boolean; warning?: boolean };

export type Scenario = {
  channel: string;
  time: string;
  user: string;
  userInitials: string;
  userColor: string;
  userMessage: React.ReactNode;
  botName: string;
  botResponse: React.ReactNode;
  cardLabel: string;
  cardItems?: CardItem[];
  cardWarning?: boolean;
  cardTitle?: string;
  cardDesc?: string;
  cardChecks?: CardCheck[];
  buttons: [string, string];
};

export const SCENARIOS: Scenario[] = [
  {
    // Panel 0: Real-time Support — work.html L1040–1086
    channel: "support-queries",
    time: "10:22 AM",
    user: "Sarah L.",
    userInitials: "SL",
    userColor: "#1863dc",
    userMessage: (
      <>
        <span className="slack-mention">@Infina AI</span> What's the tax impact
        if I sell my AAPL position today?
      </>
    ),
    botName: "Infina AI",
    botResponse: (
      <>
        Selling today realises a{" "}
        <span style={{ color: "#22c55e", fontWeight: 600 }}>
          long-term gain of $4,280
        </span>
        .
      </>
    ),
    cardLabel: "TAX SUMMARY",
    cardItems: [
      { label: "Cost basis", value: "$12,400" },
      { label: "Proceeds", value: "$16,680" },
      { label: "Est. tax (15%)", value: "$642", highlight: true },
    ],
    buttons: ["See full analysis", "Dismiss"],
  },
  {
    // Panel 1: Instant Solutions — work.html L1088–1135
    channel: "finance-team",
    time: "2:14 PM",
    user: "Michael T.",
    userInitials: "MT",
    userColor: "#7e57c2",
    userMessage: (
      <>
        <span className="slack-mention">@Infina AI</span> What's our Q4 budget
        utilisation across departments?
      </>
    ),
    botName: "Infina AI",
    botResponse: (
      <>
        Q4 budget utilisation is at{" "}
        <span style={{ color: "#22c55e", fontWeight: 600 }}>87% overall</span>.
      </>
    ),
    cardLabel: "BUDGET BREAKDOWN",
    cardItems: [
      { label: "Engineering", value: "94% — $2.1M / $2.2M", highlight: true },
      { label: "Sales", value: "82% — $1.6M / $2.0M" },
      { label: "Operations", value: "78% — $0.9M / $1.2M" },
    ],
    buttons: ["View full report", "Export"],
  },
  {
    // Panel 2: Simplify Operations — work.html L1137–1184
    channel: "operations",
    time: "9:05 AM",
    user: "Anna K.",
    userInitials: "AK",
    userColor: "#149a6e",
    userMessage: (
      <>
        <span className="slack-mention">@Infina AI</span> Send the weekly
        blocker report to all team leads
      </>
    ),
    botName: "Infina AI",
    botResponse: (
      <>
        Done. Weekly blocker report sent to{" "}
        <span style={{ color: "#22c55e", fontWeight: 600 }}>8 team leads</span>.
      </>
    ),
    cardLabel: "REPORT SUMMARY",
    cardItems: [
      { label: "Open blockers", value: "3 flagged", highlight: true },
      { label: "Resolved this week", value: "7 items" },
      { label: "Escalated", value: "1 to management" },
    ],
    buttons: ["View report", "Dismiss"],
  },
];

export type FeatureTab = {
  icon: React.ReactNode;
  title: string;
  desc: string;
};

export const FEATURE_TABS: FeatureTab[] = [
  {
    // work.html L1002–1012
    icon: (
      <svg
        width="20"
        height="20"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" />
      </svg>
    ),
    title: "Real-time Support",
    desc: "Resolves tier-1 and tier-2 queries instantly, providing insights and unblocking your team in seconds.",
  },
  {
    // work.html L1013–1023
    icon: (
      <svg
        width="20"
        height="20"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <polyline points="22 12 18 12 15 21 9 3 6 12 2 12" />
      </svg>
    ),
    title: "Instant Solutions",
    desc: "Retrieves accurate answers and actionable guidance instantly, helping teams execute workflows 5x faster.",
  },
  {
    // work.html L1024–1035
    icon: (
      <svg
        width="20"
        height="20"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <circle cx="12" cy="12" r="3" />
        <path d="M12 1v6m0 6v6M5.64 5.64l4.24 4.24m4.24 4.24l4.24 4.24M1 12h6m6 0h6M5.64 18.36l4.24-4.24m4.24-4.24l4.24-4.24" />
      </svg>
    ),
    title: "Simplify Operations",
    desc: "Automates data retrieval, synthesis, and operational checks, empowering your team to focus on high-impact tasks.",
  },
];
