import { useEffect, useState } from "react";
import { JOB_DATA } from "./personal-mock-chat-data";

const VISIBLE_COUNT = 4;

interface Props {
  /** Called when an active (non-CTA) chip is clicked */
  onChipSelect: (label: string) => void;
}

/**
 * PersonalJobPicker
 * Finance / Lifestyle tab pills → chip buttons.
 * Finance has 9 chips → fade-curtain + "See more".
 * Lifestyle has 3 chips → no curtain.
 * CTA chip ("Have something else on mind? Chat with me.") → opens infina.ai.
 */
const PersonalJobPicker = ({ onChipSelect }: Props) => {
  const [activeTab, setActiveTab] = useState<"finance" | "lifestyle">("finance");
  const [expanded, setExpanded] = useState(false);
  const [visible, setVisible] = useState(true);

  // Reset expanded when tab changes
  useEffect(() => {
    setVisible(false);
    const t = setTimeout(() => {
      setExpanded(false);
      setVisible(true);
    }, 150);
    return () => clearTimeout(t);
  }, [activeTab]);

  const items = JOB_DATA[activeTab];
  const needsCurtain = items.length > VISIBLE_COUNT && !expanded;

  const handleTabClick = (tab: "finance" | "lifestyle") => {
    if (tab === activeTab) return;
    setActiveTab(tab);
  };

  const handleChipClick = (label: string) => {
    onChipSelect(label);
  };

  const handleSeeMore = () => {
    setExpanded(true);
  };

  return (
    <div className="job-picker" id="jobPicker">
      {/* Tab pills */}
      <div className="jp-tabs">
        <button
          className={`jp-tab${activeTab === "finance" ? " active" : ""}`}
          onClick={() => handleTabClick("finance")}
          type="button"
        >
          Finance
        </button>
        <button
          className={`jp-tab${activeTab === "lifestyle" ? " active" : ""}`}
          onClick={() => handleTabClick("lifestyle")}
          type="button"
        >
          Lifestyle
        </button>
        <button
          className="jp-tab jp-tab-soon"
          disabled
          type="button"
          aria-disabled="true"
        >
          More coming soon
        </button>
      </div>

      {/* Chips outer — fade-curtain via .has-more class */}
      <div
        className={[
          "jp-chips-outer",
          expanded ? "expanded" : "",
          needsCurtain ? "has-more" : "",
        ]
          .filter(Boolean)
          .join(" ")}
      >
        <div
          className="jp-chips"
          style={{ opacity: visible ? 1 : 0, transition: "opacity .15s" }}
        >
          {visible &&
            items.map((item) => {
              if (item.badge) {
                /* Chip with badge wrapper */
                return (
                  <div key={item.label} className="jp-chip-wrap">
                    <button
                      type="button"
                      className="jp-chip"
                      onClick={() => handleChipClick(item.label)}
                    >
                      {item.label}
                    </button>
                    <span className="jp-chip-badge">{item.badge}</span>
                  </div>
                );
              }

              if (item.cta) {
                /* CTA chip → navigate to infina.ai */
                return (
                  <button
                    key={item.label}
                    type="button"
                    className="jp-chip jp-chip-soon"
                    style={{ cursor: "pointer" }}
                    onClick={() => window.open("https://infina.ai", "_blank", "noopener,noreferrer")}
                  >
                    {item.label}
                  </button>
                );
              }

              if (!item.active) {
                /* Disabled / coming-soon chip */
                return (
                  <button
                    key={item.label}
                    type="button"
                    className="jp-chip jp-chip-soon"
                    disabled
                    aria-disabled="true"
                  >
                    {item.label}
                  </button>
                );
              }

              /* Normal active chip */
              return (
                <button
                  key={item.label}
                  type="button"
                  className="jp-chip"
                  onClick={() => handleChipClick(item.label)}
                >
                  {item.label}
                </button>
              );
            })}
        </div>
      </div>

      {/* See more button — rendered outside chips-outer, shown only when curtained */}
      {needsCurtain && visible && (
        <button
          type="button"
          className="jp-see-more"
          onClick={handleSeeMore}
        >
          See more{" "}
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
            <path d="M6 9l6 6 6-6" />
          </svg>
        </button>
      )}
    </div>
  );
};

export default PersonalJobPicker;
