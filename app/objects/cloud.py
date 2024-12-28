import pygame

from random import randint

class Cloud:
    def __init__(self, widthScreen, heightScreen):
        self.__images = (
            pygame.transform.scale(pygame.image.load("image/world/cloud_1.png"), (widthScreen // 5, heightScreen // 10)),
            pygame.transform.scale(pygame.image.load("image/world/cloud_2.png"), (widthScreen // 5, heightScreen // 10))
        )
        self.__image = self.__images[randint(0, len(self.__images) - 1)]
        self.__rect = self.__images[0].get_rect()
        self.__defaultX = widthScreen
        self.__rect.x = self.__defaultX
        self.__speed = widthScreen // 70

    def move(self):
        self.__rect.x -= self.__speed

    def __create_cloud(self):
        if randint(0, 100) > 90:
            self.__rect.x = self.__defaultX
            self.__image = self.__images[randint(0, len(self.__images) - 1)]


    def logic(self):
        if self.__rect.x < -self.__rect.width:
            self.__create_cloud()

    def draw(self, screen):
        screen.blit(self.__image, self.__rect)
