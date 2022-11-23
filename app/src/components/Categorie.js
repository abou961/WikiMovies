import React from 'react';
import FilmBox from './FilmBox';
import "./Categories.css";
const Categorie = (props) => {
  return (
      <div className=" font-poppins rounded-xl text-white px-8 ">
      <div className="flex flex-col m-auto p-auto">
      <h1 className="flex pb-5 px-2 font-bold text-2xl text-white">
              {props.name}
            </h1>
            <div className="flex overflow-x-auto pb-10 hide-scroll-bar">
              <div className="flex flex-nowrap">
              {props.listFilms.map((item, index) => {
                  return <FilmBox  key={index} title={item.title} duration={item.duration} idFilm={item.id} imageUrl={item.imageUrl}/>
                })
              }
              </div>
            </div>
      </div>
      </div>
  );
      
}

export default Categorie;