from json import JSONEncoder


class Human:
    def __init__(self, name, sex, image, country, birth, occupation, prenoms, films):
        self.name = name
        self.prenoms = prenoms
        self.sex = sex
        self.image = image
        self.country = country
        self.birth = birth
        self.occupation = occupation
        self.movies = films

# subclass JSONEncoder
class HumanEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
