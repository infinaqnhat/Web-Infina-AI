import { Route, Routes } from "react-router-dom";
import LandingLayout from "@/pages/landing/LandingLayout";
import LandingHome from "@/pages/landing/LandingHome";
import LandingWork from "@/pages/landing/LandingWork";
import LandingPersonal from "@/pages/landing/LandingPersonal";
import LandingInside from "@/pages/landing/LandingInside";
import LandingAbout from "@/pages/landing/LandingAbout";
import LandingFocusAlignment from "@/pages/landing/LandingFocusAlignment";

// Route table mirrors PFA's landing routes verbatim (path -> page), so a page
// verified here behaves the same once synced. PFA owns these routes inside its
// larger App router; here they are the whole app.
const App = () => (
  <Routes>
    <Route element={<LandingLayout />}>
      <Route path="/" element={<LandingHome />} />
      <Route path="/work" element={<LandingWork />} />
      <Route path="/personal" element={<LandingPersonal />} />
      <Route path="/inside" element={<LandingInside />} />
      <Route path="/about" element={<LandingAbout />} />
      <Route path="/focus-alignment" element={<LandingFocusAlignment />} />
    </Route>
  </Routes>
);

export default App;
