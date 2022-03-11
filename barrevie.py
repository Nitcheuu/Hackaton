import pygame as pg


class BarreVie:

    def __init__(self, pokemon, x_y, ecran, longueur):
        self.ecran = ecran
        self.pokemon = pokemon
        self.longueur = longueur
        self.x_y = x_y
        self.rectangle_max = pg.Rect(x_y[0], x_y[1], self.longueur, 20)
        self.rectangle_actuel = pg.Rect(x_y[0], x_y[1], self.longueur, 20)

    def maj(self):
        pg.draw.rect(self.ecran, (255, 0, 0), self.rectangle_max)
        pg.draw.rect(self.ecran, (0, 255, 50), pg.Rect(self.x_y[0], self.x_y[1], (self.pokemon.statVie / self.pokemon.statVieActuel * self.longueur), 20))
