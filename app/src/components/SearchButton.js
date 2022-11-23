import React, { useContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import AppContext from "../context";
import ApiService from "../AppService";

const SearchButton = () => {

  const context = useContext(AppContext);
  const navigate = useNavigate();
  const [enableClick, setEnableClick] =useState(false);

  useEffect(() => {
    if(context.recherche === "") {
      setEnableClick(false);
    } else {
      setEnableClick(true);
    }
  }, [context.recherche]);

  const handleClick = () => {
    if (1) {
      navigate(`/search/${context.recherche}`);
    }
  };

  return (
    <button
      type="button"
      onClick={handleClick}
      className="rounded-tr-lg rounded-br-lg h-12 text-white bg-rose-900 transition duration-300 ease-out disabled:bg-white flex place-items-center pl-4 pr-4 font-poppins"
      disabled={!enableClick}
    >
      Search
    </button>
  );
};

export default SearchButton;
