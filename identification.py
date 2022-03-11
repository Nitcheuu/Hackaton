import pygame as pg
from chatBox import ChatBox
import os
from pygame.locals import *


class Identification:

    @staticmethod
    def identificationPoke(ecran: pg.Surface, pokemon_mystere):
        # Chargement de l'image de fond du combat
        fond = pg.image.load(f"data/backgrounds/chen.png")
        fond = pg.transform.scale(fond, (1000, 600))
        pg.mixer.music.load("data/musiques/lobby/lobby.mp3")
        pg.mixer.music.play(-1)
        estIdentifie = False
        while not estIdentifie:
            # Affichage sprite ennemi
            ecran.blit(fond, (0, 0))
            ecran.blit(pokemon_mystere.sprite, (650, 140))
            ChatBox.textIdentification(ecran, pokemon_mystere.nom)
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.jeu_en_cours = False
                if event.type == pg.KEYDOWN and event.key == K_a:
                    os.rename(f"data/hackathon_data/detection_yaourt_dessus/{pokemon_mystere.nom_fichier}", f"output/valide/{pokemon_mystere.nom_fichier}")
                    estIdentifie = True
                    pg.mixer.Sound("data/musiques/sounds/action.mp3").play()
                if event.type == pg.KEYDOWN and event.key == K_b:
                    os.rename(f"data/hackathon_data/detection_yaourt_dessus/{pokemon_mystere.nom_fichier}",
                              f"output/invalide/{pokemon_mystere.nom_fichier}")
                    estIdentifie = True
                    pg.mixer.Sound("data/musiques/sounds/action.mp3").play()

    def move_image(self, pokemon_mystere, dossier):
        pass


