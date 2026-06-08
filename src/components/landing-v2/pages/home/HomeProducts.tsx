import { useState } from "react";
import { Link } from "react-router-dom";
import {
  type TabKey,
  insideCards,
  personalRows,
  workAudiences,
} from "./home-agents-data";

/**
 * Products section — mirrors home.html `.products` (#products).
 *
 * Merged products + specialists accordion: each `.product-group` holds a
 * `.product-card` whose "Meet the specialist" toggle reveals an inline
 * `.product-panel` containing the specialist grids (formerly the tabbed
 * HomeAgents section). Single-open behavior; clicking the active card closes it.
 *
 * Desktop: `.product-group{display:contents}` so card + full-width panel become
 * grid children (card row 1, panel row 2 spanning all columns). Mobile: stacked
 * max-height accordion. All class names + data-* attrs preserved verbatim.
 */

interface ProductMeta {
  key: TabKey;
  audienceLabel: string;
  tag: string;
  title: string;
  desc: string;
}

const PRODUCTS: ProductMeta[] = [
  {
    key: "inside",
    audienceLabel: "For Products",
    tag: "Infina AI Inside",
    title: "More engaged customer. Higher revenue. Zero build time.",
    desc: "Confused customers don't convert. AI Inside puts a specialist right inside your app so every user gets the right guidance, at the right moment, and moves forward.",
  },
  {
    key: "work",
    audienceLabel: "For Business",
    tag: "Infina AI Work",
    title: "Your team, working at their best with AI handling the rest.",
    desc: "Your top talent shouldn't be buried in updates and follow-ups. AI Work handles the operational load so your team stays focused on the work that drives results.",
  },
  {
    key: "personal",
    audienceLabel: "For Individuals",
    tag: "Infina AI Personal",
    title: "Grow more. Stress less. Achieve your goal.",
    desc: "Whether you should invest or pay off debt, whether an insurance plan is worth it, or where to travel on your budget, stop guessing and get a clear answer.",
  },
];

/** Inside panel — 4-card specialist grid. */
const InsidePanelBody = () => (
  <div className="agents-grid agents-grid-4" id="inside-grid">
    {insideCards.map((card) => (
      <div key={card.agent} className="agents-card" data-agent={card.agent}>
        <div className="agents-card-left">
          <h3 className="agents-card-title">
            <span className="agents-title-main">{card.titleMain}</span>
            {card.titleSub && (
              <span className="agents-title-sub">{card.titleSub}</span>
            )}
          </h3>
          <div className="agents-context-badge">{card.contextBadge}</div>
        </div>
        <div className="agents-card-right">
          <ul className="agents-list">
            {card.bullets.map((b) => (
              <li key={b}>{b}</li>
            ))}
          </ul>
        </div>
      </div>
    ))}
  </div>
);

/** Work panel — sales wide row + operations 4-card grid. */
const WorkPanelBody = () => (
  <>
    {workAudiences.map((audience) => (
      <div key={audience.label} className="agents-work-audience">
        <span className="agents-audience-label">{audience.label}</span>
        <div
          className={`agents-grid${audience.cards.length > 1 ? " agents-grid-4" : ""}`}
          id={audience.label === "For Sales Teams" ? undefined : "work-grid"}
        >
          {audience.cards.map((card) =>
            card.wide ? (
              <div key={card.titleMain} className="agents-card agents-card-row">
                <div className="agents-card-row-meta">
                  <h3 className="agents-card-title">
                    <span className="agents-title-main">{card.titleMain}</span>
                    {card.titleSub && (
                      <span className="agents-title-sub">{card.titleSub}</span>
                    )}
                  </h3>
                  <div className="agents-context-badge">{card.contextBadge}</div>
                </div>
                <ul className="agents-list agents-list-row">
                  {card.bullets.map((b) => (
                    <li key={b}>{b}</li>
                  ))}
                </ul>
              </div>
            ) : (
              <div key={card.titleMain} className="agents-card">
                <div className="agents-card-left">
                  <h3 className="agents-card-title">
                    <span className="agents-title-main">{card.titleMain}</span>
                    {card.titleSub && (
                      <span className="agents-title-sub">{card.titleSub}</span>
                    )}
                  </h3>
                  <div className="agents-context-badge">{card.contextBadge}</div>
                </div>
                <div className="agents-card-right">
                  <ul className="agents-list">
                    {card.bullets.map((b) => (
                      <li key={b}>{b}</li>
                    ))}
                  </ul>
                </div>
              </div>
            )
          )}
        </div>
      </div>
    ))}
  </>
);

/** Personal panel — finance / lifestyle / more-coming rows. */
const PersonalPanelBody = () => (
  <div className="agents-grid agents-personal-grid">
    {personalRows.map((row) => (
      <div
        key={row.titleMain}
        className={`agents-personal-row${row.muted ? " agents-personal-row--muted" : ""}`}
      >
        <h3 className="agents-card-title">
          <span
            className="agents-title-main"
            style={row.muted ? { color: "var(--muted)" } : undefined}
          >
            {row.titleMain}
          </span>
        </h3>
        {row.bullets && (
          <ul className="agents-list">
            {row.bullets.map((b) => (
              <li key={b}>{b}</li>
            ))}
          </ul>
        )}
        {row.moreText && <p className="agents-personal-more">{row.moreText}</p>}
        {row.ctaHref && (
          <Link to={row.ctaHref} className="agents-personal-cta">
            See it in action{" "}
            <span className="agents-personal-cta-arrow">→</span>
          </Link>
        )}
        {row.subText && <p className="agents-personal-sub">{row.subText}</p>}
      </div>
    ))}
  </div>
);

const PANEL_BODY: Record<TabKey, () => JSX.Element> = {
  inside: InsidePanelBody,
  work: WorkPanelBody,
  personal: PersonalPanelBody,
};

const HomeProducts = () => {
  const [activeProduct, setActiveProduct] = useState<TabKey | null>(null);

  const toggle = (key: TabKey) => (e: React.MouseEvent) => {
    e.stopPropagation();
    setActiveProduct((prev) => (prev === key ? null : key));
  };

  return (
    <section className="products" id="products">
      <div className="container">
        <div className="section-header">
          <span className="section-eyebrow">Jobs We Get Done</span>
          <h2>
            The work you're struggling with?{" "}
            <span className="accent">AI handles it.</span>
          </h2>
        </div>

        <div className="products-grid" id="products-grid">
          {PRODUCTS.map((product) => {
            const isActive = activeProduct === product.key;
            const PanelBody = PANEL_BODY[product.key];
            return (
              <div
                key={product.key}
                className="product-group"
                data-product={product.key}
              >
                <div
                  className={`product-card${isActive ? " active" : ""}`}
                  data-product={product.key}
                >
                  <span className="product-audience-label">
                    {product.audienceLabel}
                  </span>
                  <span className="product-tag">{product.tag}</span>
                  <h3>{product.title}</h3>
                  <p className="product-desc">{product.desc}</p>
                  <span
                    className="product-see-more"
                    onClick={toggle(product.key)}
                  >
                    <span className="see-more-default">Meet the specialist</span>
                    <span className="see-more-active">Hide</span>
                  </span>
                </div>
                <div
                  className={`product-panel${isActive ? " active" : ""}`}
                  id={`tab-${product.key}`}
                >
                  <div className="product-tree-connector" />
                  <div className="product-panel-inner">
                    <PanelBody />
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default HomeProducts;
