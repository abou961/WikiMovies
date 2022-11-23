import React, { useState, useEffect } from "react";
import ApiService from "../AppService";
import { useParams, Link } from "react-router-dom";
import NavBar from "../components/NavBar";
import ButtonReturn from "../components/ButtonReturn";

import loadingGIF from "../misc/images/loading.gif";
// page qui donne les infos d'un film
const SeriesPage = () => {

  const [responseSeries, setResponseSeries] = useState("");
  const [isDataFetched, setIsDataFetched] = useState(false);
  const [seriesExist, setSeriesExist] = useState(true);
  const { idSeries } = useParams();

  useEffect(() => {
    ApiService.getSeries(idSeries)
      .then((res) => {
        if(JSON.stringify(res).length < 10) {
          setIsDataFetched(true);
          setSeriesExist(false);
        } else {
          setResponseSeries(res);
          if(!isDataFetched) {
            setIsDataFetched(true);
          }
          if (!seriesExist) {
            setSeriesExist(true);
          }
        }

      })
      .catch((error) => {
        setIsDataFetched(true);
        setSeriesExist(false);
      });
  }, []);

  const movies = responseSeries.movies;
  const casting = responseSeries.cast;
  const producers = responseSeries.producer;

  // const [linkImage, setLinkImage] = useState("");
  // setLinkImage("https://static01.nyt.com/images/2013/12/27/multimedia/movies-wolf-12272013/movies-wolf-12272013-superJumbo.jpg")
  return (
    <div className="bg-blacked font-poppins flex-col items-stretch h-screen text-gray-200  overflow-y-auto hide-scroll-bar">
      <NavBar />
      <div className="pt-24">
      {isDataFetched && seriesExist && (
      <>
        <div
          id="header"
          className="flex flex-row items-center justify-center bg-cover bg-center relative w-100 h-72 bg-white overflow-hidden"
          style={{ backgroundImage: `url(${responseSeries.img})` }}
        >
          <h1 className="relative z-10 font-bold font-poppins text-6xl">
            {responseSeries.title}
          </h1>
          <div className="absolute bg-black opacity-50 w-full h-full">
          </div>
        </div>
        <div id="contenu" className="pt-12 pl-24 pr-24 pb-24">
          <div className="font-semibold text-xl mt-4 mb-2">Synopsis</div>
          <div className="text-sm max-h-24 overflow-hidden">
            {responseSeries.resume}
          </div>
          <div className="flex flex-row">
          <div className="flex flex-col w-1/3 order-1">
              <h3 className="font-semibold text-xl mt-4 mb-2">Films</h3>
              {movies.map((movie,index) => (
                <Link className="hover:text-rose-900 hover:underline" key={index} to={`/film/wd:${movie[1]}`}>{movie[0]}</Link>
              ))}
          </div>
            <div className="flex flex-col w-1/3 order-3">
              <h3 className="font-semibold text-xl mt-4 mb-2">Producers</h3>
              <ul className="text-sm">
                {producers.map((name,index) => (<li key={index}><Link className="hover:text-rose-900 hover:underline" to={`/person/wd:${name[1]}`}>{name[0]}</Link></li>))}
              </ul>
            </div>
            <div className="flex flex-col w-1/3 order-2">
              <h3 className="font-semibold text-xl mt-4 mb-2 ">Cast members</h3>
              <ul className="text-sm">
              {casting.map((name, index) => (<li key={index}><Link className="hover:text-rose-900 hover:underline" to={`/person/wd:${name[1]}`}>{name[0]}</Link></li>))}
              </ul>
            </div>
          </div>
        </div>
      </>
      )}
      {!isDataFetched && seriesExist && (
        <div className="flex flex-col pt-32 items-center">
        <img
          src={loadingGIF}
          alt="chargement"
          className="w-1/6"
          max-width="100px"
        />
      </div>
      )}
      {isDataFetched && !seriesExist && (
          <div className="flex flex-col mt-24 items-center justify-center">
            <div className="font-poppins text-center text-2xl mb-8 text-white font-medium">
              This Series doesn't have an English Wiki Page
            </div>
            <ButtonReturn />
          </div>
        )}
      </div>
    </div>
  );
};

export default SeriesPage;
