from SPARQLWrapper import SPARQLWrapper, JSON
import Utils
import sys


class SPARQLCall:
    def __init__(self):
        self.sparql = SPARQLWrapper(
            "https://query.wikidata.org/sparql"
        )
        self.sparql.setReturnFormat(JSON)

    def get_Human(self, id):
        query = """
        select ?instancelabel ?genrelabel ?date where
        {
        %()s wdt:P31 ?instance;
                     wdt:P21 ?genre;
                     wdt:P569 ?date.
          ?instance rdfs:label ?instancelabel.
          ?genre rdfs:label ?genrelabel.
          FILTER ((lang(?instancelabel)="en") && (lang(?genrelabel)="en") )
        }
        """.replace("%()s", id)

        # Genre
        query_country = """
        SELECT ?countrylabel ?namelabel WHERE {
          %()s wdt:P27 ?country;
            wdt:P734 ?name.
          ?country rdfs:label ?countrylabel.
          ?name rdfs:label ?namelabel.
          FILTER(((LANG(?namelabel)) = "en") && ((LANG(?countrylabel)) = "en"))
        }
        """.replace("%()s", id)

        #Metiers
        query_metier = """
        select  ?label where
        {
        %()s wdt:P31 ?instance;
                     wdt:P106?occupation.
          ?occupation rdfs:label ?label.
          VALUES ?instance {wd:Q5}
          FILTER ((lang(?label)="en") )
        }
        """.replace("%()s", id)

        # Prenoms
        query_prenoms = """
        SELECT ?firstnamelabel WHERE {
          %()s wdt:P735 ?firstname.
          ?firstname rdfs:label ?firstnamelabel.
          FILTER(((LANG(?firstnamelabel)) = "en"))
        }""".replace("%()s", id)

        query_movies = """
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        select distinct ?f ?flabel where
        {{
        ?f ?membertype %()s;
          p:P444 ?review;
          wdt:P31 wd:Q11424.
        ?review pq:P459 wd:Q108403540.
        ?f wdt:P444 ?reviewlabel;
           rdfs:label ?flabel.
        VALUES ?membertype { wdt:P161 wd:P57 wd:P58 wd:P344 wd:P86 wd:P162}
          FILTER ((lang(?flabel)="en"))
        LET (?stringnote := STRBEFORE(?reviewlabel, "/")).
        LET (?floatnote := xsd:float(?stringnote)).
        }
        UNION
        {
          ?f ?membertype %()s;
          rdfs:label ?flabel;
          wdt:P31 wd:Q11424.
          VALUES ?membertype { wdt:P161 wd:P57 wd:P58 wd:P344 wd:P86 wd:P162}
          FILTER NOT EXISTS {?f p:P444/pq:P459 wd:Q108403540}
          FILTER ((lang(?flabel)="en"))
        
        }} 
        ORDER BY DESC(?floatnote)
        LIMIT 5""".replace("%()s", id)

        try:
            self.sparql.setQuery(query)
            ret = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_country)
            ret_country = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_metier)
            ret_metier = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_prenoms)
            ret_prenoms = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_movies)
            ret_movies = self.sparql.queryAndConvert()
            return Utils.construct_human(ret, id, ret_country, ret_metier, ret_prenoms, ret_movies)
        except Exception as e:
          print(e)

    def get_Film_Series(self, id):
        query = """
        select ?instance ?label ?countrylabel  where
        {
        %()s wdt:P31 ?instance;
                     rdfs:label  ?label.
          OPTIONAL{
             %(1)s wdt:P495 ?country.
             ?country rdfs:label ?countrylabel.
            FILTER (lang(?countrylabel)="en")
           }
          VALUES ?instance {wd:Q24856}  
          FILTER ( (lang(?label)="en") )
        }limit 1
        """.replace("%()s", id).replace("%(1)s", id)

        # Genres
        query_genres = """
        select  ?genrelabel where
        {
        %()s  wdt:P31 ?instance;
                     wdt:P136 ?genre.
          ?genre rdfs:label ?genrelabel.
          VALUES ?instance {wd:Q24856}
          FILTER ((lang(?genrelabel)="en") )
        } LIMIT 10
        """.replace("%()s", id)

        # Casting
        query_cast = """
        select  ?list ?objectlabel where
        {
        %()s wdt:P31 ?instance;
                     wdt:P161 ?list.
          ?list rdfs:label ?objectlabel.
          VALUES ?instance {wd:Q24856}
          FILTER ((lang(?objectlabel)="en") )
        } LIMIT 10
        """.replace("%()s", id)

        # Producers
        query_producers = """
        select  ?list ?objectlabel where
        {
        %()s wdt:P31 ?instance;
                     wdt:P162 ?list.
          ?list rdfs:label ?objectlabel.
          VALUES ?instance {wd:Q24856}
          FILTER ((lang(?objectlabel)="en") )
        } LIMIT 10
        """.replace("%()s", id)

        query_movies = """
        select distinct ?f ?flabel where
        {
        ?f wdt:P179 %()s;
           rdfs:label ?flabel.
          FILTER (lang(?flabel) = "en")
        }""".replace("%()s", id)
        try:
            self.sparql.setQuery(query)
            ret = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_genres)
            ret_genres = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_cast)
            ret_cast = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_producers)
            ret_producer = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_movies)
            ret_movies = self.sparql.queryAndConvert()
            return Utils.construct_film_series(ret, id, ret_genres, ret_cast, ret_producer, ret_movies)
        except Exception as e:
            print(e)

    def get_Film(self, id):
        query = """
            select distinct ?instance ?titre ?partof ?partoflabel ?director ?directorlabel ?countrylabel where
            {
            %()s wdt:P31 ?instance;
                         wdt:P1476 ?titre;
                         wdt:P495 ?country;
                         wdt:P57 ?director.
              ?director rdfs:label ?directorlabel.
              ?country rdfs:label ?countrylabel.  
              OPTIONAL {%(1)s wdt:P179 ?partof.
                        ?partof rdfs:label ?partoflabel.
                        FILTER (lang(?partoflabel)="en")}
              FILTER ((lang(?countrylabel)="en")  && (lang(?directorlabel)="en") )
            }limit 1
                        """.replace("%()s", id).replace("%(1)s", id)

        # Genres
        query_genres = """
        select distinct  ?genrelabel where
        {
        %()s wdt:P31 ?instance;
                     wdt:P136 ?genre.
          ?genre rdfs:label ?genrelabel.
          VALUES ?instance {wd:Q11424 wd:Q24869 wd:Q229390}
          FILTER ((lang(?genrelabel)="en") )
        }""".replace("%()s", id)

        # Casting
        query_cast = """
        select distinct ?list ?objectlabel where
        {
        %()s wdt:P31 ?instance;
                     wdt:P161 ?list.
          ?list rdfs:label ?objectlabel.
          VALUES ?instance {wd:Q11424  wd:Q24869 wd:Q229390}
          FILTER ((lang(?objectlabel)="en") )
        } LIMIT 10""".replace("%()s", id)

        # Scénaristes
        query_scenaristes = """
        select distinct ?list ?objectlabel where
        {
        %()s wdt:P31 ?instance;
                     wdt:P58 ?list.
          ?list rdfs:label ?objectlabel.
          VALUES ?instance {wd:Q11424 wd:Q24869 wd:Q229390}
          FILTER ((lang(?objectlabel)="en") )
        } LIMIT 5""".replace("%()s", id)

        # Photographes
        query_photo = """
        select distinct ?list ?objectlabel where
        {
        %()s wdt:P31 ?instance;
                     wdt:P344 ?list.
          ?list rdfs:label ?objectlabel.
          VALUES ?instance {wd:Q11424 wd:Q24869 wd:Q229390}
          FILTER ((lang(?objectlabel)="en") )
        } LIMIT 5""".replace("%()s", id)

        # Compagnies de production
        query_production_comp = """
        select distinct ?objectlabel where
        {
        %()s wdt:P31 ?instance;
                     wdt:P272 ?list.
          ?list rdfs:label ?objectlabel.
          VALUES ?instance {wd:Q11424 wd:Q24869 wd:Q229390} 
          FILTER ((lang(?objectlabel)="en") )
        } LIMIT 5""".replace("%()s", id)

        query_dur_review = """
       select distinct ?label ?datenode where
        {
        %()s wdt:P31 ?instance;
                     p:P444 ?node;
                     wdt:P577 ?datenode.
          ?node pq:P459 wd:Q108403540;
           ps:P444 ?label.
          VALUES ?instance {wd:Q11424 wd:Q24869 wd:Q229390}
        } LIMIT 1""".replace("%()s", id)
        try:
            self.sparql.setQuery(query)
            ret = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_genres)
            ret_genres = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_cast)
            ret_cast = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_scenaristes)
            ret_scen = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_photo)
            ret_photo = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_production_comp)
            ret_prod_comp = self.sparql.queryAndConvert()
            self.sparql.setQuery(query_dur_review)
            ret_dur_review = self.sparql.queryAndConvert()
            return Utils.construct_film(ret, id, ret_genres, ret_cast, ret_scen, ret_photo, ret_prod_comp,
                                        ret_dur_review)
        except Exception as e:
            print(e)

    def get_caractere(self, objet, relation):
        query = """
                select ?caract where
                {
                wd:%(objet)s wdt:%(relation)s ?caract.
                }
                """.replace("%(objet)s", objet).replace("%(relation)s", relation)
        self.sparql.setQuery(query)
        try:
            ret = self.sparql.queryAndConvert()
            return ret["results"]["bindings"][0]["caract"]["value"]
        except Exception as e:
            print(e)

    def get_result_search(self, enter, limit):
        query_movie = """
        select distinct ?object ?objectlabel ?duration  where
        {
        ?object wdt:P31 wd:Q11424.
        ?object rdfs:label ?objectlabel.
        ?object wdt:P31 ?objectinstance.
        OPTIONAL{?object wdt:P2047 ?duration}
        VALUES ?objectinstance {wd:Q11424}
        FILTER ((lang(?objectlabel)="en") && regex(?objectlabel, "%()s"))
        }
        LIMIT 7
        """.replace("%()s", enter)
        try:
            self.sparql.setQuery(query_movie)
            ret_movie = self.sparql.queryAndConvert()
            return Utils.construct_separated_list_of_result(ret_movie)
        except Exception as e:
            print(e)

    def get_all_movies_of_serie(self, serie):
        query = """
                select distinct ?f ?flabel where
                {
                ?f wdt:P179 wd:%()s;
                wdt:P31 wd:Q11424.
                ?f rdfs:label ?flabel.
                FILTER ((lang(?flabel)="en"))
                }
                """.replace("%()s", serie)
        self.sparql.setQuery(query)
        try:
            ret = self.sparql.queryAndConvert()
            return Utils.construct_list_films(ret)
        except Exception as e:
            print(e)

    def get_all_films_from_same_serie(self, film):
        query = """
                select distinct ?f ?flabel where
                {
                wd:%()s wdt:P179 ?serie.
                ?f wdt:P179 ?serie;
                wdt:P31 wd:Q11424.
                ?f rdfs:label ?flabel.
                FILTER ((?f != wd:%()s)&&(lang(?flabel)="en"))
                }
                        """.replace("%()s", film)
        self.sparql.setQuery(query)
        try:
            ret = self.sparql.queryAndConvert()
            return Utils.construct_list_films(ret)
        except Exception as e:
            print(e)

    def get_top_films_by_genre(self):
        list_genres = [
            ["Comedy", "wd:Q157443"],
            ["Horror", "wd:Q200092"],
            ["Action", "wd:Q188473"],
            ["Drama", "wd:Q130232"]
        ]

        query = """
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        select distinct ?f ?flabel where
        {
          {
            ?f ?genre %()s;
              p:P444 ?review;
              wdt:P577 ?date;
              wdt:P31 wd:Q11424.
            ?review pq:P459 wd:Q108403540.
            ?f wdt:P444 ?reviewlabel;
              rdfs:label ?flabel.
            LET (?stringnote := STRBEFORE(?reviewlabel, "/")).
            LET (?floatnote := xsd:float(?stringnote)).
            FILTER ((lang(?flabel)="en") && ?floatnote > 7.5)    
          }
        }
        ORDER BY desc(?date)
        LIMIT 5
        """

        rets = []
        genres = ["Comedy", "Horror", "Action", "Drama"]

        for [_, genre_id] in list_genres:
            try:
                self.sparql.setQuery(query.replace("%()s", genre_id))
                ret = self.sparql.queryAndConvert()
                rets.append(ret)
            except Exception as e:
                print(e)
        return Utils.construct_list_genres(rets, genres)

