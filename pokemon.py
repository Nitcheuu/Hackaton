import attaque
import json

class Pokemon:
    statAttaque : int
    statVie: int
    statDefence: int
    statVitesse: int
    type: str
    nom : str
    attaques: attaque[]


    def __init__(self, nom, identifiant ):
        dico = json.loads(f"data/pokemons/{identifiant}_{nom}/data.json")
        nom = nom;
        type = dico['types'][0]['name']
        statVie = dico['stats'][0]['base_stat']
        statAttaque = dico['stats'][1]['base_stat']
        statDefence = dico['stats'][2]['base_stat']
        statVitesse = dico['stats'][5]['base_stat']
