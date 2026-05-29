import { Link } from "react-router-dom";

/**
 * Products section — mirrors home.html L4264–4309.
 * HTML uses <a href="inside.html"> etc.; React uses <Link to="/inside"> for SPA routing.
 * All class names, text content, and data-* attributes preserved verbatim from HTML.
 */
const HomeProducts = () => (
  <section className="products" id="products">
    <div className="container">
      <div className="section-header">
        <span className="section-eyebrow">Infina AI Products</span>
        <h2>
          Precision built for <span className="accent">your exact need</span>
        </h2>
      </div>

      <div className="products-grid" id="products-grid">
        {/* Card — Inside */}
        <div className="product-card" data-product="inside">
          <span className="product-audience-label">For Platforms</span>
          <span className="product-tag">Infina AI Inside</span>
          <h3>More engaged customer. Higher revenue. Zero build time.</h3>
          <ul className="product-bullets">
            <li>AI specialist integrated on your app/web</li>
            <li>Go live in weeks, not months</li>
            <li>Help your customer makes better financial decisions</li>
          </ul>
          <Link to="/inside" className="product-link">
            Explore AI Inside
          </Link>
        </div>

        {/* Card — Work */}
        <div className="product-card" data-product="work">
          <span className="product-audience-label">For Business</span>
          <span className="product-tag">Infina AI Work</span>
          <h3>Your team, working at their best with AI handling the rest.</h3>
          <ul className="product-bullets">
            <li>Integrate in Slack and Whatsapp</li>
            <li>Automates updates, tracking, and routine workflows 24/7</li>
            <li>
              Frees your team for decisions and the work that move business
              forward
            </li>
          </ul>
          <Link to="/work" className="product-link">
            Explore AI Work
          </Link>
        </div>

        {/* Card — Personal */}
        <div className="product-card" data-product="personal">
          <span className="product-audience-label">For Individuals</span>
          <span className="product-tag">Infina AI Personal</span>
          <h3>Grow more. Stress less. Achieve your goal.</h3>
          <ul className="product-bullets">
            <li>Wealth management and personal finance, simplified</li>
            <li>Ask anything: savings, investments, loans, or insurance</li>
            <li>Plan trips, travels, and daily tasks with ease</li>
          </ul>
          <Link to="/personal" className="product-link">
            Explore AI Personal
          </Link>
        </div>
      </div>
    </div>
  </section>
);

export default HomeProducts;
