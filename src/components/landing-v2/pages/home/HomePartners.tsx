/**
 * Partners section — mirrors home.html `.partners` (eyebrow "Proud to work with"
 * then a full-width logo-image marquee).
 *
 * The track renders the logo set 3× so the `marquee-slide` keyframe loops
 * seamlessly at translateX(-33.333%) (one full set advanced per cycle).
 * Logos are mirrored to /landing-html/uploads/ by scripts/setup-harness-assets.mjs.
 */

interface PartnerLogo {
  src: string;
  alt: string;
}

const LOGOS: PartnerLogo[] = [
  { src: "/landing-html/uploads/Infina-logo.png", alt: "Infina" },
  { src: "/landing-html/uploads/Kafi-logo.svg", alt: "Kafi" },
  { src: "/landing-html/uploads/aaa-insurance.png", alt: "AAA Insurance Corporation" },
  { src: "/landing-html/uploads/sovico-group.png", alt: "Sovico Group" },
  { src: "/landing-html/uploads/savills-logo.svg", alt: "Savills" },
];

const HomePartners = () => (
  <section className="partners">
    <div className="container">
      <p className="partners-eyebrow">Proud to work with</p>
    </div>
    <div className="industry-marquee">
      <div className="industry-track">
        {[0, 1, 2].flatMap((pass) =>
          LOGOS.map((logo) => (
            <div
              className="industry-card"
              key={`${pass}-${logo.alt}`}
              aria-hidden={pass > 0 || undefined}
            >
              <img src={logo.src} alt={logo.alt} />
            </div>
          ))
        )}
      </div>
    </div>
  </section>
);

export default HomePartners;
