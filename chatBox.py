import pygame as pg

class ChatBox:

    @staticmethod
    def textBox1(screen):
        fond = pg.Rect(50, 640, 500, 200)
        pg.draw.rect(screen, (255, 255, 255), fond)
        color_black = (0, 0, 0)
        test_font = pg.font.SysFont("comicsansms", 30)
        screen.blit(test_font.render("Que voulez vous faire ?", True, color_black), (50, 640))

    @staticmethod
    def textAttack(screen, nomPokemon, nomAttack):

        fond = pg.Rect(50, 640, 500, 200)
        pg.draw.rect(screen, (255, 255, 255), fond)
        color_black = (0, 0, 0)
        attackFont = pg.font.SysFont("comicsansms", 30)
        screen.blit(attackFont.render(f"{nomPokemon} utilise {nomAttack} !", True, color_black), (50, 640))

        color_black = (0, 0, 0)
        attackFont = pg.font.SysFont("comicsansms", 30)
        screen.blit(attackFont.render(f"{nomPokemon} utilise {nomAttack} !", True, color_black), (50, 640))

    @staticmethod
    def textIdentification(screen, nomPokemon):
        color_black = (0, 0, 0)
        identificationFont = pg.font.SysFont("comicsansms", 30)
        screen.blit(identificationFont.render(f"{nomPokemon} était un bon pot de Poke-yaourt ?", True, color_black), (50, 640))



    @staticmethod
    def textIdentification(screen, nomPokemon):
        fond = pg.Rect(50, 640, 500, 200)
        pg.draw.rect(screen, (255, 255, 255), fond)
        color_black = (0, 0, 0)
        identificationFont = pg.font.SysFont("comicsansms", 30)
        screen.blit(identificationFont.render(f"{nomPokemon} était un bon pot de Poke-yaourt ?", True, color_black), (50, 640))

    @staticmethod
    def textVictoire(screen, nomPokemonPerdant, nomPokemonGagnant):
        color_black = (0, 0, 0)
        texteVictoire = pg.font.SysFont("comicsansms", 30)
        screen.blit(texteVictoire.render(f"{nomPokemonPerdant} est ko ! {nomPokemonGagnant} gagne le combat !", True, color_black),
                    (50, 640))
