import pygame as pg

class ChatBox:
    @staticmethod
    def textBox1(screen):
        color_black = (0, 0, 0)
        test_font = pg.font.SysFont("comicsansms", 30)
        screen.blit(test_font.render("Que voulez vous faire ?", True, color_black), (50, 640))



