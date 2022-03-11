import json
import attaque
import random

class Pokemon:
    statAttaque : int
    statVieMax: int
    statVieActuel: int
    statDefence: int
    statVitesse: int
    type: str
    nom : str
    attaques: list[attaque]

    def __init__(self, nom, identifiant, ennemi=False ):
        if ennemi:
            self.nom = "???"
            self.type = "normal"
            self.statVieMax = random.randrange(50, 70)
            self.statVieActuel = self.statVieMax
            self.statAttaque = random.randrange(70, 80)
            self.statDefence = random.randrange(65, 75)
            self.statVitesse = random.randrange(61, 71)

        else :
            dico = json.loads(f"data/pokemons/{identifiant}_{nom}/data.json")
            self.nom = nom
            self.type = dico['types'][0]['name']
            self.statVieMax = dico['stats'][0]['base_stat']
            self.statVieActuel = self.statVieMax
            self.statAttaque = dico['stats'][1]['base_stat']
            self.statDefence = dico['stats'][2]['base_stat']
            self.statVitesse = dico['stats'][5]['base_stat']
