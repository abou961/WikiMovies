import json
from SPARQLWrapper import SPARQLWrapper, JSON
from Film import Film, FilmEncoder
from FilmSeries import FilmSeries, FilmSeriesEncoder
import wikipedia
from bs4 import BeautifulSoup
import requests

from FilmSeries import FilmSeries
from Human import Human, HumanEncoder


def get_image_w(id):
    query = """
                        SELECT ?pageid WHERE {
                        VALUES (?item) {(%()s)} 
                        [ schema:about ?item ; schema:name ?name ;
                          schema:isPartOf <https://en.wikipedia.org/> ]
                         SERVICE wikibase:mwapi {
                             bd:serviceParam wikibase:endpoint "en.wikipedia.org" .
                             bd:serviceParam wikibase:api "Generator" .
                             bd:serviceParam mwapi:generator "allpages" .
                             bd:serviceParam mwapi:gapfrom ?name .
                             bd:serviceParam mwapi:gapto ?name .
                             ?pageid wikibase:apiOutput "@pageid" .
                        }
                    }""".replace("%()s", id)
    sparql = SPARQLWrapper(
        "https://query.wikidata.org/sparql"
    )
    sparql.setReturnFormat(JSON)
    sparql.setQuery(query)
    try:
        url = "https://en.wikipedia.org/?curid=" + sparql.queryAndConvert()['results']['bindings'][0]['pageid']['value']
    except Exception as e:
        url = None
        print(e)
    if url:
        get_url = requests.get(url)
        get_text = get_url.text
        soup = BeautifulSoup(get_text, "html.parser")

        tables = soup.find_all('td', class_="infobox-image")
        if tables:
            img = tables[0].find("img").get("src")
            return img

        return ""
    else:
        return ""

def get_image_from_wikipedia(id, words):
    query = """
                    SELECT ?pageid WHERE {
                    VALUES (?item) {(%()s)} 
                    [ schema:about ?item ; schema:name ?name ;
                      schema:isPartOf <https://en.wikipedia.org/> ]
                     SERVICE wikibase:mwapi {
                         bd:serviceParam wikibase:endpoint "en.wikipedia.org" .
                         bd:serviceParam wikibase:api "Generator" .
                         bd:serviceParam mwapi:generator "allpages" .
                         bd:serviceParam mwapi:gapfrom ?name .
                         bd:serviceParam mwapi:gapto ?name .
                         ?pageid wikibase:apiOutput "@pageid" .
                    }
                }""".replace("%()s", id)
    sparql = SPARQLWrapper(
        "https://query.wikidata.org/sparql"
    )
    sparql.setReturnFormat(JSON)
    sparql.setQuery(query)
    try:
        url = "https://en.wikipedia.org/?curid=" + sparql.queryAndConvert()['results']['bindings'][0]['pageid']['value']
    except Exception as e:
        url = None
        print(e)
    if url:
        get_url = requests.get(url)
        get_text = get_url.text
        soup = BeautifulSoup(get_text, "html.parser")
        title = soup.find_all(["h1"])[0].get_text()
        p = wikipedia.page(title, auto_suggest=False)

        if p.images:
            imgs = p.images

            for i in imgs:
                if words in i:
                    img = i
                    break
            else:
                img = imgs[0]
            return img
        else:
            return ""
    else:
        return ""


def construct_separated_list_of_result(ret_movie):
    films = []
    for r in ret_movie["results"]["bindings"]:
        id = r['object']["value"].split("/")[-1]
        query = """
                    SELECT ?pageid WHERE {
                    VALUES (?item) {(%()s)} 
                    [ schema:about ?item ; schema:name ?name ;
                      schema:isPartOf <https://en.wikipedia.org/> ]
                     SERVICE wikibase:mwapi {
                         bd:serviceParam wikibase:endpoint "en.wikipedia.org" .
                         bd:serviceParam wikibase:api "Generator" .
                         bd:serviceParam mwapi:generator "allpages" .
                         bd:serviceParam mwapi:gapfrom ?name .
                         bd:serviceParam mwapi:gapto ?name .
                         ?pageid wikibase:apiOutput "@pageid" .
                    }
                }""".replace("%()s", "wd:" + id)
        sparql = SPARQLWrapper(
            "https://query.wikidata.org/sparql"
        )
        sparql.setReturnFormat(JSON)
        sparql.setQuery(query)
        try:
            url = "https://en.wikipedia.org/?curid=" + sparql.queryAndConvert()['results']['bindings'][0]['pageid'][
                'value']
        except Exception as e:
            url = None
            print(e)
        if url:
            get_url = requests.get(url)
            get_text = get_url.text
            soup = BeautifulSoup(get_text, "html.parser")
            title = soup.find_all(["h1"])[0].get_text()

            p = wikipedia.page(title, auto_suggest=False)

        if "duration" not in r:
            duration = ""
        else:
            duration = r['duration']["value"] + " min"

        img = get_image_w("wd:" + id)

        res = {"id": "wd:" + id, "name": r['objectlabel']["value"], "image": img, "duration": duration}
        if img != "":
            films.append(res)

    result = {"films": films}
    return json.dumps(result)


def construct_list_films(ret):
    films = []
    for r in ret["results"]["bindings"]:
        res = {"link": r['f']["value"], "name": r['flabel']["value"]}
        films.append(res)

    result = {"films": films}
    return json.dumps(result)


def construct_human(ret, id, ret_country, ret_metier, ret_prenoms, ret_movies):
    r = ret["results"]["bindings"][0]
    r_c = ret_country["results"]["bindings"][0]
    movies = []
    for m in ret_movies["results"]["bindings"]:
        movies.append([m['flabel']['value'], "wd:" + m['f']['value'].split("/")[-1]])
    prenoms = []
    for r_p in ret_prenoms["results"]["bindings"]:
        prenoms.append(r_p['firstnamelabel']['value'])

    name = r_c['namelabel']['value']
    sexe = r['genrelabel']['value']
    country = r_c['countrylabel']['value']
    birth = r['date']['value']
    r_m = ret_metier["results"]["bindings"]
    metiers = []
    for r_i in r_m:
        metiers.append(r_i['label']['value'])
    img = get_image_w(id)

    h = Human(name, sexe, img, country, birth, metiers, prenoms, movies)
    return json.dumps(h, cls=HumanEncoder)


def construct_film_series(ret, id, ret_genre, ret_cast, ret_producers, ret_movies):
    r = ret["results"]["bindings"][0]
    titre = ''
    country = ''
    if 'label' in r:
        titre = r['label']['value']
    if 'title' in r:
        titre = r['title']['value']
    if 'nativelabel' in r:
        titre = r['nativelabel']['value']
    if 'countrylabel' in r:
        country = r['countrylabel']['value']

    genre = []
    for re in ret_genre["results"]["bindings"]:
        genre.append(re['genrelabel']['value'])

    casting = []
    for re in ret_cast["results"]["bindings"]:
        casting.append([re['objectlabel']['value'], re['list']['value'].split("/")[-1]])

    producers = []
    for re in ret_producers["results"]["bindings"]:
        producers.append([re['objectlabel']['value'], re['list']['value'].split("/")[-1]])

    movies = []
    for re in ret_movies["results"]["bindings"]:
        movies.append([re['flabel']['value'], re['f']['value'].split("/")[-1]])

    query = """
                SELECT ?pageid WHERE {
                VALUES (?item) {(%()s)} 
                [ schema:about ?item ; schema:name ?name ;
                  schema:isPartOf <https://en.wikipedia.org/> ]
                 SERVICE wikibase:mwapi {
                     bd:serviceParam wikibase:endpoint "en.wikipedia.org" .
                     bd:serviceParam wikibase:api "Generator" .
                     bd:serviceParam mwapi:generator "allpages" .
                     bd:serviceParam mwapi:gapfrom ?name .
                     bd:serviceParam mwapi:gapto ?name .
                     ?pageid wikibase:apiOutput "@pageid" .
                }
            }""".replace("%()s", id)
    sparql = SPARQLWrapper(
        "https://query.wikidata.org/sparql"
    )
    sparql.setReturnFormat(JSON)
    sparql.setQuery(query)
    url = None
    try:
        if sparql.queryAndConvert()['results']['bindings']:
            url = "https://en.wikipedia.org/?curid=" + sparql.queryAndConvert()['results']['bindings'][0]['pageid'][
                'value']
    except Exception as e:
        print(e)

    resume = ""
    if url:
        get_url = requests.get(url)
        get_text = get_url.text
        soup = BeautifulSoup(get_text, "html.parser")
        title = soup.find_all(["h1"])[0].get_text()

        p = wikipedia.page(title, auto_suggest=False)
        resume = p.summary


    img = get_image_w(id)
    # franchise ou logo ou le titre ou wordmark
    f = FilmSeries(titre, genre, country, producers, casting, resume, img, movies)
    return json.dumps(f, cls=FilmSeriesEncoder)


def construct_film(ret, id, ret_genre, ret_cast, ret_scen, ret_photo, ret_prod_comp, ret_dur_review):
    r = ret["results"]["bindings"][0]
    titre = r['titre']['value']
    country = r['countrylabel']['value']
    director = [r['directorlabel']['value'], "wd:" + r['director']['value'].split("/")[-1]]

    part_of_serie = ""
    if 'partoflabel' in r:
        part_of_serie = [r['partoflabel']['value'], r['partof']['value'].split("/")[-1]]

    pub_date = ret_dur_review["results"]["bindings"][0]['datenode']['value']
    duration = ""
    review = ret_dur_review["results"]["bindings"][0]['label']['value']

    genres = []
    for r in ret_genre["results"]["bindings"]:
        genres.append(r['genrelabel']['value'])

    cast_member = []
    for r in ret_cast["results"]["bindings"]:
        cast_member.append([r['objectlabel']['value'], r['list']['value'].split("/")[-1]])

    screenwriter = []
    for r in ret_scen["results"]["bindings"]:
        screenwriter.append([r['objectlabel']['value'], r['list']['value'].split("/")[-1]])

    photograph = []
    for r in ret_photo["results"]["bindings"]:
        photograph.append([r['objectlabel']['value'], r['list']['value'].split("/")[-1]])

    production_company = []
    for r in ret_prod_comp["results"]["bindings"]:
        production_company.append(r['objectlabel']['value'])

    query = """
            SELECT ?pageid WHERE {
            VALUES (?item) {(%()s)} 
            [ schema:about ?item ; schema:name ?name ;
              schema:isPartOf <https://en.wikipedia.org/> ]
             SERVICE wikibase:mwapi {
                 bd:serviceParam wikibase:endpoint "en.wikipedia.org" .
                 bd:serviceParam wikibase:api "Generator" .
                 bd:serviceParam mwapi:generator "allpages" .
                 bd:serviceParam mwapi:gapfrom ?name .
                 bd:serviceParam mwapi:gapto ?name .
                 ?pageid wikibase:apiOutput "@pageid" .
            }
        }""".replace("%()s", id)
    sparql = SPARQLWrapper(
        "https://query.wikidata.org/sparql"
    )
    sparql.setReturnFormat(JSON)
    sparql.setQuery(query)
    try:
        url = "https://en.wikipedia.org/?curid=" + sparql.queryAndConvert()['results']['bindings'][0]['pageid']['value']
    except Exception as e:
        print(e)

    get_url = requests.get(url)
    get_text = get_url.text
    soup = BeautifulSoup(get_text, "html.parser")
    title = soup.find_all(["h1"])[0].get_text()

    p = wikipedia.page(title, auto_suggest=False)
    plot = p.content.split("== Plot ==")[1].split("==")[0]

    img = get_image_w(id)

    f = Film(titre, part_of_serie, country, pub_date, director, screenwriter, cast_member, photograph,
             production_company, duration, review, plot, img, genres)
    return json.dumps(f, cls=FilmEncoder)


def construct_list_genres(ret, genres):
    list_of = [[], [], [], []]
    ini = 0
    for ru in ret:
        ri = ru['results']['bindings']
        for r in ri:
            id = r['f']['value'].split("/")[-1]

            query = """
                        SELECT ?pageid WHERE {
                        VALUES (?item) {(%()s)} 
                        [ schema:about ?item ; schema:name ?name ;
                          schema:isPartOf <https://en.wikipedia.org/> ]
                         SERVICE wikibase:mwapi {
                             bd:serviceParam wikibase:endpoint "en.wikipedia.org" .
                             bd:serviceParam wikibase:api "Generator" .
                             bd:serviceParam mwapi:generator "allpages" .
                             bd:serviceParam mwapi:gapfrom ?name .
                             bd:serviceParam mwapi:gapto ?name .
                             ?pageid wikibase:apiOutput "@pageid" .
                        }
                    }""".replace("%()s", "wd:" + id)
            sparql = SPARQLWrapper(
                "https://query.wikidata.org/sparql"
            )
            sparql.setReturnFormat(JSON)
            sparql.setQuery(query)
            try:
                url = "https://en.wikipedia.org/?curid=" + sparql.queryAndConvert()['results']['bindings'][0]['pageid'][
                    'value']
            except Exception as e:
                print(e)

            get_url = requests.get(url)
            get_text = get_url.text
            soup = BeautifulSoup(get_text, "html.parser")
            title = soup.find_all(["h1"])[0].get_text()

            p = wikipedia.page(title, auto_suggest=False)
            try:
                imgs = p.images
                if imgs:
                    for i in imgs:
                        if "poster" in i or any(ext in i for ext in title.split(" ")):
                            img = i
                            break
                    else:
                        img = imgs[0]
                else:
                    img = ""
            except Exception as e:
                img = ""

            list_of[ini].append([title, "wd:" + id, img])
        ini += 1
    result = dict(zip(genres, list_of))
    return result
