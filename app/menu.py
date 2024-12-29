import pygame
from sys import exit

from .game import Game

class Menu:
    def __init__(self, widthScreen, heightScreen):
        pygame.init()
        pygame.display.set_caption("Run, Grogu, run")
        pygame.display.set_icon(pygame.image.load("image/icon.png"))
        self.__widthScreen = widthScreen
        self.__heightScreen = heightScreen
        self.__screen = pygame.display.set_mode((self.__widthScreen, self.__heightScreen), pygame.RESIZABLE)
        self.__clockApp = pygame.time.Clock()
        self.__FPS = 30
        self.__runMenu = True

        self.__imageBackground = pygame.transform.scale(pygame.image.load("image/background.png"), (self.__widthScreen, self.__heightScreen))

        pygame.font.init()
        self.__font = pygame.font.Font("font/Monocraft.otf", self.__widthScreen // 30)
        self.__infoForStart = self.__font.render("To start the game, press any button", True, (255, 255, 255))
        self.__scoreInMenu = "Your score: {}"

    def run(self):
        while True:
            self.__menuStart()
            self.__gameStart()

    def __menuStart(self):
        self.__runMenu = True
        while self.__runMenu:
            self.__check_events()
            self.__drawScreen()

    def __check_events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT  or (events.type == pygame.KEYDOWN and events.key == pygame.K_ESCAPE):
                self.__exitFromApp()
            elif events.type == pygame.KEYDOWN:
                self.__runMenu = False
            elif events.type == pygame.VIDEORESIZE:
                self.__init__(*self.__screen.get_size())

    def __exitFromApp(self):
        pygame.quit()
        exit()

    def __drawScreen(self):
        self.__drawBackground()
        self.__drawText()
        pygame.display.flip()
        self.__clockApp.tick(self.__FPS)

    def __drawBackground(self):
        self.__screen.blit(self.__imageBackground, (0, 0))

    def __drawText(self):
        self.__screen.blit(self.__infoForStart, (self.__widthScreen // 2 - self.__infoForStart.get_width() // 2, self.__heightScreen // 2 - self.__infoForStart.get_height()))
        with open("score/score.txt", "r") as file:
            scoreText = self.__font.render(self.__scoreInMenu.format(file.readline()), True, (255, 255, 255))
        self.__screen.blit(scoreText, (self.__widthScreen // 2 - scoreText.get_width() // 2, self.__heightScreen // 2))

    def __gameStart(self):
        self.__gameGrogu = Game(self.__screen)
        self.__gameGrogu.run()
