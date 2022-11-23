import React from "react";
import { useNavigate } from "react-router-dom";

const PreviewFilm = (props) => {

  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/film/${props.id}`);
  };

  return (
    <div className="container flex flex-row gap-5 h-48 font-poppins">
      <button type="button" onClick={handleClick} className="w-3/5">
        <img src={props.image} alt="film" className="w-full h-full object-cover rounded-md hover:brightness-50 hover:ease-out hover:duration-200 hover:-translate-y-1 "/>
      </button>
      <div className="flex flex-col">
      <button type="button" onClick={handleClick} className="text-white text-left text-xl hover:text-gray-500 hover:underline font-poppins font-semibold">
          {props.title}
        </button>
        <div className="text-white text-sm font-poppins font-medium">
          {props.duration}
        </div>
        <div className="text-sm text-white mt-6 font-light">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </div>
      </div>
    </div>
  );
};

export default PreviewFilm;
