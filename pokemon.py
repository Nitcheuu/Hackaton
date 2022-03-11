from attaque import Attaque
import json
import pygame as pg


class Pokemon:
    statAttaque : int
    statVie: int
    statDefence: int
    statVitesse: int
    type: str
    nom : str
    attaques: list[Attaque]
    dico : dict


    def __init__(self, identifiant, nom):
        print(nom)
        print(identifiant)
        with open(f"data/pokemons/{identifiant}_{nom}/data.json", "r") as pokemon_data:
            self.dico = json.load(pokemon_data)
        self.nom = nom
        self.type = self.dico['types'][0]["type"]['name']
        self.statVie = self.dico['stats'][0]['base_stat']
        self.statAttaque = self.dico['stats'][1]['base_stat']
        self.statDefence = self.dico['stats'][2]['base_stat']
        self.statVitesse = self.dico['stats'][5]['base_stat']
        self.sprite = pg.image.load(f"data/pokemons/{identifiant}_{nom}/back_default.png")
        self.sprite = pg.transform.scale(self.sprite, (300, 300))
