import pygame

class Background:
    def __init__(self, widthScreen, heightScreen):
        self.__image = pygame.transform.scale(pygame.image.load("image/world/background.png"), (widthScreen, heightScreen))
        self.__rect = self.__image.get_rect()
        self.__speed = widthScreen // 400

    def resizeScreen(self, widthScreen, heightScreen):
        self.__image = pygame.transform.scale(self.__image, (widthScreen, heightScreen))
        self.__rect.width, self.__rect.height = self.__image.get_size()
        self.__speed = widthScreen // 400

    def move(self):
        self.__rect.x -= self.__speed

    def logic(self):
        if self.__rect.x <= -self.__rect.width:
            self.__rect.x = 0

    def draw(self, screen):
        screen.blit(self.__image, self.__rect)
        screen.blit(self.__image, (self.__rect.x + self.__rect.width, self.__rect.y))
