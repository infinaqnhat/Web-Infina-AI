import { useState } from "react";
import { useRevealOnScroll } from "@/components/landing-v2/hooks/use-reveal-on-scroll";
import { UPLOADS, heroStats } from "./realsalex-content-data";

const TVC_SRC = `${UPLOADS}/realsalex-tvc.mp4`;
const TVC_POSTER = `${UPLOADS}/realsalex-tvc-poster.jpg`;

/**
 * RealSaleXHero — copy left, click-to-play TVC right.
 * Mirrors <header class="hero"> in Web-Infina-AI/realsalex.html.
 *
 * The video element is only mounted after the first click, matching the source
 * page's inline script: the poster keeps LCP fast and the MP4 is never fetched
 * until the visitor asks for it.
 */
const RealSaleXHero = () => {
  const revealRef = useRevealOnScroll<HTMLElement>();
  const [playing, setPlaying] = useState(false);

  return (
    <header className="hero" ref={revealRef}>
      <div className="hero-bg" />
      <div className="hero-grid-bg" />
      <div className="container hero-grid">
        <div className="hero-copy">
          <h1>
            Sell like a team of two. <span className="accent">On your own.</span>
          </h1>
          <p className="hero-sub">
            Real Sale X works alongside you: it answers your buyers 24/7, nurtures every deal, and
            pings you with a ready-to-send message the moment a buyer is ready to act.
          </p>
          <p className="hero-note">
            It handles the follow-up and admin, so you spend more time closing, not chasing.
          </p>
          <div className="hero-ctas">
            <a href="#see-it-work" className="btn-primary">
              See how it works
            </a>
          </div>
          <div className="hero-stats">
            {heroStats.map((s) => (
              <div key={s.label}>
                <strong>{s.value}</strong>
                <span>{s.label}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="hero-visual reveal">
          <div
            className="hero-video"
            style={playing ? { cursor: "default" } : undefined}
            onClick={() => setPlaying(true)}
          >
            {playing ? (
              // autoPlay mirrors the source script, which calls play() right after insert.
              <video src={TVC_SRC} poster={TVC_POSTER} controls autoPlay playsInline preload="auto" />
            ) : (
              <>
                <img
                  className="hero-video-poster"
                  src={TVC_POSTER}
                  alt="Real Sale X, watch the film"
                  loading="eager"
                  fetchPriority="high"
                  width={1920}
                  height={1080}
                />
                <button className="hero-play" type="button" aria-label="Play the Real Sale X film">
                  <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true">
                    <path d="M8 5v14l11-7z" fill="currentColor" />
                  </svg>
                </button>
                <span className="hero-video-label">Watch the film · 0:48</span>
                <a className="hero-video-fallback" href={TVC_SRC}>
                  Watch the Real Sale X film
                </a>
              </>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};

export default RealSaleXHero;
