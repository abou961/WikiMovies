import React, { useState, useMemo } from "react";
import AppContext from "./context";

const AppProvider = (props) => {
  const [recherche, setRecherche] = useState("");

  const appContext = useMemo(
    () => ({
      recherche,
      setRecherche,
    }),
    [recherche, setRecherche]
  );

  return (
    <AppContext.Provider value={appContext}>
      {props.children}
    </AppContext.Provider>
  );
};

export default AppProvider;
