import pygame as pg

pg.init()


class Menu:

    @staticmethod
    def choix(ecran):
        font = pg.font.SysFont("comicsansms", 30)
        ecran.blit(font.render("a - Attaquer", True, (0, 0, 0)), (700, 625))
        ecran.blit(font.render("b - Pokemon", True, (0, 0, 0)), (700, 675))