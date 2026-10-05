import { RealSaleXIcon } from "./realsalex-icons";
import type { RealSaleXIconName } from "./realsalex-icons";

type IconTone = "blue" | "green" | "purple" | "amber" | "rose";

/** Data sources feeding the Property Expert, two per row as in the source. */
const SOURCE_ROWS: { icon: RealSaleXIconName; tone: IconTone; label: string }[][] = [
  [
    { icon: "house", tone: "blue", label: "MLS" },
    { icon: "doc", tone: "green", label: "Seller Disclosure" },
  ],
  [
    { icon: "search", tone: "purple", label: "Inspection Report" },
    { icon: "bank", tone: "amber", label: "Public Records" },
  ],
  [
    { icon: "people", tone: "blue", label: "HOA" },
    { icon: "bars", tone: "rose", label: "Comps" },
  ],
];

const BADGES: { icon: RealSaleXIconName; tone: IconTone; title: string; text: string }[] = [
  { icon: "lock", tone: "blue", title: "Private buyer conversations", text: "Every buyer gets a confidential chat." },
  { icon: "bolt", tone: "green", title: "No login required", text: "Get answers instantly." },
  {
    icon: "clock",
    tone: "amber",
    title: "Share it everywhere",
    text: "Property page, listing campaigns, open-house materials, or a yard sign QR.",
  },
];

const ARROW_STROKE = { stroke: "currentColor", strokeWidth: 3, strokeLinecap: "round", strokeLinejoin: "round" } as const;

/**
 * "Grounded in your listing" flow (Listing Agent tab): six data sources →
 * Property Expert → a cited answer, plus the three trust badges. Mirrors
 * <div class="grounded-diagram"> in Web-Infina-AI/realsalex-v2.html; the
 * curved connector SVGs are copied as-is because they are not icon shapes.
 */
const RealSaleXGroundedDiagram = () => (
  <div className="grounded-diagram reveal">
    <div className="grounded-flow">
      <div className="grounded-sources">
        {SOURCE_ROWS.map((row) => (
          <div key={row[0].label} className="source-row">
            {row.map((src) => (
              <div key={src.label} className="source-card">
                <span className={`source-icon icon-${src.tone}`}>
                  <RealSaleXIcon name={src.icon} />
                </span>
                {src.label}
              </div>
            ))}
          </div>
        ))}
      </div>

      <div className="grounded-arrows">
        <span className="arrow-cell">
          <svg width="70" height="60" viewBox="0 0 180 110" fill="none">
            <path d="M6 8 C 70 8, 82 32, 92 58 C 101 82, 118 98, 164 98" {...ARROW_STROKE} />
            <path d="M164 98 L154 92 M164 98 L154 104" {...ARROW_STROKE} />
          </svg>
        </span>
        <span className="arrow-cell">
          <svg width="70" height="14" viewBox="0 0 180 24" fill="none">
            <path d="M6 12 H164" stroke="currentColor" strokeWidth={3} strokeLinecap="round" />
            <path d="M164 12 L154 6 M164 12 L154 18" {...ARROW_STROKE} />
          </svg>
        </span>
        <span className="arrow-cell">
          <svg width="70" height="60" viewBox="0 0 180 110" fill="none">
            <path d="M6 102 C 70 102, 82 78, 92 52 C 101 28, 118 12, 164 12" {...ARROW_STROKE} />
            <path d="M164 12 L154 6 M164 12 L154 18" {...ARROW_STROKE} />
          </svg>
        </span>
      </div>

      <div className="grounded-mobile-arrows">
        <svg width="120" height="65" viewBox="0 0 240 130" fill="none">
          <path d="M20 10 C20 55, 70 60, 110 60 C150 60, 190 70, 190 110" stroke="currentColor" strokeWidth={3} strokeLinecap="round" />
          <path d="M190 110L182 98" stroke="currentColor" strokeWidth={3} strokeLinecap="round" />
          <path d="M190 110L198 98" stroke="currentColor" strokeWidth={3} strokeLinecap="round" />
          <circle cx="20" cy="10" r="7" fill="currentColor" />
        </svg>
        <svg width="120" height="65" viewBox="0 0 240 130" fill="none">
          <path d="M220 10 C220 55, 170 60, 130 60 C90 60, 50 70, 50 110" stroke="currentColor" strokeWidth={3} strokeLinecap="round" />
          <path d="M50 110L42 98" stroke="currentColor" strokeWidth={3} strokeLinecap="round" />
          <path d="M50 110L58 98" stroke="currentColor" strokeWidth={3} strokeLinecap="round" />
          <circle cx="220" cy="10" r="7" fill="currentColor" />
        </svg>
      </div>

      <div className="grounded-center">
        <div className="center-node">
          <RealSaleXIcon name="house" size={30} />
          <span>Property Expert</span>
        </div>
        <span className="center-dashed" />
      </div>

      <div className="grounded-output">
        <span className="output-arrow">
          <RealSaleXIcon name="arrowRight" size={22} strokeWidth={2.5} />
        </span>
        <div className="answer-card">
          <span className="answer-check">
            <RealSaleXIcon name="answerCheck" size={18} strokeWidth={2.5} />
          </span>
          <p>Foundation repairs completed in 2022.</p>
          <div className="answer-tags">
            <span className="answer-tag">
              <span className="source-icon icon-green sm">
                <RealSaleXIcon name="doc" size={12} />
              </span>
              Seller Disclosure
            </span>
            <span className="answer-tag">
              <span className="source-icon icon-purple sm">
                <RealSaleXIcon name="search" size={12} />
              </span>
              Inspection Report
            </span>
          </div>
          {/* The source links to "#" (the sample answer has no document to open);
              preventDefault keeps the click from jumping the page to the top. */}
          <a href="#" className="answer-source-link" onClick={(e) => e.preventDefault()}>
            SOURCE SHOWN <RealSaleXIcon name="external" size={12} />
          </a>
        </div>
      </div>
    </div>

    <div className="grounded-callout">
      <span className="callout-icon">
        <RealSaleXIcon name="info" size={14} />
      </span>
      If the answer isn't in the data, it says so.
    </div>

    <div className="grounded-badges">
      {BADGES.map((badge) => (
        <div key={badge.title} className="grounded-badge">
          <span className={`badge-icon icon-${badge.tone}`}>
            <RealSaleXIcon name={badge.icon} size={18} />
          </span>
          <div>
            <b>{badge.title}</b>
            <span>{badge.text}</span>
          </div>
        </div>
      ))}
    </div>
  </div>
);

export default RealSaleXGroundedDiagram;
