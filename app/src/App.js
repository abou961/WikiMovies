import React from "react";
import { RenderRoutes, ROUTES } from "./routes/routes";

function App() {
  return (
    <>
      <RenderRoutes routes={ROUTES} />
    </>
  );
}
export default App;
