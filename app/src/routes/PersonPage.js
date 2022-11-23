import React, { useState, useEffect } from "react";
import Rating from "@mui/material/Rating";
import ApiService from "../AppService";
import { Link } from "react-router-dom";

import loadingGIF from "../misc/images/loading.gif";
import { useParams } from "react-router-dom";

import HarryPotterImage from "../misc/images/HP5.jpg";

import NavBar from "../components/NavBar";
import ButtonReturn from "../components/ButtonReturn";
// page qui donne les infos d'un film
const FilmPage = () => {
  const [responsePerson, setResponsePerson] = useState("");
  const [isDataFetched, setIsDataFetched] = useState(false);
  const [personExist, setPersonExist] = useState(true);
  const { idPerson } = useParams();

  useEffect(() => {
    ApiService.getPerson(idPerson)
      .then((res) => {
        console.log(res, JSON.stringify(res).length);
        if(JSON.stringify(res).length < 10) {
          setIsDataFetched(true);
          setPersonExist(false);
        } else {
          setResponsePerson(res);
          if (!isDataFetched) {
            setIsDataFetched(true);
          }
          if (!personExist) {
            setPersonExist(true);
          }
        }

      })
      .catch((error) => {
        setIsDataFetched(true);
        setPersonExist(false);
      });
  }, []);

  const occupations = responsePerson.occupation;
  const movies = responsePerson.movies;
  // const [linkImage, setLinkImage] = useState("");
  // setLinkImage("https://static01.nyt.com/images/2013/12/27/multimedia/movies-wolf-12272013/movies-wolf-12272013-superJumbo.jpg")
  return (
    <div className="bg-blacked font-poppins flex-col items-stretch h-screen text-gray-200  overflow-y-auto hide-scroll-bar">
      <NavBar />
      <div className="pt-24">
        {isDataFetched && personExist && (
          <>
            <div
              id="header"
              className="flex flex-row items-center justify-center bg-cover bg-center relative w-100 h-72 bg-white overflow-hidden"
              style={{ backgroundImage: `url(${responsePerson.image})` }}
            >
              <h1 className="relative z-10 font-bold font-poppins text-6xl">
                {responsePerson.prenoms[0]} {responsePerson.name}
              </h1>
              <div className="absolute bg-black opacity-50 w-full h-full"></div>
            </div>
            <div id="contenu" className="pt-12 pl-24 pr-24 pb-24">
              <div className="font-semibold text-xl mt-4 mb-2">Pays</div>
              <div className="text-sm max-h-24 overflow-hidden">
                {responsePerson.country}
              </div>
              <div className="flex flex-row">
                <div className="flex flex-col w-1/3 order-2">
                  <h3 className="font-semibold  text-xl mt-4 mb-2">Sexe</h3>
                  <h4 className="text-sm">{responsePerson.sex[0]}</h4>
                </div>
                <div className="flex flex-col w-1/3 order-3">
                  <h3 className="font-semibold text-xl mt-4 mb-2">
                    occupations
                  </h3>
                  <ul className="text-sm">
                    {occupations.map((name, index) => (
                      <li key={index}>{name}</li>
                    ))}
                  </ul>
                </div>
                <div className="flex flex-col w-1/3 order-1">
                  <h3 className="font-semibold text-xl mt-4 mb-2 ">Films</h3>
                  <ul className="text-sm">
                    {movies.map((name, index) => (
                      <li key={index}>
                        <Link className="hover:text-rose-900 hover:underline" to={`/film/${name[1]}`}>{name[0]}</Link>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </div>
          </>
        ) }
        {!isDataFetched && personExist && (
        <div className="flex flex-col pt-32 items-center">
          <img
            src={loadingGIF}
            alt="chargement"
            className="w-1/6"
          />
        </div>
      )}
        {isDataFetched && !personExist && (
          <div className="flex flex-col mt-24 items-center justify-center">
            <div className="font-poppins text-center text-2xl mb-8 text-white font-medium">
              This person doesn't have an English Wiki Page
            </div>
            <ButtonReturn />
          </div>
        )}
      </div>
    </div>
  );
};

export default FilmPage;
