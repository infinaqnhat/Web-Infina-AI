import { UPLOADS } from "./realsalex-content-data";
import { RealSaleXIcon } from "./realsalex-icons";
import type { RealSaleXIconName } from "./realsalex-icons";

type RowStatus = "alert" | "due" | "done";

interface QuestionRow {
  photo: string;
  place: string;
  question: string;
  topic: string;
  status: RowStatus;
  statusLabel: string;
}

const MAIN_THUMB = `${UPLOADS}/property-123-main-thumb.jpg`;

/* Sample buyer, as in the source mockup. */
const BUYER_TAGS: { icon: RealSaleXIconName; label: string }[] = [
  { icon: "pin", label: "Austin, TX" },
  { icon: "person", label: "First-time buyer" },
  { icon: "checkCircle", label: "Pre-approved" },
  { icon: "tag", label: "Budget up to $900K" },
  { icon: "bed", label: "3-4 bed" },
];

const ATTENTION_ROWS: QuestionRow[] = [
  {
    photo: MAIN_THUMB,
    place: "123 Main Street",
    question: "Was this repaired professionally, or should we ask for a closer inspection?",
    topic: "Inspection",
    status: "alert",
    statusLabel: "Needs attention",
  },
  {
    photo: MAIN_THUMB,
    place: "123 Main Street",
    question: "Can we get the patio repair credit in writing before we sign?",
    topic: "Credit",
    status: "alert",
    statusLabel: "Needs attention",
  },
];

const OTHER_ROWS: QuestionRow[] = [
  {
    photo: `${UPLOADS}/property-lakeview-88.jpg`,
    place: "88 Lakeview Drive",
    question: "Does the HOA allow short-term rentals?",
    topic: "HOA",
    status: "due",
    statusLabel: "Following up",
  },
  {
    photo: `${UPLOADS}/property-oaklane-42.jpg`,
    place: "42 Oak Lane",
    question: "Is the lender fully confirmed for this property?",
    topic: "Financing",
    status: "done",
    statusLabel: "Answered",
  },
  {
    photo: MAIN_THUMB,
    place: "123 Main Street",
    question: "When exactly is the disclosure deadline?",
    topic: "Timeline",
    status: "done",
    statusLabel: "Answered",
  },
];

const QuestionRowItem = ({ row }: { row: QuestionRow }) => {
  const isAlert = row.status === "alert";
  return (
    <div className={`buyer-row${isAlert ? " is-alert" : ""}`}>
      {isAlert && (
        <span className="buyer-row-icon">
          <RealSaleXIcon name="alert" strokeWidth={2.5} />
        </span>
      )}
      <img className="buyer-row-photo" src={row.photo} alt={row.place} />
      <span className="buyer-row-text">
        <b>{row.question}</b>
        <span>
          {row.place} · {row.topic}
        </span>
      </span>
      <span className={`buyer-row-status is-${row.status}`}>{row.statusLabel}</span>
      <span className="buyer-row-chevron">
        <RealSaleXIcon name="chevronRight" />
      </span>
    </div>
  );
};

/**
 * "Once the buyer is ready" section (Buyer Agent tab only): a sample buyer
 * profile with open questions grouped by urgency. Mirrors the
 * <div class="buyer-card"> section in Web-Infina-AI/realsalex-v2.html.
 */
const RealSaleXBuyerProfile = ({ hidden }: { hidden: boolean }) => (
  <section className="section" hidden={hidden}>
    <div className="container">
      <div className="section-head reveal">
        <span className="eyebrow">Once the buyer is ready</span>
        <h2>
          Address obstacles while there's <span className="accent">time to act.</span>
        </h2>
        <p>
          The relationship continues after a tour or an offer. Home Concierge helps organize questions and flag
          issues for your attention.
        </p>
      </div>
      <div className="buyer-card reveal">
        <div className="buyer-topbar">
          <div className="buyer-who">
            <img className="buyer-avatar" src={`${UPLOADS}/avatar-alex-rivera.jpg`} alt="Alex Rivera" />
            <div>
              <h3 className="buyer-name">Alex Rivera</h3>
              <p className="buyer-status">
                <span className="buyer-dot" />
                Active buyer · 3 homes in consideration
              </p>
            </div>
          </div>
          <div className="buyer-contact">
            <span>
              <RealSaleXIcon name="mail" />
              alex.rivera@example.com
            </span>
            <span>
              <RealSaleXIcon name="phone" />
              (512) 555-0148
            </span>
          </div>
        </div>

        <div className="buyer-tags">
          {BUYER_TAGS.map((t) => (
            <span key={t.label}>
              <RealSaleXIcon name={t.icon} size={15} />
              {t.label}
            </span>
          ))}
        </div>

        <div className="buyer-group is-alert">
          <div className="buyer-group-head">
            <span className="buyer-group-icon is-alert">
              <RealSaleXIcon name="alert" strokeWidth={2.5} />
            </span>
            Needs your attention
            <span className="buyer-group-count is-alert">{ATTENTION_ROWS.length}</span>
          </div>
          {ATTENTION_ROWS.map((row) => (
            <QuestionRowItem key={row.question} row={row} />
          ))}
        </div>

        <div className="buyer-group">
          <div className="buyer-group-head">
            <span className="buyer-group-icon">
              <RealSaleXIcon name="chat" />
            </span>
            Other questions
            <span className="buyer-group-count">{OTHER_ROWS.length}</span>
          </div>
          {OTHER_ROWS.map((row) => (
            <QuestionRowItem key={row.question} row={row} />
          ))}
        </div>
      </div>
    </div>
  </section>
);

export default RealSaleXBuyerProfile;
