import { finalCtaCopy, tabCta } from "./realsalex-content-data";
import type { AgentTab } from "./realsalex-content-data";
import RealSaleXListingUrlInput from "./RealSaleXListingUrlInput";

const TABS: AgentTab[] = ["buying", "listing"];

/**
 * Closing CTA band with a second "paste a listing" box. Mirrors
 * <section class="section final-cta"> in Web-Infina-AI/realsalex-v2.html.
 * The button label and note follow the active tab; `onCreate` runs the same
 * flow as the hero button (demo build on buying, QR panel on listing).
 */
const RealSaleXFinalCta = ({ tab, onCreate }: { tab: AgentTab; onCreate: () => void }) => (
  <section className="section final-cta">
    <div className="container">
      {TABS.map((key) => (
        <div key={key} className="tab-copy" hidden={key !== tab}>
          <h2>
            {finalCtaCopy[key].title}
            <br />
            <span className="accent">{finalCtaCopy[key].accent}</span>
          </h2>
          <p className="italic-line">{finalCtaCopy[key].line}</p>
        </div>
      ))}
      <div className="create-box final-create">
        <div className="create-row">
          <RealSaleXListingUrlInput id="url-2" />
          <button type="button" className="btn-primary" onClick={onCreate}>
            {tabCta[tab].label}
          </button>
        </div>
        <p className="create-note">{finalCtaCopy[tab].note}</p>
      </div>
    </div>
  </section>
);

export default RealSaleXFinalCta;
