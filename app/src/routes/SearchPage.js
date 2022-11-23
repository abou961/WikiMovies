import React, { useState, useEffect, useContext } from "react";
import NavBar from "../components/NavBar";
import { useParams } from "react-router-dom";
import PreviewFilm from "../components/PreviewFilm";
import HarryPotterImage1 from "../misc/images/HP1.jpg";
import HarryPotterImage5 from "../misc/images/HP5.jpg";
import ApiService from "../AppService";
import AppContext from "../context";
import loadingGIF from "../misc/images/loading.gif";
import FilmBox from "../components/FilmBox.js"
// page qui présente les résultats d'une recherche
const SearchPage = () => {
  const [responseSearch, setResponseSearch] = useState("");
  const [isDataFetched, setIsDataFetched] = useState(false);
  const { input } = useParams();
  const context = useContext(AppContext);

  useEffect(() => {
    context.setRecherche(""); // vider le cache de l'input search
    ApiService.getSearchFilm(input)
    .then((res) => {
      console.log(res);
      setResponseSearch(res);
      if(!isDataFetched) {
        setIsDataFetched(true);
      }

    });
  }, [input]);

  const films = responseSearch.films;

  return (
    <div className="bg-blacked flex flex-col items-stretch h-screen overflow-y-auto">
      <NavBar inputSearch={input} />
      <div className="container mx-auto flex flex-col pl-12 mt-32 gap-5">
        {isDataFetched ? (
          <>
            <div className="font-poppins text-white font-bold text-2xl">
              Meilleurs Résultats 
            </div>
            <div className="flex flex-wrap gap-6">
              {films.map((item) => {
              if(item.image !== "") {
                return (
               <FilmBox
               key={item.id} title={item.name} duration={item.duration.substr(0,3)} idFilm={item.id} imageUrl={item.image}
               />
              )}})}
            </div>
          </>
        ) : (
          <div className="flex flex-col pt-32 items-center">
            <img
              src={loadingGIF}
              alt="chargement"
              className="w-1/6"
            />
          </div>
        )}
      </div>
    </div>
  );
};

export default SearchPage;
