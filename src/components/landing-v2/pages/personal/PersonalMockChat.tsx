import { useEffect, useRef, useState } from "react";
import { CONVERSATIONS } from "./personal-mock-chat-data";

type ChatState = "idle" | "thinking" | "typing" | "done";

interface Props {
  /** The chip label / question that was selected. null = closed. */
  question: string | null;
  onClose: () => void;
}

/**
 * PersonalMockChat
 * Inline conversation panel that expands inside .cbar.
 * State machine: idle → thinking (1 000 ms dots) → typing (12 ms/char typewriter)
 *   → done (follow-up chips + CTA).
 * Respects prefers-reduced-motion: skips typewriter, renders full text instantly.
 * All timers are cleaned up on unmount and on question change.
 */
const PersonalMockChat = ({ question, onClose }: Props) => {
  const [state, setState] = useState<ChatState>("idle");
  const [displayedText, setDisplayedText] = useState("");
  const [showFollowups, setShowFollowups] = useState(false);
  const [showCta, setShowCta] = useState(false);

  // Refs to track timers so cleanup is reliable across re-renders
  const thinkingTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const typeIntervalRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  // Detect prefers-reduced-motion once
  const prefersReducedMotion =
    typeof window !== "undefined" &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const clearAllTimers = () => {
    if (thinkingTimerRef.current) {
      clearTimeout(thinkingTimerRef.current);
      thinkingTimerRef.current = null;
    }
    if (typeIntervalRef.current) {
      clearTimeout(typeIntervalRef.current);
      typeIntervalRef.current = null;
    }
  };

  useEffect(() => {
    // Always clear previous timers when question changes or on unmount
    clearAllTimers();
    setDisplayedText("");
    setShowFollowups(false);
    setShowCta(false);

    if (!question) {
      setState("idle");
      return;
    }

    const conv = CONVERSATIONS[question];
    if (!conv) {
      setState("idle");
      return;
    }

    // Start thinking phase
    setState("thinking");

    thinkingTimerRef.current = setTimeout(() => {
      setState("typing");

      if (prefersReducedMotion) {
        // Instant render — no typewriter
        setDisplayedText(conv.response);
        setState("done");
        setShowFollowups(true);
        setShowCta(true);
        return;
      }

      // Typewriter: ~12 ms per character
      let charIdx = 0;
      const fullText = conv.response;

      const step = () => {
        charIdx++;
        setDisplayedText(fullText.substring(0, charIdx));
        if (charIdx < fullText.length) {
          typeIntervalRef.current = setTimeout(step, 12);
        } else {
          setState("done");
          setShowFollowups(true);
          setShowCta(true);
        }
      };

      typeIntervalRef.current = setTimeout(step, 12);
    }, 1000);

    return clearAllTimers;
  }, [question]); // eslint-disable-line react-hooks/exhaustive-deps

  // Cleanup on unmount
  useEffect(() => {
    return clearAllTimers;
  }, []);

  if (state === "idle" || !question) return null;

  const conv = CONVERSATIONS[question];
  if (!conv) return null;

  const handleFollowupClick = (fq: string) => {
    // Follow-up chip re-runs mock-chat with the followup label if it has a
    // conversation entry, otherwise re-asks the original question
    const target = fq in CONVERSATIONS ? fq : question;
    // Signal parent to open new conversation via custom event that PersonalHero listens for
    window.dispatchEvent(
      new CustomEvent("personal-mock-chat-select", { detail: { question: target } })
    );
  };

  return (
    <div className="cbar-messages-inner">
      {/* Close button */}
      <div className="mc-close-row">
        <button
          type="button"
          className="mc-close"
          aria-label="Close"
          onClick={onClose}
        >
          ✕
        </button>
      </div>

      {/* User bubble */}
      <div className="mc-user">
        <div className="mc-user-bubble">{question}</div>
      </div>

      {/* Agent response */}
      <div className="mc-agent">
        <div className="mc-avatar" aria-hidden="true">
          {conv.avatar}
        </div>
        <div className="mc-body">
          <div className="mc-name">{conv.specialist}</div>

          {/* Thinking dots */}
          {state === "thinking" && (
            <div className="mc-bubble">
              <div className="mc-thinking">
                <span className="mc-dot" />
                <span className="mc-dot" />
                <span className="mc-dot" />
              </div>
            </div>
          )}

          {/* Typewriter / completed response */}
          {(state === "typing" || state === "done") && (
            <div className="mc-bubble">{displayedText}</div>
          )}

          {/* Follow-up chips */}
          {showFollowups && (
            <div className="mc-followups">
              {conv.followups.map((fq) => (
                <button
                  key={fq}
                  type="button"
                  className="mc-followup"
                  onClick={() => handleFollowupClick(fq)}
                >
                  {fq}
                </button>
              ))}
            </div>
          )}

          {/* CTA */}
          {showCta && (
            <div className="mc-cta">
              <button
                type="button"
                className="mc-cta-btn"
                onClick={() => window.open("https://infina.ai", "_blank", "noopener,noreferrer")}
              >
                Chat with your Specialist
                <svg
                  width="14"
                  height="14"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M5 12h14M12 5l7 7-7 7" />
                </svg>
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default PersonalMockChat;
