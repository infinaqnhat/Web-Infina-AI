import { compareCopy } from "./realsalex-content-data";
import type { AgentTab } from "./realsalex-content-data";
import { RealSaleXIcon } from "./realsalex-icons";

const TABS: AgentTab[] = ["buying", "listing"];

/**
 * "The same buyer, two experiences" / "The same yard sign, two outcomes":
 * a Today vs With Home Concierge (or Property Expert) table plus a pull quote.
 * Mirrors the first plain <section class="section"> after the hero in
 * Web-Infina-AI/realsalex-v2.html.
 *
 * Both tab variants stay mounted and only the active one is shown, as in the
 * source, so the page-level reveal observer sees every `.reveal` up front.
 */
const RealSaleXCompare = ({ tab }: { tab: AgentTab }) => (
  <section className="section">
    <div className="container">
      {TABS.map((key) => {
        const copy = compareCopy[key];
        return (
          <div key={key} className="tab-copy" hidden={key !== tab}>
            <span className="eyebrow" style={{ textAlign: "center", display: "block" }}>
              {copy.eyebrow}
            </span>
            <div className="compare-heads reveal" style={{ marginTop: 8 }}>
              <div className="today">
                <b>{copy.today.head}</b>
                <span>{copy.today.sub}</span>
              </div>
              <div />
              <div className="advisor">
                <b>{copy.advisor.head}</b>
                <span>{copy.advisor.sub}</span>
              </div>
            </div>
            <div className="compare-table reveal">
              {copy.rows.map((row) => (
                <div key={row.today} className="compare-row">
                  <div className="compare-cell today">{row.today}</div>
                  <div className="compare-arrow">
                    <RealSaleXIcon name="arrowRight" size={20} />
                  </div>
                  <div className="compare-cell advisor">{row.advisor}</div>
                </div>
              ))}
            </div>
            <p className="pull-quote reveal" style={{ marginTop: "clamp(40px,5vw,64px)" }}>
              {copy.quote}
            </p>
          </div>
        );
      })}
    </div>
  </section>
);

export default RealSaleXCompare;
