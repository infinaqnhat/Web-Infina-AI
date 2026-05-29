/**
 * Chat scenarios for the FocusContextChat interactive window.
 * Source-mirrored from the JS `scenarios` object in Web-Infina-AI/focus-alignment.html (lines 651-670).
 *
 * DIVERGENCE FROM infina-pfa-80389:
 *   infina-pfa-80389 simplified the "blockers" scenario to `typing: true` (typing indicator only).
 *   HTML source-of-truth has the full blockers response: aiIntro + single task card + followup + actions[].
 *   This file restores the full HTML source data for the mirror repo.
 */

export type ScenarioKey = "priorities" | "blockers" | "report";

export interface TaskItem {
  id: string;
  name: string;
  tag: string;
  tagClass: string;
  idColor: string;
}

export interface BlockerTask {
  id: string;
  name: string;
  tag: string;
}

export interface Scenario {
  userMsg: string;
  /** "typing" scenario — shows only typing indicator (infina-pfa-80389 simplification) */
  typing?: boolean;
  /** AI intro text */
  aiIntro?: string;
  /** "tasks" scenario — shows AI intro + task list */
  tasks?: TaskItem[];
  /** "blockers" scenario — shows AI intro + single task card + followup + action buttons */
  task?: BlockerTask;
  followup?: string;
  actions?: string[];
  /** "report" scenario — shows AI intro + note + followup */
  note?: string;
}

export const CHAT_SCENARIOS: Record<ScenarioKey, Scenario> = {
  priorities: {
    userMsg: "What are my top priorities for this week?",
    aiIntro:
      "Here are your top 3 Strategic High Priorities — all currently in Queue:",
    tasks: [
      {
        id: "KR-358",
        name: "Infina AI Landing Page",
        tag: "Focus",
        tagClass: "status-focus",
        idColor: "#1863dc",
      },
      {
        id: "KR-355",
        name: "Infina AI logo redesign",
        tag: "Queue",
        tagClass: "status-queue",
        idColor: "#1863dc",
      },
      {
        id: "SHP-568",
        name: "Website — MKT × Product merge",
        tag: "Queue",
        tagClass: "status-queue",
        idColor: "#1863dc",
      },
    ],
  },
  blockers: {
    userMsg: "Any blockers on KR-355?",
    aiIntro:
      "KR-355 is in Queue. Last update: 1st draft sent to James. Noah is working with James on revisions.",
    task: { id: "KR-355", name: "Infina AI logo redesign", tag: "Queue" },
    followup: "No blocker logged — want me to ask Nathan for a status check?",
    actions: ["Yes, ping Nathan", "No, skip"],
  },
  report: {
    userMsg: "Submit my daily report",
    aiIntro:
      "I don't see a daily report for today yet. Here's a draft based on your updates:",
    note: "KR-355: Sent 1st draft to James. Noah is working with James on revisions.",
    followup: "Any blockers today? (yes/no)",
  },
};

export const PROMPT_BUTTONS: { key: ScenarioKey; label: string }[] = [
  { key: "priorities", label: "What are my top priorities for this week?" },
  { key: "blockers", label: "Any blockers on KR-355?" },
  { key: "report", label: "Submit my daily report" },
];
