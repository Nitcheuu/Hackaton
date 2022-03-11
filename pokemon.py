from attaque import Attaque
import json
import pygame as pg
import random
import os


class Pokemon:
    statAttaque : int
    statVieMax: int
    statVieActuel: int
    statDefence: int
    statVitesse: int
    type: str
    nom : str
    attaques: list[Attaque]
    dico : dict


    def __init__(self,identifiant, nom , attaques, ennemi=False ):
        if ennemi:
            self.nom = "???"
            self.type = "normal"
            self.statVie = random.randrange(50, 70)
            self.statVieActuel = self.statVie
            self.statAttaque = random.randrange(70, 80)
            self.statDefence = random.randrange(65, 75)
            self.statVitesse = random.randrange(61, 71)
            liste = os.listdir("./data/hackathon_data/detection_yaourt_dessus")
            self.sprite = pg.image.load(f"data/hackathon_data/detection_yaourt_dessus/{liste[random.randint(0, len(liste) - 1)]}")
            self.sprite = pg.transform.scale(self.sprite, (280, 200))
            print(liste)
        else:
            with open(f"data/pokemons/{identifiant}_{nom}/data.json", "r") as pokemon_data:
                self.dico = json.load(pokemon_data)
            self.nom = nom
            self.type = self.dico['types'][0]["type"]['name']
            self.statVie = self.dico['stats'][0]['base_stat']
            self.statVieActuel = self.statVie
            self.statAttaque = self.dico['stats'][1]['base_stat']
            self.statDefence = self.dico['stats'][2]['base_stat']
            self.statVitesse = self.dico['stats'][5]['base_stat']
            self.sprite = pg.image.load(f"data/pokemons/{identifiant}_{nom}/back_default.png")
            self.sprite = pg.transform.scale(self.sprite, (300, 300))
            self.attaques = []
            for attaque in attaques:
                self.attaques.append(Attaque(attaque))
