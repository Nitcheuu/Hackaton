import pygame
import pygame as pg
from combat import Combat


class Game:

    TAILLE_ECRAN : tuple
    FPS : int
    run : bool


    def __init__(self, hauteur : int, largeur : int, FPS : int):
        pg.init()
        # Définition de la taille de l'écran
        self.TAILLE_ECRAN = (hauteur, largeur)
        # Définition du nombre de FPS
        self.FPS = FPS
        # Défintion de la fenetre du jeu
        self.ecran = pg.display.set_mode(self.TAILLE_ECRAN)
        # Variable qui permet de savoir si la fenetre est active ou non
        self.jeu_en_cours = True


    def demarrer(self):

        combat = Combat(1, self.ecran)
        while self.jeu_en_cours:
            self.ecran.fill((255, 255, 255))
            combat.maj()
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.jeu_en_cours = False
            pg.time.Clock().tick(self.FPS)
        pygame.quit()