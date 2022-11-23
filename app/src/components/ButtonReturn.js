import React from "react";

const ButtonReturn = () => {
    const handleClick = () => {
        window.history.back();
    };

    return ( 
        <button
            type="button"
            onClick={handleClick}
            className="rounded-lg h-12 w-24 text-center text-blacked bg-white transition duration-300 ease-out hover:bg-gray-300 pl-4 pr-4 font-poppins"
        >
            Return
        </button>
     );
}
 
export default ButtonReturn;