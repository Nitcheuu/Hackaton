import pygame as pg
from joueur import Joueur
pg.init()


class Combat:

    def __init__(self, id_background : int, ecran : pg.Surface, joueur : Joueur):
        # Chargement de l'image de fond du combat
        self.fond = pg.image.load(f"data/backgrounds/background_{id_background}.PNG")
        # Chargement de l'écran du combat
        self.ecran = ecran
        # Définition du joueur
        self.joueur = joueur




    def maj(self):
        self.ecran.blit(self.fond, (0, 0))
        self.ecran.blit(self.joueur.pokemon_actif.sprite, (100, 310))