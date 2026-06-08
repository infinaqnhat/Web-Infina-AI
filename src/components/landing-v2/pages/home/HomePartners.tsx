/**
 * Industries We Serve section — mirrors home.html `.partners` (eyebrow "Industries We Serve"
 * then a full-width industry image-card marquee).
 *
 * The track renders the industry set 3× so the `marquee-slide` keyframe loops
 * seamlessly at translateX(-33.333%) (one full set advanced per cycle).
 * Images are mirrored to /landing-html/uploads/ by scripts/setup-harness-assets.mjs.
 */

interface Industry {
  src: string;
  alt: string;
  label: string;
}

const INDUSTRIES: Industry[] = [
  { src: "/landing-html/uploads/Securities Icon.png", alt: "Securities", label: "Securities" },
  { src: "/landing-html/uploads/Insurance Icon.png", alt: "Insurance", label: "Insurance" },
  { src: "/landing-html/uploads/Fintech Icon.jpg", alt: "Fintech", label: "Fintech" },
  { src: "/landing-html/uploads/Fund Management Icon.png", alt: "Fund Management", label: "Fund Management" },
  { src: "/landing-html/uploads/Bank Icon.jpg", alt: "Bank", label: "Bank" },
  { src: "/landing-html/uploads/e-Wallet Icon.jpg", alt: "e-Wallet", label: "e-Wallet" },
  { src: "/landing-html/uploads/Travel Icon.jpg", alt: "Travel", label: "Travel" },
];

const HomePartners = () => (
  <section className="partners">
    <div className="container">
      <p className="partners-eyebrow">Industries We Serve</p>
    </div>
    <div className="industry-marquee">
      <div className="industry-track">
        {[0, 1, 2].flatMap((pass) =>
          INDUSTRIES.map((industry) => (
            <div
              className="industry-card"
              key={`${pass}-${industry.alt}`}
              aria-hidden={pass > 0 || undefined}
            >
              <img src={industry.src} alt={industry.alt} />
              <span>{industry.label}</span>
            </div>
          ))
        )}
      </div>
    </div>
  </section>
);

export default HomePartners;
