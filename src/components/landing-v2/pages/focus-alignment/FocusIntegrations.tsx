import { useEffect, useRef } from "react";

/**
 * FocusIntegrations — 7-logo integrations grid section.
 * Source-mirrored from Web-Infina-AI/focus-alignment.html integrations section (lines 571–621).
 * Inline SVG brand logos: Slack, Google Workspace, Microsoft 365, Notion, GitHub, Linear, Zapier.
 */
const FocusIntegrations = () => {
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
    <section className="section integrations-section" ref={sectionRef}>
      <div className="container">
        <div className="section-header reveal">
          <p className="section-label">Integrations</p>
          <h2>
            Works with the tools your team{" "}
            <span className="accent-blue-text">already uses.</span>
          </h2>
          <p>No "rip and replace." Connect in minutes.</p>
        </div>

        <div className="integrations-grid reveal">
          {/* Slack */}
          <div className="integration-card">
            <svg width="36" height="36" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 122.8 122.8">
              <path d="M25.8 77.6c0 7.1-5.8 12.9-12.9 12.9S0 84.7 0 77.6s5.8-12.9 12.9-12.9h12.9v12.9zm6.5 0c0-7.1 5.8-12.9 12.9-12.9s12.9 5.8 12.9 12.9v32.3c0 7.1-5.8 12.9-12.9 12.9s-12.9-5.8-12.9-12.9V77.6z" fill="#e01e5a"/>
              <path d="M45.2 25.8c-7.1 0-12.9-5.8-12.9-12.9S38.1 0 45.2 0s12.9 5.8 12.9 12.9v12.9H45.2zm0 6.5c7.1 0 12.9 5.8 12.9 12.9s-5.8 12.9-12.9 12.9H12.9C5.8 58.1 0 52.3 0 45.2s5.8-12.9 12.9-12.9h32.3z" fill="#36c5f0"/>
              <path d="M97 45.2c0-7.1 5.8-12.9 12.9-12.9s12.9 5.8 12.9 12.9-5.8 12.9-12.9 12.9H97V45.2zm-6.5 0c0 7.1-5.8 12.9-12.9 12.9s-12.9-5.8-12.9-12.9V12.9C64.7 5.8 70.5 0 77.6 0s12.9 5.8 12.9 12.9v32.3z" fill="#2eb67d"/>
              <path d="M77.6 97c7.1 0 12.9 5.8 12.9 12.9s-5.8 12.9-12.9 12.9-12.9-5.8-12.9-12.9V97h12.9zm0-6.5c-7.1 0-12.9-5.8-12.9-12.9s5.8-12.9 12.9-12.9h32.3c7.1 0 12.9 5.8 12.9 12.9s-5.8 12.9-12.9 12.9H77.6z" fill="#ecb22e"/>
            </svg>
            <span>Slack</span>
          </div>

          {/* Google Workspace */}
          <div className="integration-card">
            <svg width="36" height="36" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
              <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
              <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
              <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
            </svg>
            <span>Google Workspace</span>
          </div>

          {/* Microsoft 365 */}
          <div className="integration-card">
            <svg width="36" height="36" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M11 11H3V3h8v8z" fill="#F25022"/>
              <path d="M21 11h-8V3h8v8z" fill="#7FBA00"/>
              <path d="M11 21H3v-8h8v8z" fill="#00A4EF"/>
              <path d="M21 21h-8v-8h8v8z" fill="#FFB900"/>
            </svg>
            <span>Microsoft 365</span>
          </div>

          {/* Notion */}
          <div className="integration-card">
            <svg width="36" height="36" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="currentColor">
              <rect width="24" height="24" rx="4" fill="#000"/>
              <text x="6" y="17" fontSize="14" fontWeight="900" fill="#fff" fontFamily="serif">N</text>
            </svg>
            <span>Notion</span>
          </div>

          {/* GitHub */}
          <div className="integration-card">
            <svg width="36" height="36" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path fillRule="evenodd" clipRule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" fill="#181717"/>
            </svg>
            <span>GitHub</span>
          </div>

          {/* Linear */}
          <div className="integration-card">
            <svg width="36" height="36" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
              <rect width="100" height="100" rx="20" fill="#5E6AD2"/>
              <path d="M17.5 72.5L27.5 82.5L82.5 27.5L72.5 17.5L17.5 72.5Z" fill="white"/>
              <path d="M17.5 50L50 17.5L72.5 17.5L17.5 72.5L17.5 50Z" fill="white" opacity="0.6"/>
              <path d="M50 82.5L82.5 50L82.5 72.5L72.5 82.5L50 82.5Z" fill="white" opacity="0.6"/>
            </svg>
            <span>Linear</span>
          </div>

          {/* Zapier */}
          <div className="integration-card">
            <svg width="36" height="36" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
              <rect width="100" height="100" rx="20" fill="#FF4A00"/>
              <text x="18" y="68" fontSize="56" fontWeight="900" fill="#fff" fontFamily="sans-serif">Z</text>
            </svg>
            <span>Zapier</span>
          </div>
        </div>

        <p className="integration-note reveal">
          Import your existing priorities from{" "}
          <strong>Asana</strong>, <strong>Notion</strong>, or{" "}
          <strong>Google Sheets</strong> in under 10 minutes.
        </p>
      </div>
    </section>
  );
};

export default FocusIntegrations;
