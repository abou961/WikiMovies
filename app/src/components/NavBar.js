import React from 'react';
import SearchInput from './SearchInput';
import SearchButton from './SearchButton';
import { useNavigate } from "react-router-dom";

const NavBar = (props) => {

    const navigate = useNavigate();

    const handleClick = () => {
        navigate(`/`);
    }

    return (
        <div className="pl-12 pr-12 bg-blacked fixed flex h-24 flex-row items-center justify-between w-full z-40 ">
            <button onClick={handleClick} className="text-3xl text-gray-200 font-bold mr-16 font-poppins flex-row flex">
                Netfl'<p className='text-rose-900'>IF</p>
            </button>
            <div className='flex flex-row w-1/2'>
                <SearchInput inputSearch={props.inputSearch} />
                <SearchButton />
            </div>
        </div>
    );
}

export default NavBar;