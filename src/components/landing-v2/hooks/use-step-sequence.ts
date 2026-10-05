import { useCallback, useEffect, useRef, useState } from "react";

export type StepSequenceStatus = "idle" | "running" | "done";

/**
 * Scripted "progress checklist" timer used by the front-end-only demo flows.
 *
 * Mirrors the static pages' setInterval pattern: `start()` resets to step 0,
 * then every `intervalMs` one more step is marked done. Once the counter
 * reaches `stepCount` the sequence flips to "done" instead of rendering the
 * final step, exactly like the source (the last checkmark is never shown,
 * the finished state replaces the list).
 *
 * `step` is the number of completed steps while running.
 */
export const useStepSequence = (stepCount: number, intervalMs: number) => {
  const [status, setStatus] = useState<StepSequenceStatus>("idle");
  const [step, setStep] = useState(0);
  const timerRef = useRef<number>();

  const start = useCallback(() => {
    window.clearInterval(timerRef.current);
    setStep(0);
    setStatus("running");
    let completed = 0;
    timerRef.current = window.setInterval(() => {
      completed += 1;
      if (completed >= stepCount) {
        window.clearInterval(timerRef.current);
        setStatus("done");
        return;
      }
      setStep(completed);
    }, intervalMs);
  }, [stepCount, intervalMs]);

  const reset = useCallback(() => {
    window.clearInterval(timerRef.current);
    setStatus("idle");
  }, []);

  // A running interval must not outlive the component that renders it.
  useEffect(() => () => window.clearInterval(timerRef.current), []);

  return { status, step, start, reset };
};
