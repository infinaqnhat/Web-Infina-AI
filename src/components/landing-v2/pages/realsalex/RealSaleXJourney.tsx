import { Fragment } from "react";
import { journeyStages } from "./realsalex-journey-data";
import type { JourneySectionCopy, JourneyStep } from "./realsalex-journey-data";
import { RealSaleXIcon } from "./realsalex-icons";

const lastIndex = journeyStages.length - 1;

/** First dot is filled blue, last is the green "done" dot, the rest are hollow. */
const dotModifier = (i: number) => (i === 0 ? " is-filled" : i === lastIndex ? " is-done" : "");

/** Card body shared by the stacked mobile card and the fanned desktop card. */
const StepText = ({ step, isLast }: { step: JourneyStep; isLast: boolean }) => (
  <>
    <div className="journey-head">
      <span className="aic-num">{step.num}</span>
      <h3>{step.title}</h3>
    </div>
    <p className="journey-sub">{step.sub}</p>
    <div className="journey-pill-row">
      <span className={`journey-icon${isLast ? " is-done" : ""}`}>
        <RealSaleXIcon name={step.icon} size={14} strokeWidth={isLast ? 2.5 : 2} />
      </span>
      <span className="journey-pill">{step.pill}</span>
    </div>
    <p>{step.text}</p>
  </>
);

/**
 * "How it works" journey: 4 step cards over an Exploration → Transaction
 * timeline. realsalex-v2.html renders it once per tab with different copy.
 *
 * Two layouts ship together and CSS shows one: .journey-mobile (stacked
 * cards, ≤900px) and .journey-desktop (fanned, rotated cards, ≥901px).
 */
const RealSaleXJourney = ({ copy, hidden }: { copy: JourneySectionCopy; hidden: boolean }) => {
  const { steps } = copy;
  return (
    <section className="section" hidden={hidden}>
      <div className="container">
        <div className="section-head reveal">
          <span className="eyebrow">{copy.eyebrow}</span>
          <h2>
            {copy.title}
            <span className="accent">{copy.accent}</span>
          </h2>
          <p>{copy.sub}</p>
        </div>

        <div className="journey-mobile reveal">
          {steps.map((step, i) => {
            const isLast = i === steps.length - 1;
            return (
              <Fragment key={step.num}>
                {i > 0 && (
                  <span className="journey-m-arrow">
                    <RealSaleXIcon name="arrowDown" size={18} strokeWidth={2.5} />
                  </span>
                )}
                <div className={`journey-m-card${isLast ? " is-last" : ""}`}>
                  <div className="journey-m-text">
                    <StepText step={step} isLast={isLast} />
                  </div>
                  <img className="journey-m-photo" src={step.photoMobile ?? step.photo} alt={step.alt} />
                </div>
              </Fragment>
            );
          })}
          <div className="journey-m-timeline">
            <div className="journey-m-track">
              <div className="journey-m-dots">
                {journeyStages.map((stage, i) => (
                  <div key={stage.stage} className="journey-m-dot-wrap">
                    <span className={`journey-m-dot${dotModifier(i)}`} />
                  </div>
                ))}
              </div>
            </div>
            <div className="journey-m-labels">
              {journeyStages.map((stage) => (
                <span key={stage.stage} className="journey-m-label">
                  {stage.stage}
                </span>
              ))}
            </div>
          </div>
        </div>

        <div className="journey-desktop reveal">
          <div className="journey-row">
            {steps.map((step, i) => (
              <Fragment key={step.num}>
                {i > 0 && (
                  <span className="journey-arrow">
                    <RealSaleXIcon name="arrowRight" size={16} strokeWidth={2.5} />
                  </span>
                )}
                <div className={`journey-card j-${i + 1}`}>
                  <img className="journey-photo" src={step.photo} alt={step.alt} />
                  <div className="journey-mask" />
                  <div className="journey-content">
                    <StepText step={step} isLast={i === steps.length - 1} />
                  </div>
                </div>
              </Fragment>
            ))}
          </div>
          <div className="journey-timeline">
            <div className="journey-track">
              <div className="journey-dots">
                {journeyStages.map((stage, i) => (
                  <div key={stage.stage} className="journey-dot-wrap">
                    <span className={`journey-dot${dotModifier(i)}`} />
                  </div>
                ))}
              </div>
            </div>
            <div className="journey-labels">
              {journeyStages.map((stage) => (
                <div key={stage.stage} className="journey-label">
                  <b>{stage.label}</b>
                  <span>{stage.stage}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default RealSaleXJourney;
