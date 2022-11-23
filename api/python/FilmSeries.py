from json import JSONEncoder


class FilmSeries:
    def __init__(self, title, genre, country, producer, cast, resume, img, movies):
        self.title = title
        self.movies = movies
        self.genre = genre
        self.country = country
        self.producer = producer
        self.cast = cast
        self.resume = resume
        self.img = img


# subclass JSONEncoder
class FilmSeriesEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
