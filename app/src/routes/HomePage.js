import React, { useContext } from "react";
import Categorie from "../components/Categorie";
import NavBar from "../components/NavBar";
import AppContext from "../context";
import "../components/Categories.css"

const HomePage = () => {
  const context = useContext(AppContext);
  const ListFilmsHorreur = [
    {
       id: "wd:Q64004122",
       title:"The Invisible Man",
       duration:"124",
       imageUrl:"https://i.pinimg.com/originals/61/eb/39/61eb391c12b79776f24d448489efe761.jpg"
    },
    {
       id: "wd:Q87519760",
       title:"Relic",
       duration:"89",
       imageUrl:"https://images6.alphacoders.com/343/343138.jpg"
    },
    {
       id: "wd:Q83826818",
       title:"His House",
       duration:"93",
       imageUrl:"https://images.hdqwalls.com/wallpapers/the-house-by-the-lake-5o.jpg"
    },
    {
       id: "wd:Q98114112",
       title:"Host",
       duration:"56",
       imageUrl:"https://wallpaperaccess.com/full/3539064.jpg"
    },
    {
       id: "wd:Q55402791",
       title:"The Lighthouse",
       duration:"109",
       imageUrl:"https://wallpapercave.com/wp/wp4755708.jpg"
    },
    {
       id: "wd:Q68681279",
       title:"Saint Maud",
       duration:"84",
       imageUrl:"https://wallpapercave.com/wp/wp6838241.jpg"
    },
    {
       id: "wd:Q55907451",
       title:"Midsommar",
       duration:"147",
       imageUrl:"https://wallpapercave.com/wp/wp4960585.jpg"
    },
    {
       id: "wd:Q64678948",
       title:"After Midnight",
       duration:"83",
       imageUrl:"https://c4.wallpaperflare.com/wallpaper/75/326/561/the-midnight-monsters-musica-music-hd-wallpaper-preview.jpg"
    },
    {
       id: "wd:Q56000996",
       title:"Us",
       duration:"112",
       imageUrl:"https://images3.alphacoders.com/100/thumb-1920-1001405.jpg"
    }
  ];
  const ListMeilleuresComedies = [
    {
       id: "wd:Q105438931",
       title:"I'm Your Man",
       duration:"108",
       imageUrl:"https://picfiles.alphacoders.com/469/thumb-469402.jpg"
    },
    {
       id: "wd:Q69303989",
       title:"Another Round",
       duration:"117",
       imageUrl:"https://assets.vogue.com/photos/6074a28d29d0bb7c9dffeabf/master/w_2560%2Cc_limit/002-Druk-Mads-Mikkelsen-Photo-By-Henrik%2520Ohsten.jpg"
    },
    {
       id: "wd:Q65084655",
       title:"Palm Springs",
       duration:"90",
       imageUrl:"https://images.unsplash.com/photo-1632429619634-3d97fc1693e9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8cGFsbSUyMHNwcmluZ3N8ZW58MHx8MHx8&w=1000&q=80"
    },
    {
       id: "wd:Q85806998",
       title:"The Duke",
       duration:"95",
       imageUrl:"https://wallpaperaccess.com/full/1291186.jpg"
    },
    {
       id: "wd:Q98078759",
       title:"Shiva Baby",
       duration:"78",
       imageUrl:"https://bholenathh.com/wp-content/uploads/2022/03/bholenath-picture.jpg"
    },
    {
       id: "wd:Q57982486",
       title:"Knives Out",
       duration:"130",
       imageUrl:"https://images8.alphacoders.com/105/thumb-1920-1052048.jpg"
    },
    {
       id: "wd:Q54862508",
       title:"Jojo Rabbit",
       duration:"108",
       imageUrl:"https://wallpapercave.com/wp/wp4764201.jpg"
    },
    {
       id: "wd:Q54959170",
       title:"Dolemite Is My Name",
       duration:"118",
       imageUrl:"https://static01.nyt.com/images/2019/10/04/arts/04DOLEMITE/04DOLEMITE-videoSixteenByNineJumbo1600-v5.jpg"
    },
    {
       id: "wd:Q61448040",
       title:"Parasite",
       duration:"132",
       imageUrl:"https://wallpapercave.com/wp/wp5510252.jpg"
    }
  ];
  const ListFilmsAction = [
    {
      id: "wd:Q189330",
      title: "The Dark Knight Rises",
      duration: "164",
      imageUrl: "https://wallpapercave.com/wp/wp383267.jpg"
    },
    {
      id: "wd:Q163872",
      title: "The Dark Knight",
      duration: "153",
      imageUrl: "https://images4.alphacoders.com/855/85508.jpg"
    },
    {
      id: "wd:Q61117344",
      title: "The Batman",
      duration: "176",
      imageUrl: "https://images.hdqwalls.com/wallpapers/2022-the-batman-movie-4k-g4.jpg"
    },
    {
      id: "wd:Q68934496",
      title: "Spider-Man: No Way Home",
      duration: "148",
      imageUrl: "https://cdn.wallpapersafari.com/30/28/2GuUqd.jpg"
    },
    {
      id: "wd:Q60834962",
      title: "Dune",
      duration: "155",
      imageUrl: "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/a58a7719-0dcf-4e0b-b7bb-d2b725dbbb8e/depapg5-059fd064-edd6-4eb9-9fc7-97ae7908e024.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2E1OGE3NzE5LTBkY2YtNGUwYi1iN2JiLWQyYjcyNWRiYmI4ZVwvZGVwYXBnNS0wNTlmZDA2NC1lZGQ2LTRlYjktOWZjNy05N2FlNzkwOGUwMjQucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.9hNOSCtnlopfm9--ARiB08UnlZ20B3OMYYPPivyR-zc"
    },
    {
      id: "wd:Q65065595",
      title: "The Old Guard",
      duration: "125",
      imageUrl: "https://images5.alphacoders.com/117/1179107.jpg"
    },
    {
      id: "wd:Q55106022",
      title: "Extreme Job",
      duration: "111",
      imageUrl: "https://m.media-amazon.com/images/M/MV5BNjg5MGEzYjktMTRmMi00NTliLTg0MGQtNTJhN2NjMjc2YTU2XkEyXkFqcGdeQXVyNzI1NzMxNzM@._V1_.jpg"
    },
    {
      id: "wd:Q182692",
      title: "Apocalypse Now",
      duration: "153",
      imageUrl: "https://api-cdn.arte.tv/api/mami/v1/program/fr/083883-041-A/1920x1080?ts=1573649584&text=true"
    },
    {
      id: "wd:Q55081822",
      title: "Ford v Ferrari",
      duration: "152",
      imageUrl: "https://images.hdqwalls.com/wallpapers/ford-v-ferrari-movie-vw.jpg"
    },
    {
      id: "wd:Q55106098",
      title: "The Witch: Part 1. The Subversion",
      duration: "126",
      imageUrl: "https://images7.alphacoders.com/121/thumb-1920-1218864.jpg"
    }
  ];
  const ListCategories = [
    {
      title: "Action movies",
      listFilms: ListFilmsAction
    },
    {
      title: "Comedies",
      listFilms: ListMeilleuresComedies
    },
    {
      title: "Horror movies",
      listFilms: ListFilmsHorreur
    }
  ];
  return (

    <div className="bg-blacked flex flex-col items-stretch h-screen overflow-y-auto hide-scroll-bar ">
      <NavBar />
      <div className="flex flex-col pt-8 mt-24 gap-2">
        {ListCategories.map((item, index) => {
          return <Categorie key={index} name={item.title} listFilms={item.listFilms} />
        })
        }
        <h1 className="text-white">
          {context.recherche}
        </h1>

      </div>
    </div>
  );
};

export default HomePage;
