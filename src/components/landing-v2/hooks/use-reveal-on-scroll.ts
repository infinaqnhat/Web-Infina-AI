import { useEffect, useRef } from "react";
import type { RefObject } from "react";

/**
 * Attaches the static pages' "reveal on scroll" behavior to a subtree.
 *
 * Mirrors the IntersectionObserver block the source HTML pages run inline:
 * every `.reveal` descendant gains `.visible` the first time it intersects,
 * then stops being observed. One observer serves the whole subtree.
 *
 * Lives under components/landing-v2/ so scripts/sync-landing-to-pfa.sh carries
 * it along with the components that import it — src/hooks/ is not synced.
 *
 * @param threshold visibility ratio that triggers the reveal; the source pages
 *                  use 0.12 on realsalex.html and 0.1 on the focus-alignment
 *                  sections, so callers pass their page's own value.
 */
export const useRevealOnScroll = <T extends HTMLElement>(
  threshold = 0.12
): RefObject<T> => {
  const rootRef = useRef<T>(null);

  useEffect(() => {
    const root = rootRef.current;
    if (!root) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold }
    );

    root.querySelectorAll<HTMLElement>(".reveal").forEach((el) => observer.observe(el));
    return () => observer.disconnect();
  }, [threshold]);

  return rootRef;
};
