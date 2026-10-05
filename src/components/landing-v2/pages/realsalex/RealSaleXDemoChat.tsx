import { useEffect, useRef, useState } from "react";
import type { AgentTab } from "./realsalex-content-data";
import { demoQuestions } from "./realsalex-demo-questions-data";
import { demoTabCopy } from "./realsalex-demo-card-copy-data";
import type { DemoAnswer } from "./realsalex-demo-questions-data";
import { PERSONA_OPTIONS, demoPersonas } from "./realsalex-demo-personas-data";
import type { PersonaKey } from "./realsalex-demo-personas-data";

/** Simulated "typing" pause before an answer appears (source timings). */
const THINK_MS_CHIP = 640;
const THINK_MS_FREE_TEXT = 700;

interface ChatState {
  qi: number;
  thinking: boolean;
  asked: string | null;
  unknown: boolean;
  persona: PersonaKey | null;
}

const INITIAL_STATE: ChatState = { qi: 0, thinking: false, asked: null, unknown: false, persona: "buyer" };

/**
 * Keyword match of a free-text question against the canned answers: counts
 * words of 4+ chars that appear anywhere in an entry and needs at least 2
 * hits, otherwise -1 ("not in the data"). Same heuristic as the source.
 */
const matchQuestion = (text: string, questions: DemoAnswer[]) => {
  const words = text.toLowerCase().match(/[a-z$0-9]{4,}/g) || [];
  let best = -1;
  let top = 0;
  questions.forEach((q, i) => {
    const hay = `${q.q} ${q.lead} ${q.points.map((p) => p.t).join(" ")}`.toLowerCase();
    const score = words.filter((w) => hay.includes(w)).length;
    if (score > top) {
      top = score;
      best = i;
    }
  });
  return top >= 2 ? best : -1;
};

/**
 * Idle state of the demo card: persona pills, the buyer/advisor thread, the
 * suggested-question chips and a free-text ask box. FRONT-END ONLY, every
 * answer is canned. The parent remounts this per tab (key={tab}), which
 * resets the thread to the first-time-buyer persona like the source does on
 * a tab switch.
 */
const RealSaleXDemoChat = ({ tab, hidden }: { tab: AgentTab; hidden: boolean }) => {
  const questions = demoQuestions[tab];
  const personas = demoPersonas[tab];
  const { agentFirst, roleLabel, askTitle } = demoTabCopy[tab];

  const [state, setState] = useState<ChatState>(INITIAL_STATE);
  const [draft, setDraft] = useState("");
  const thinkTimer = useRef<number>();

  useEffect(() => () => window.clearTimeout(thinkTimer.current), []);

  const think = (next: ChatState, delayMs: number) => {
    window.clearTimeout(thinkTimer.current);
    setState(next);
    thinkTimer.current = window.setTimeout(() => setState((s) => ({ ...s, thinking: false })), delayMs);
  };

  const pickQuestion = (i: number) => {
    if (i === state.qi && !state.asked && !state.persona) return;
    think({ qi: i, thinking: true, asked: null, unknown: false, persona: null }, THINK_MS_CHIP);
  };

  const pickPersona = (key: PersonaKey) => {
    if (key === state.persona) return;
    think({ qi: state.qi, thinking: true, asked: null, unknown: false, persona: key }, THINK_MS_CHIP);
  };

  const askFreeText = () => {
    const text = draft.trim();
    if (!text) return;
    const i = matchQuestion(text, questions);
    setDraft("");
    think({ qi: i < 0 ? state.qi : i, thinking: true, asked: text, unknown: i < 0, persona: null }, THINK_MS_FREE_TEXT);
  };

  const unknownAnswer: DemoAnswer = {
    q: "",
    lead: "I do not have that in the listing, the disclosure or the public records for this property, so I am not going to guess.",
    points: [],
    close: `I have passed the question to ${agentFirst}. The answer will appear here in this thread.`,
    sources: ["Agent Notes"],
  };
  const active = state.persona ? personas[state.persona] : state.unknown ? unknownAnswer : questions[state.qi];
  const closeText = active.close.split("%A").join(agentFirst);
  const buyerText = state.persona ? active.q : state.asked || questions[state.qi].q;

  return (
    <div className="demo-body" id="demo-idle" hidden={hidden}>
      <div className="persona-pills">
        {PERSONA_OPTIONS.map((p) => (
          <button
            key={p.key}
            type="button"
            className={`persona-pill${p.key === state.persona ? " is-active" : ""}`}
            onClick={() => pickPersona(p.key)}
          >
            {p.label}
          </button>
        ))}
      </div>
      <h3>{askTitle}</h3>
      <div className="demo-thread">
        <div className="demo-msg buyer">
          <span className="lbl">Buyer</span>
          <p>{buyerText}</p>
        </div>
        {state.thinking ? (
          <div className="demo-thinking">
            <span />
            <span />
            <span />
          </div>
        ) : (
          <div className="demo-msg advisor">
            <span className="lbl">{roleLabel}</span>
            <div className="bubble">
              <p>{active.lead}</p>
              {active.points.length > 0 && (
                <ol className="demo-points">
                  {active.points.map((pt) => (
                    <li key={pt.n}>
                      <b>{pt.n}</b>
                      <span>{pt.t}</span>
                    </li>
                  ))}
                </ol>
              )}
              <p>{closeText}</p>
              <div className="demo-sources">
                <span className="lbl">Sources</span>
                {active.sources.map((src) => (
                  <span key={src} className="src">
                    {src}
                  </span>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
      <div>
        <div className="demo-chips">
          {questions.map((q, i) => (
            <button
              key={q.q}
              type="button"
              className={`demo-chip${i === state.qi && !state.asked ? " is-active" : ""}`}
              onClick={() => pickQuestion(i)}
            >
              {q.q}
            </button>
          ))}
        </div>
        <div className="demo-ask-row" style={{ marginTop: 12 }}>
          <input
            type="text"
            value={draft}
            placeholder="Ask about this property..."
            aria-label="Ask the advisor about this property"
            onChange={(e) => setDraft(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") askFreeText();
            }}
          />
          <button type="button" aria-label="Send question" onClick={askFreeText}>
            →
          </button>
        </div>
      </div>
    </div>
  );
};

export default RealSaleXDemoChat;
