import API
import sys


def main():
    a = API.SPARQLCall()
    fct = sys.argv[1]

    if fct == "0":
        # Resultat de recherche
        if len(sys.argv) > 3:
            print(a.get_result_search(sys.argv[2], sys.argv[3]))
        else:
            print(a.get_result_search(sys.argv[2], "5"))
    elif fct == "1":
        # Récupérer les films d'une série
        print(a.get_all_movies_of_serie(sys.argv[2]))
    elif fct == "2":
        # Récupérer les films d'une même série qu'un film donné
        print(a.get_all_films_from_same_serie(sys.argv[2]))
    elif fct == "3":
        # Récupérer les infos d'un film par son ID
        print(a.get_Film(sys.argv[2]))
    elif fct == "4":
        # Récupérer les infos d'une série de films par son ID
        print(a.get_Film_Series(sys.argv[2]))
    elif fct == "5":
        # Récupérer les infos d'un humain par son ID
        print(a.get_Human(sys.argv[2]))
    elif fct == "6":
        # Récupérer les films par genre
        print(a.get_top_films_by_genre())


main()
