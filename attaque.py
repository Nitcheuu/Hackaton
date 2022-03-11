import json


class Attaque:
    nomAttaque: str
    type: str
    attaque: int
    precision: int

    def __init__(self, nom):
        dico = json.loads(f"data/moves/{nom}.json")
        self.type = dico['type']['name']
        self.attaque = dico['power']
        if dico['accuracy'] is None:
            self.precision = 100
        else:
            self.precision = dico['accuracy']
        self.nomAttaque = dico['name']