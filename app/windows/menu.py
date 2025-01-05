import pygame
from sys import exit

class Menu:
    def __init__(self, screen):
        self.__screen = screen
        self.__widthScreen, self.__heightScreen = self.__screen.get_size()
        self.__clock = pygame.time.Clock()
        self.__FPS = 30
        self.__runMenu = True
        self.__imageBackground = pygame.transform.scale(pygame.image.load("image/background.png"), (self.__widthScreen, self.__heightScreen))
        self.__initFont()

    def __initFont(self):
        pygame.font.init()
        self.__font = pygame.font.Font("font/Monocraft.otf", self.__widthScreen // 30)
        self.__infoForStart = self.__font.render("To start the game, press any button", True, (255, 255, 255))
        self.__scoreInMenu = "Your score: {}"

    def run(self):
        self.__runMenu = True
        while self.__runMenu:
            self.__checkEvents()
            self.__drawScreen()

    def __checkEvents(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT  or (events.type == pygame.KEYDOWN and events.key == pygame.K_ESCAPE):
                self.__exitFromGame()
            elif events.type == pygame.KEYDOWN:
                self.__runMenu = False
            elif events.type == pygame.VIDEORESIZE:
                self.__resizeWindow()

    def __resizeWindow(self):
        self.__widthScreen, self.__heightScreen = self.__screen.get_size()
        self.__imageBackground = pygame.transform.scale(pygame.image.load("image/background.png"), (self.__widthScreen, self.__heightScreen))
        self.__initFont()

    def __exitFromGame(self):
        pygame.quit()
        exit()

    def __drawScreen(self):
        self.__drawBackground()
        self.__drawText()

        pygame.display.flip()
        self.__clock.tick(self.__FPS)

    def __drawBackground(self):
        self.__screen.blit(self.__imageBackground, (0, 0))

    def __drawText(self):
        self.__screen.blit(self.__infoForStart, (self.__widthScreen // 2 - self.__infoForStart.get_width() // 2, self.__heightScreen // 2 - self.__infoForStart.get_height()))
        with open("score/score.txt", "r") as file:
            scoreText = self.__font.render(self.__scoreInMenu.format(file.readline()), True, (255, 255, 255))
        self.__screen.blit(scoreText, (self.__widthScreen // 2 - scoreText.get_width() // 2, self.__heightScreen // 2))
