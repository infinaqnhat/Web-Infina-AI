import { Outlet } from "react-router-dom";

/**
 * LandingLayout — wraps all landing routes. Each child page renders its
 * own LandingNav + LandingFooter so per-page wrappers (`.{page}-page`)
 * scope their CSS correctly without an outer container interfering.
 */
const LandingLayout = () => (
  <div className="landing-root">
    <Outlet />
  </div>
);

export default LandingLayout;
