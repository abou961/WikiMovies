import React from "react";

const AppContext = React.createContext({
  recherche: null,
  setRecherche: () => null,
});

export default AppContext;
