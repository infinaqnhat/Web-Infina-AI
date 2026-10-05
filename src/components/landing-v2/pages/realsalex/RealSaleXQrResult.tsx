import { useEffect } from "react";
import { useStepSequence } from "@/components/landing-v2/hooks/use-step-sequence";
import { UPLOADS } from "./realsalex-content-data";

const QR_STEPS = ["Reading the listing", "Generating your QR code", "Preparing your yard sign design"];
const STEP_INTERVAL_MS = 620;

/**
 * QR result panel under the Listing Agent hero ("Create Property Expert").
 * FRONT-END ONLY, demo visual: a scripted checklist, then a static sample QR
 * image. "Download QR Code" has no handler in the source either.
 *
 * Each increment of `runNonce` restarts the sequence; until the first run
 * the panel is not rendered (the source keeps it `hidden`).
 */
const RealSaleXQrResult = ({ runNonce }: { runNonce: number }) => {
  const { status, step, start } = useStepSequence(QR_STEPS.length, STEP_INTERVAL_MS);

  useEffect(() => {
    if (runNonce > 0) start();
  }, [runNonce, start]);

  if (status === "idle") return null;

  return (
    <div className="qr-result" id="qr-result">
      {status === "running" ? (
        <div className="qr-loading">
          <h4>Generating your QR code</h4>
          <div className="qr-steps">
            {QR_STEPS.map((label, i) => (
              <div key={label} className={`qr-step${i < step ? " is-done" : ""}`}>
                <span className="mark">{i < step ? "✓" : "·"}</span>
                <span>{label}</span>
              </div>
            ))}
          </div>
        </div>
      ) : (
        <div className="qr-built">
          <img src={`${UPLOADS}/qr-sample.png`} alt="Sample QR code for the listing" />
          <div className="qr-built-text">
            <b>Your QR code is ready.</b>
            <p>
              Print it on your yard sign or open house flyer. Visitors scan it to ask your Concierge about 124
              Oak Street, day or night.
            </p>
            <button type="button" className="btn-secondary">
              Download QR Code
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default RealSaleXQrResult;
