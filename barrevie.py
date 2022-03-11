import pygame as pg


class BarreVie:

    def __init__(self, pokemon, x_y, ecran, longueur):
        self.ecran = ecran
        self.pokemon = pokemon
        self.longueur = longueur
        self.x_y = x_y
        self.rectangle_max = pg.Rect(x_y[0], x_y[1], self.longueur, 20)
        self.rectangle_actuel = pg.Rect(x_y[0], x_y[1], self.longueur, 20)
        self.rectangle_fond = pg.Rect(x_y[0] - 10, x_y[1] - 70, self.longueur + 20, 100)
        self.font = pg.font.SysFont("comicsansms", 20)

    def maj(self):
        pg.draw.rect(self.ecran, (255, 255, 255), self.rectangle_fond)
        self.ecran.blit(self.font.render(self.pokemon.nom, True, (0, 0, 0)), (self.x_y[0], self.x_y[1] - 60))
        self.ecran.blit(self.font.render(f"{self.pokemon.statVieActuel} / {self.pokemon.statVie}", True, (0, 0, 0)), (self.x_y[0], self.x_y[1] - 35))
        pg.draw.rect(self.ecran, (255, 0, 0), self.rectangle_max)
        pg.draw.rect(self.ecran, (0, 255, 50), pg.Rect(self.x_y[0], self.x_y[1], (( self.pokemon.statVieActuel / self.pokemon.statVie) * self.longueur), 20))

