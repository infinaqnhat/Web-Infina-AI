import { useEffect, useRef, useState } from "react";
import PersonalJobPicker from "./PersonalJobPicker";
import PersonalMockChat from "./PersonalMockChat";

/**
 * PersonalHero
 * Hero section for /personal — mirrors personal.html L1244–1316.
 * - Purple dual-radial background + hero-grid-bg + 4 floating .shape divs
 * - hero-badge "For Individual" (verbatim from HTML L1253)
 * - h1: "Better your everyday decisions / with AI specialists" (verbatim from HTML L1254)
 * - Chat bar: flex-column — .cbar-messages panel above, .cbar-row input row below
 * - Hosts PersonalJobPicker and PersonalMockChat; wires chip selection → mock-chat
 * - Typewriter cycling ghost text (4 prompts from HTML L1697–1702)
 */
const PROMPTS = [
  "ACB stock at 23k, should I buy now?",
  "I have 1B, want to buy 3B house in 2 years - invest how?",
  "Income 20M/month, how much rent to save enough?",
  "Any important news affecting VN market today?",
];

const PersonalHero = () => {
  const [ghostText, setGhostText] = useState("");
  const [userValue, setUserValue] = useState("");
  const [userTyped, setUserTyped] = useState(false);
  // null = chat closed; string = currently selected question
  const [activeQuestion, setActiveQuestion] = useState<string | null>(null);

  const typeIdxRef = useRef(0);
  const charIdxRef = useRef(0);
  const isDelRef = useRef(false);
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // ── Typewriter ghost text ───────────────────────────────────────
  useEffect(() => {
    const typeStep = () => {
      if (userTyped) return;
      const cur = PROMPTS[typeIdxRef.current];
      let delay: number;
      if (!isDelRef.current) {
        charIdxRef.current++;
        setGhostText(cur.substring(0, charIdxRef.current));
        if (charIdxRef.current >= cur.length) {
          isDelRef.current = true;
          delay = 1800;
        } else {
          delay = 40 + Math.random() * 40;
        }
      } else {
        charIdxRef.current--;
        setGhostText(cur.substring(0, charIdxRef.current));
        if (charIdxRef.current <= 0) {
          isDelRef.current = false;
          typeIdxRef.current = (typeIdxRef.current + 1) % PROMPTS.length;
          delay = 300;
        } else {
          delay = 20;
        }
      }
      timerRef.current = setTimeout(typeStep, delay);
    };

    timerRef.current = setTimeout(typeStep, 100);
    return () => {
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, [userTyped]);

  // ── Listen for follow-up chip re-selections from PersonalMockChat ─
  useEffect(() => {
    const handler = (e: Event) => {
      const { question } = (e as CustomEvent<{ question: string }>).detail;
      openMockChat(question);
    };
    window.addEventListener("personal-mock-chat-select", handler);
    return () => window.removeEventListener("personal-mock-chat-select", handler);
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  // ── Input handlers ──────────────────────────────────────────────
  const handleInputChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const val = e.target.value;
    setUserValue(val);
    if (val.length > 0 && !userTyped) {
      setUserTyped(true);
      if (timerRef.current) clearTimeout(timerRef.current);
    } else if (val.length === 0 && userTyped) {
      setUserTyped(false);
      setGhostText("");
      typeIdxRef.current = 0;
      charIdxRef.current = 0;
      isDelRef.current = false;
    }
    const ta = textareaRef.current;
    if (ta) {
      ta.style.height = "auto";
      ta.style.height = Math.min(ta.scrollHeight, 120) + "px";
    }
  };

  const handleSend = () => {
    if (userValue.trim() || ghostText) {
      window.open("https://infina.ai", "_blank", "noopener,noreferrer");
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  // ── Mock-chat open/close ────────────────────────────────────────
  const openMockChat = (question: string) => {
    setUserValue(question);
    setUserTyped(true);
    if (timerRef.current) clearTimeout(timerRef.current);
    const ta = textareaRef.current;
    if (ta) {
      ta.style.height = "auto";
      ta.style.height = Math.min(ta.scrollHeight, 120) + "px";
    }
    setActiveQuestion(question);
  };

  const handleChipSelect = (label: string) => {
    openMockChat(label);
  };

  const handleMockChatClose = () => {
    setActiveQuestion(null);
  };

  const isChatExpanded = activeQuestion !== null;

  return (
    <section className="hero">
      {/* Dual-radial purple background */}
      <div className="hero-bg" />
      <div className="hero-grid-bg" />

      {/* Floating decorative shapes — hidden on mobile via CSS */}
      <div className="shape shape-1" />
      <div className="shape shape-2" />
      <div className="shape shape-3" />
      <div className="shape shape-4" />

      <div className="container">
        <div className="hero-inner">
          {/* Badge — verbatim from HTML L1253 */}
          <div className="hero-badge">For Individual</div>

          {/* h1 — verbatim from HTML L1254 */}
          <h1>
            Better your everyday decisions
            <br />
            with <span className="accent">AI specialists</span>
          </h1>

          <div className="cbar-wrap">
            {/* Chat bar — flex-column: messages panel above, input row below */}
            <div className={`cbar${isChatExpanded ? " expanded" : ""}`}>
              {/* Collapsible messages panel */}
              <div className="cbar-messages">
                <PersonalMockChat
                  question={activeQuestion}
                  onClose={handleMockChatClose}
                />
              </div>

              {/* Input row */}
              <div className="cbar-row">
                <div className="cbar-input-wrap">
                  <div
                    className={`cbar-ghost${userTyped ? " hidden" : ""}`}
                    aria-hidden="true"
                  >
                    {ghostText}
                  </div>
                  <textarea
                    ref={textareaRef}
                    className="cbar-input"
                    rows={1}
                    aria-label="Ask specialist"
                    value={userValue}
                    onChange={handleInputChange}
                    onKeyDown={handleKeyDown}
                  />
                </div>

                <div className="cbar-icons">
                  <button
                    type="button"
                    className="cbar-icon-btn"
                    aria-label="Attach"
                  >
                    <svg
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    >
                      <path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48" />
                    </svg>
                  </button>
                  <button
                    type="button"
                    className="cbar-icon-btn"
                    aria-label="Voice"
                  >
                    <svg
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    >
                      <rect x="9" y="2" width="6" height="12" rx="3" />
                      <path d="M5 10v2a7 7 0 0 0 14 0v-2" />
                      <path d="M12 19v3" />
                    </svg>
                  </button>
                </div>

                <button
                  className="cbar-send"
                  onClick={handleSend}
                  aria-label="Send"
                >
                  <svg
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2.5"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <path d="M12 19V5M6 11l6-6 6 6" />
                  </svg>
                </button>
              </div>
            </div>

            {/* Job Picker — below the chat bar, inside cbar-wrap */}
            <PersonalJobPicker onChipSelect={handleChipSelect} />
          </div>
        </div>
      </div>
    </section>
  );
};

export default PersonalHero;
