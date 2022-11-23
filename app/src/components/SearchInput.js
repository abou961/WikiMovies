import React,{useContext} from 'react';
import AppContext from '../context';


const SearchInput = (props) => {
    const context = useContext(AppContext);

    return (
        <> 
            <input 
                onChange={(e) => {context.setRecherche(e.target.value)}} 
                type="text" 
                placeholder={props.inputSearch ? props.inputSearch : "Chercher un film" }
                className="h-12 focus:outline-none rounded-tl-lg rounded-bl-lg font-poppins pl-4 w-full"
            /> 
        </>
    );

}
 
export default SearchInput;