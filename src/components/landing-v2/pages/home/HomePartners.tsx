/**
 * Industries section — mirrors home.html industries block (eyebrow + headline +
 * sub, then a full-width icon-card marquee).
 *
 * The track renders the 7-industry set 3× so the `marquee-slide` keyframe can
 * loop seamlessly at translateX(-33.333%) (one full set advanced per cycle).
 * Class names + SVG icon paths match home.html verbatim.
 */

interface Industry {
  label: string;
  icon: React.ReactNode;
}

const INDUSTRIES: Industry[] = [
  {
    label: "Securities",
    icon: (
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
        <polyline points="22 7 13.5 15.5 8.5 10.5 2 17" />
        <polyline points="16 7 22 7 22 13" />
      </svg>
    ),
  },
  {
    label: "Insurance",
    icon: (
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
      </svg>
    ),
  },
  {
    label: "Fintech",
    icon: (
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
        <rect x="1" y="4" width="22" height="16" rx="2" ry="2" />
        <line x1="1" y1="10" x2="23" y2="10" />
      </svg>
    ),
  },
  {
    label: "Fund Management",
    icon: (
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none" />
        <path d="M9.5 3h5a1.5 1.5 0 0 1 1.5 1.5a3.5 3.5 0 0 1 -3.5 3.5h-1a3.5 3.5 0 0 1 -3.5 -3.5a1.5 1.5 0 0 1 1.5 -1.5" />
        <path d="M4 17v-1a8 8 0 1 1 16 0v1a4 4 0 0 1 -4 4h-8a4 4 0 0 1 -4 -4" />
      </svg>
    ),
  },
  {
    label: "Bank",
    icon: (
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
        <line x1="3" y1="22" x2="21" y2="22" />
        <rect x="6" y="2" width="12" height="20" rx="1" />
        <path d="M9 7h1m5 0h-1M9 12h1m5 0h-1M9 17h1m5 0h-1" />
      </svg>
    ),
  },
  {
    label: "e-Wallet",
    icon: (
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
        <rect x="5" y="2" width="14" height="20" rx="2" ry="2" />
        <line x1="12" y1="18" x2="12.01" y2="18" />
      </svg>
    ),
  },
  {
    label: "Travel",
    icon: (
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
        <circle cx="12" cy="12" r="10" />
        <line x1="2" y1="12" x2="22" y2="12" />
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
      </svg>
    ),
  },
];

const HomePartners = () => (
  <section className="partners">
    <div className="container">
      <p className="partners-eyebrow">Industries We Serve</p>
      <h2 className="partners-headline">Built for regulated industries.</h2>
      <p className="partners-sub">Trusted by financial services teams across Southeast Asia.</p>
    </div>
    <div className="industry-marquee">
      <div className="industry-track">
        {[0, 1, 2].flatMap((pass) =>
          INDUSTRIES.map((it) => (
            <div className="industry-card" key={`${pass}-${it.label}`} aria-hidden={pass > 0 || undefined}>
              <div className="industry-card-icon">{it.icon}</div>
              <span>{it.label}</span>
            </div>
          ))
        )}
      </div>
    </div>
  </section>
);

export default HomePartners;
