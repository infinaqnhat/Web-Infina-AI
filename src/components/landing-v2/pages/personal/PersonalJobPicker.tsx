import { JOB_DATA, type JobChip } from "./personal-mock-chat-data";

interface Props {
  /** Called when an active (non-CTA) card is clicked */
  onChipSelect: (label: string) => void;
}

const INFINA_URL = "https://infina.ai";
const openInfina = () => window.open(INFINA_URL, "_blank", "noopener,noreferrer");

/** Speech-bubble icon, 14×14, matches the marketing-site CHAT_ICON path */
const ChatIcon = () => (
  <svg
    width="14"
    height="14"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
  </svg>
);

/** One question/CTA card inside a category grid. */
const JobCard = ({
  item,
  onChipSelect,
}: {
  item: JobChip;
  onChipSelect: (label: string) => void;
}) => {
  if (item.cta) {
    return (
      <div
        className="jp-card jp-card-cta"
        onClick={openInfina}
        role="button"
        tabIndex={0}
        onKeyDown={(e) => {
          if (e.key === "Enter" || e.key === " ") openInfina();
        }}
      >
        <span className="jp-card-cta-text">
          Have something else on mind?
          <br />
          Chat with me.
        </span>
      </div>
    );
  }

  return (
    <div
      className="jp-card"
      onClick={() => onChipSelect(item.label)}
      role="button"
      tabIndex={0}
      onKeyDown={(e) => {
        if (e.key === "Enter" || e.key === " ") onChipSelect(item.label);
      }}
    >
      <div className="jp-card-title">{item.label}</div>
      <div className="jp-card-count">
        <ChatIcon />
        <strong>{item.count}</strong> asked
      </div>
      {item.badge && <span className="jp-card-badge">{item.badge}</span>}
    </div>
  );
};

/**
 * PersonalJobPicker
 * Two stacked tinted category sections (Finance, Lifestyle), each a 3-column
 * card grid — mirrors the live marketing site (no tab toggle). Each card shows
 * the question title + question count with a chat icon; the CTA card
 * ("Have something else on mind?") opens infina.ai.
 */
const PersonalJobPicker = ({ onChipSelect }: Props) => (
  <div className="job-picker" id="jobPicker">
    <div className="jp-category-section jp-finance">
      <div className="jp-category-divider">Finance</div>
      <div className="jp-chips">
        {JOB_DATA.finance.map((item) => (
          <JobCard key={item.label} item={item} onChipSelect={onChipSelect} />
        ))}
      </div>
    </div>

    <div className="jp-category-section jp-lifestyle">
      <div className="jp-category-divider">Lifestyle</div>
      <div className="jp-chips">
        {JOB_DATA.lifestyle.map((item) => (
          <JobCard key={item.label} item={item} onChipSelect={onChipSelect} />
        ))}
      </div>
    </div>
  </div>
);

export default PersonalJobPicker;
