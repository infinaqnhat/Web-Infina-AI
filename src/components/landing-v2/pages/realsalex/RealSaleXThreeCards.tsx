import type { ThreeCardSectionCopy } from "./realsalex-content-data";

/**
 * Numbered 3-card section (.aic-3). realsalex-v2.html uses it twice, once per
 * tab: "Three reasons agents send a Property Expert." (listing) and
 * "Give every question a next step." (buying). The page passes `hidden` for
 * the inactive tab so the section stays mounted, as in the source.
 */
const RealSaleXThreeCards = ({ copy, hidden }: { copy: ThreeCardSectionCopy; hidden: boolean }) => (
  <section className="section" hidden={hidden}>
    <div className="container">
      <div className="section-head reveal">
        {copy.eyebrow && <span className="eyebrow">{copy.eyebrow}</span>}
        <h2>
          {copy.title}
          <span className="accent">{copy.accent}</span>
        </h2>
        {copy.sub && <p>{copy.sub}</p>}
      </div>
      <div className="aic-3">
        {copy.cards.map((card, i) => (
          <div key={card.title} className="aic reveal">
            <span className="aic-num">{String(i + 1).padStart(2, "0")}</span>
            <h3>{card.title}</h3>
            <p>{card.text}</p>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default RealSaleXThreeCards;
