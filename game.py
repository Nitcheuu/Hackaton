import pygame
import pygame as pg

from combat import Combat
from joueur import Joueur

class Game:

    TAILLE_ECRAN : tuple
    FPS : int
    joueur : Joueur
    run : bool


    def __init__(self, hauteur : int, largeur : int, FPS : int):
        pg.init()
        # Définition de la taille de l'écran
        self.TAILLE_ECRAN = (hauteur, largeur)
        # Définition du nombre de FPS
        self.FPS = FPS
        # Définition du joueur
        self.joueur = Joueur(["6_charizard", "3_venusaur", "9_blastoise", "25_pikachu"], [["flamethrower", "double-hit"], ["energy-ball", "double-hit"], ["flamethrower", "double-hit"], ["thunder", "double-hit"],])
        # Défintion de la fenetre du jeu
        self.ecran = pg.display.set_mode(self.TAILLE_ECRAN)
        # Variable qui permet de savoir si la fenetre est active ou non
        self.jeu_en_cours = True


    def demarrer(self):

        combat = Combat(1, self.ecran, self.joueur)
        while self.jeu_en_cours:
            self.ecran.fill((255, 255, 255))
            combat.lancer()
            print("principal")
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.jeu_en_cours = False
            pg.time.Clock().tick(self.FPS)
        pygame.quit()