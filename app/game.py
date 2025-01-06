from .windows import *

import pygame

class Game:
    def __init__(self, widthScreen, heightScreen):
        pygame.init()
        pygame.display.set_caption("Run, Grogu, run")
        pygame.display.set_icon(pygame.image.load("image/icon.png"))
        pygame.mouse.set_visible(False)
        self.__screen = pygame.display.set_mode((widthScreen, heightScreen), pygame.RESIZABLE)

    def run(self):
        while True:
            self.__startMenu()
            self.__startGame()

    def __startMenu(self):
        self.__menu = Menu(self.__screen)
        self.__menu.run()

    def __startGame(self):
        self.__game = Gameplay(self.__screen)
        self.__game.run()
