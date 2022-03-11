import pygame as pg
from joueur import Joueur
from pokemon import Pokemon
from barrevie import BarreVie
from menu import Menu
pg.init()


class Combat:

    def __init__(self, id_background : int, ecran : pg.Surface, joueur : Joueur):
        # Chargement de l'image de fond du combat
        self.fond = pg.image.load(f"data/backgrounds/background_{id_background}.PNG")
        # Chargement de l'écran du combat
        self.ecran = ecran
        # Définition du joueur
        self.joueur = joueur
        # Définition de l'ennemi
        self.ennemi = Pokemon("", "", ["double-hit"], ennemi=True)
        # Définition barre de vie du joeuur
        self.barre_joueur = BarreVie(self.joueur.pokemon_actif, (20, 300), ecran, 350)

        self.barre_ennemi = BarreVie(self.ennemi, (600, 80), ecran, 350)

        self.menu = Menu()

        self.fin = False





    def maj(self):
        self.ecran.blit(self.fond, (0, 0))
        self.ecran.blit(self.joueur.pokemon_actif.sprite, (100, 310))
        self.ecran.blit(self.ennemi.sprite, (650, 140))
        self.menu.choix(self.ecran)
        self.barre_joueur.maj()
        self.barre_ennemi.maj()



