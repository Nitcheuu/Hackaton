import pygame as pg
from joueur import Joueur
from pokemon import Pokemon
from barrevie import BarreVie
from menu import Menu
from chatBox import ChatBox
from pygame.locals import *
from time import sleep
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
        self.barre_joueur = BarreVie(self.joueur.pokemon_actif, (20, 250), ecran, 350)

        self.barre_ennemi = BarreVie(self.ennemi, (600, 80), ecran, 350)

        self.menu = Menu()

        self.fin = False

        self.chatbox = ChatBox()





    def maj(self):
        self.ecran.blit(self.fond, (0, 0))
        self.ecran.blit(self.joueur.pokemon_actif.sprite, (100, 310))
        self.ecran.blit(self.ennemi.sprite, (650, 140))
        self.menu.choix(self.ecran)
        self.barre_joueur.maj()
        self.barre_ennemi.maj()


    def lancer(self):
        while not self.fin:
            self.chatbox.textBox1(self.ecran)
            choix = self.choisir()
            if choix == 97:
                self.attaquer()

    def attaquer(self):
        if self.joueur.pokemon_actif.statVitesse >= self.ennemi.statVitesse:
            self.joueur.pokemon_actif.attaquer(self.ennemi)
            pg.display.flip()
            self.maj()
            self.chatbox.textAttack(self.ecran, self.joueur.pokemon_actif.nom, "attaque")
            sleep(1)
            self.ennemi.attaquer(self.joueur.pokemon_actif)
            pg.display.flip()
            self.maj()
            self.chatbox.textAttack(self.ecran, self.ennemi.nom, "attaque")
            sleep(1)
        else:
            self.ennemi.attaquer(self.joueur.pokemon_actif)
            pg.display.flip()
            self.maj()
            self.chatbox.textAttack(self.ecran, self.ennemi.nom, "attaque")
            sleep(1)
            self.joueur.pokemon_actif.attaquer(self.ennemi)
            pg.display.flip()
            self.chatbox.textAttack(self.ecran, self.joueur.pokemon_actif.nom, "attaque")
            self.maj()
            sleep(1)





    def choisir(self):
        while True:
            self.maj()
            pg.display.flip()
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN and (event.key == K_a or event.key == K_b):
                    return event.key




