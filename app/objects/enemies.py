import pygame

from random import randint

class Enemies:
    def __init__(self, widthScreen, heightScreen, groundY):
        self.__images = (
        pygame.transform.scale(pygame.image.load("image/enemies/trooper.png"), (widthScreen // 10, heightScreen // 10)),
        pygame.transform.scale(pygame.image.load("image/enemies/droid.png"), (widthScreen // 10, heightScreen // 10)),
        pygame.transform.scale(pygame.image.load("image/enemies/gideon.png"), (widthScreen // 10, heightScreen // 10)),
        pygame.transform.scale(pygame.image.load("image/enemies/jawa.png"), (widthScreen // 10, heightScreen // 10)))
        self.__image = self.__images[randint(0, len(self.__images) - 1)]
        self.__rect = self.__image.get_rect()
        self.__startX = widthScreen
        self.__rect.y = groundY - self.__image.get_height()
        self.__rect.x = self.__startX
        self.__speed = widthScreen // 70

    def move(self):
        self.__rect.x -= self.__speed

    def __createEnemy(self):
        if randint(0, 100) > 90:
            self.__rect.x = self.__startX
            self.__image = self.__images[randint(0, len(self.__images) - 1)]

    def logic(self):
        if self.__rect.x < -self.__rect.width:
            self.__createEnemy()

    def draw(self, screen):
        screen.blit(self.__image, self.__rect)

    @property
    def rect(self):
        return self.__rect
