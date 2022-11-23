import React from "react";
import HarryPotterImage from "../misc/images/HP5.jpg";
import { useNavigate } from "react-router-dom";

const FilmBox = (props) => {
  
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/film/${props.idFilm}`);
  }
  
  return (
    <div   className="inline-block px-3">
      <button onClick={handleClick} className="group/edit relative w-64 h-64 max-w-xs overflow-hidden rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300 ease-in-out">
      <img
        src={props.imageUrl}
        alt="film"
        className="rounded-lg object-cover h-full w-full"
      />
      <div className="flex flex-col py-2 justify-center absolute group-hover/edit:h-full transition-h duration-100 ease-in-out bottom-0 w-full">
        <div className="absolute bg-black opacity-80 w-full h-full z-10"></div>
        <p id="title" className="group-hover/edit:text-2xl transition-text duration-100 ease-in-out font-poppins font-semibold text-md text-white z-30 px-2 pb-1">
          {props.title}
        </p>
        <p id="duration" className="group-hover/edit:text-xl transition-text duration-100 ease-in-out group-hover/edit:pb-16 transition-pb duration-100 ease-in-out font-poppins text-sm font-semibold text-rose-900 z-20">
          {props.duration} min
        </p>
      </div>
    </button>
    </div>
  );
};

export default FilmBox;
