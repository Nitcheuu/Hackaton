import pygame as pg
from chatBox import ChatBox

class Identification:

    @staticmethod
    def identificationPoke(ecran: pg.Surface, pokeYaourt):
        # Chargement de l'image de fond du combat
        fond = pg.image.load(f"data/backgrounds/chen.png")
        # Affichage sprite ennemi
        ecran.blit(fond, (0, 0))
        ecran.blit(pokeYaourt.sprite, (650, 140))

        ChatBox.textIdentification()
