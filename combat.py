import pygame as pg
pg.init()


class Combat:

    def __init__(self, id_background : int, ecran : pg.Surface):
        # Chargement de l'image de fond du combat
        self.fond = pg.image.load(f"data/backgrounds/background_{id_background}.PNG")
        # Chargement de l'écran du combat
        self.ecran = ecran



    def maj(self):
        self.ecran.blit(self.fond, (0, 0))