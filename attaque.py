import json


class Attaque:
    nomAttaque : str
    type : str
    attaque : int
    precision : int

    def __init__(self, nom):
        with open(f"data/moves/{nom}.json", "r") as pokemon_data:
            self.dico = json.load(pokemon_data)
        self.type = self.dico['type']['name']
        self.attaque = self.dico['power']

        if self.dico['accuracy'] is None:
            self.precision = 100
        else:
            self.precision = self.dico['accuracy']

        self.nomAttaque = self.dico['name']
