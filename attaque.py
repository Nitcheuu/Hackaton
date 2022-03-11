import json


class Attaque:
    nomAttaque : str
    type : str
    attaque : int
    precision : int

    def __init__(self, nom):
        dico = json.loads(f"data/moves/{nom}.json")
        type = dico['type']['name']
        attaque = dico['power']
        if dico['accuracy'] is None:
            precision = 100
        else:
            precision = dico['accuracy']