import attaque
import json
import attaque

class Pokemon:
    statAttaque : int
    statVie: int
    statDefence: int
    statVitesse: int
    type: str
    nom : str
    attaques: list[Attaque]


    def __init__(self, nom, identifiant ):
        dico = json.loads(f"data/pokemons/{identifiant}_{nom}/data.json")
        self.nom = nom;
        self.type = dico['types'][0]['name']
        self.statVie = dico['stats'][0]['base_stat']
        self.statAttaque = dico['stats'][1]['base_stat']
        self.statDefence = dico['stats'][2]['base_stat']
        self.statVitesse = dico['stats'][5]['base_stat']
