import { useEffect, useRef, useState } from "react";
import { useStepSequence } from "@/components/landing-v2/hooks/use-step-sequence";
import type { AgentTab } from "./realsalex-content-data";
import { BUILD_STEPS, demoTabCopy } from "./realsalex-demo-card-copy-data";
import RealSaleXDemoChat from "./RealSaleXDemoChat";

const TABS: AgentTab[] = ["buying", "listing"];
const STEP_INTERVAL_MS = 620;
const COPIED_RESET_MS = 1600;

interface RealSaleXDemoProps {
  tab: AgentTab;
  /** Each increment replays the "Building your advisor" sequence. */
  buildRunNonce: number;
}

/**
 * "What your client gets" demo card (#see-it-work). Mirrors
 * <section class="section demo-section" id="see-it-work"> in
 * Web-Infina-AI/realsalex-v2.html.
 *
 * Three stages share one card: idle (the chat demo), loading (scripted build
 * checklist) and built (share link). FRONT-END ONLY: nothing is created or
 * sent, the share link is a fixed sample per tab.
 * TODO: show the real advisor URL from the backend preview API once it is live.
 *
 * The build stage survives a tab switch (only its copy changes), the chat
 * resets to its first persona; both match the source.
 */
const RealSaleXDemo = ({ tab, buildRunNonce }: RealSaleXDemoProps) => {
  const copy = demoTabCopy[tab];
  const { status, step, start, reset } = useStepSequence(BUILD_STEPS.length, STEP_INTERVAL_MS);
  const [copied, setCopied] = useState(false);
  const copiedTimer = useRef<number>();

  useEffect(() => {
    if (buildRunNonce > 0) start();
  }, [buildRunNonce, start]);

  useEffect(() => () => window.clearTimeout(copiedTimer.current), []);

  const copyLink = () => {
    navigator.clipboard?.writeText(copy.shareLink).catch(() => {});
    setCopied(true);
    window.clearTimeout(copiedTimer.current);
    copiedTimer.current = window.setTimeout(() => setCopied(false), COPIED_RESET_MS);
  };

  return (
    <section className="section demo-section" id="see-it-work">
      <div className="container">
        <div className="section-head reveal">
          {TABS.map((key) => (
            <div key={key} className="tab-copy" hidden={key !== tab}>
              <h2>
                {demoTabCopy[key].heading.title}
                <span className="accent">{demoTabCopy[key].heading.accent}</span>
              </h2>
              <p>{demoTabCopy[key].heading.sub}</p>
            </div>
          ))}
        </div>
        <div className="demo-wrap reveal">
          <div className="demo-card">
            <div className="demo-card-head">
              <div className="who">
                <b>{copy.advisorName}</b>
                <span>{copy.brokerage}</span>
              </div>
              <span className="demo-live-tag">Live · answers 24/7</span>
            </div>

            {TABS.map((key) => {
              const [main, ...thumbs] = demoTabCopy[key].gallery;
              return (
                <div key={key} className="tab-copy" hidden={key !== tab}>
                  <div className="demo-gallery">
                    <div className="demo-gallery-main">
                      <img src={main.src} alt={main.alt} loading="lazy" />
                    </div>
                    <div className="demo-gallery-side">
                      {thumbs.map((img, i) => {
                        const isLast = i === thumbs.length - 1;
                        return (
                          <div key={img.src} className={`demo-gallery-thumb${isLast ? " demo-gallery-more" : ""}`}>
                            <img src={img.src} alt={img.alt} loading="lazy" />
                            {isLast && <span className="demo-gallery-more-tag">See all 5 photos</span>}
                          </div>
                        );
                      })}
                    </div>
                  </div>
                  <div className="demo-specs">
                    <b>{demoTabCopy[key].address}</b>
                    {demoTabCopy[key].specs.map((spec) => (
                      <span key={spec}>{spec}</span>
                    ))}
                  </div>
                </div>
              );
            })}

            <RealSaleXDemoChat key={tab} tab={tab} hidden={status !== "idle"} />

            <div className="demo-loading" hidden={status !== "running"}>
              <h3>{copy.loadingTitle}</h3>
              <div className="demo-steps">
                {BUILD_STEPS.map((label, i) => (
                  <div key={label} className={`demo-step${i < step ? " is-done" : ""}`}>
                    <span className="mark">{i < step ? "✓" : "·"}</span>
                    <span className="lbl-t">{label}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="demo-built" hidden={status !== "done"}>
              <span className="tag-ready">Ready to send</span>
              <h3>{copy.builtTitle}</h3>
              <p>
                It has read the listing, the county records and the disclosure. Send this link instead of the
                listing, and you'll see every question your buyer asks.
              </p>
              <div className="demo-link-row">
                <span>{copy.shareLink}</span>
                <button type="button" className="btn-secondary" onClick={copyLink}>
                  {copied ? "Copied" : "Copy link"}
                </button>
              </div>
              <div className="demo-built-actions">
                <button type="button" className="btn-ghost" onClick={reset}>
                  Back to the example
                </button>
              </div>
            </div>

            <div className="demo-footer" hidden={status === "running"}>
              {copy.footer}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default RealSaleXDemo;
