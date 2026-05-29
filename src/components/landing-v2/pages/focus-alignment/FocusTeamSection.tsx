import { useEffect, useRef } from "react";

/**
 * FocusTeamSection — "Built for the whole team" section.
 * Source-mirrored from Web-Infina-AI/focus-alignment.html team section (lines 454–570).
 * 2-col: left = eyebrow + h2 + 4 feature cells, right = team mockup (3 member rows).
 */
const FocusTeamSection = () => {
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    const section = sectionRef.current;
    if (!section) return;
    const revealEls = section.querySelectorAll<HTMLElement>(".reveal");
    const observers: IntersectionObserver[] = [];
    revealEls.forEach((el) => {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("visible");
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.1 }
      );
      observer.observe(el);
      observers.push(observer);
    });
    return () => observers.forEach((o) => o.disconnect());
  }, []);

  return (
    <section className="section team-section" ref={sectionRef}>
      <div className="container">
        <div className="team-grid reveal">
          {/* Left: content */}
          <div className="team-content">
            <p className="team-eyebrow">Team &amp; Org</p>
            <h2>
              Built for the whole team{" "}
              <span className="accent-blue-text">not just the manager.</span>
            </h2>
            <p>
              See every direct report's active priorities in one view. Spot
              bottlenecks before they become blockers. Keep the org chart
              accurate so everyone knows who owns what.
            </p>
            <div className="team-features">
              <div className="team-feature">
                <h4>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
                    <circle cx="9" cy="7" r="4" />
                    <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
                    <path d="M16 3.13a4 4 0 0 1 0 7.75" />
                  </svg>
                  My Team
                </h4>
                <p>
                  Manage your direct reports and oversee their active priorities
                  across Focus, Queue, and Blocked statuses.
                </p>
              </div>
              <div className="team-feature">
                <h4>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <rect x="3" y="3" width="7" height="7" />
                    <rect x="14" y="3" width="7" height="7" />
                    <rect x="14" y="14" width="7" height="7" />
                    <rect x="3" y="14" width="7" height="7" />
                  </svg>
                  Org Chart
                </h4>
                <p>
                  Visual org structure with clear reporting lines. Search by
                  name, email, or position.
                </p>
              </div>
              <div className="team-feature">
                <h4>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
                    <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                  </svg>
                  Role-based access
                </h4>
                <p>
                  Everyone sees what's relevant to them. Sensitive priorities
                  stay private.
                </p>
              </div>
              <div className="team-feature">
                <h4>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <polyline points="23 4 23 10 17 10" />
                    <path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10" />
                  </svg>
                  Real-time sync
                </h4>
                <p>
                  Updates from any team member reflect instantly across the
                  whole team view.
                </p>
              </div>
            </div>
          </div>

          {/* Right: team mockup */}
          <div className="team-mockup">
            <div className="team-mockup-header">
              <span className="team-mockup-title">My Team · 3 direct reports</span>
              <div className="team-mockup-search">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <circle cx="11" cy="11" r="8" />
                  <line x1="21" y1="21" x2="16.65" y2="16.65" />
                </svg>
                Search teammates
              </div>
            </div>

            {/* Nathan */}
            <div className="team-member-row">
              <div>
                <div className="team-avatar" style={{ background: "#1863dc" }}>NA</div>
              </div>
              <div>
                <div className="team-member-name">Nathan</div>
                <div className="team-member-role" style={{ marginBottom: 10 }}>
                  Marketing Manager
                </div>
                <div className="team-tasks">
                  <div className="team-task-row">
                    <span className="team-task-id">KR-358</span>
                    <span className="team-task-name">Landing page</span>
                    <span className="status-tag status-focus">Focus</span>
                  </div>
                  <div className="team-task-row">
                    <span className="team-task-id">KR-355</span>
                    <span className="team-task-name">Logo redesign</span>
                    <span className="status-tag status-queue">Queue</span>
                  </div>
                </div>
              </div>
            </div>

            {/* Daniel */}
            <div className="team-member-row">
              <div>
                <div className="team-avatar" style={{ background: "#0891b2" }}>DA</div>
              </div>
              <div>
                <div className="team-member-name">Daniel</div>
                <div className="team-member-role" style={{ marginBottom: 10 }}>
                  Senior Designer
                </div>
                <div className="team-tasks">
                  <div className="team-task-row">
                    <span className="team-task-id" style={{ color: "#1863dc" }}>SHP-568</span>
                    <span className="team-task-name">Website merge</span>
                    <span className="status-tag status-focus">Focus</span>
                  </div>
                  <div className="team-task-row">
                    <span className="team-task-id">KR-362</span>
                    <span className="team-task-name">Brand system</span>
                    <span className="status-tag status-blocked">Blocked</span>
                  </div>
                </div>
              </div>
            </div>

            {/* Kevin */}
            <div className="team-member-row">
              <div>
                <div className="team-avatar" style={{ background: "#ea580c" }}>KE</div>
              </div>
              <div>
                <div className="team-member-name">Kevin</div>
                <div className="team-member-role" style={{ marginBottom: 10 }}>
                  Senior Engineer
                </div>
                <div className="team-tasks">
                  <div className="team-task-row">
                    <span className="team-task-id">KR-371</span>
                    <span className="team-task-name">API rate limits</span>
                    <span className="status-tag status-focus">Focus</span>
                  </div>
                  <div className="team-task-row">
                    <span className="team-task-id">KR-364</span>
                    <span className="team-task-name">SSO rollout</span>
                    <span className="status-tag status-done">Done</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default FocusTeamSection;
