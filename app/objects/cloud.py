import pygame

from random import randint

class Cloud:
    def __init__(self, widthScreen, heightScreen):
        self.__images = (
            pygame.transform.scale(pygame.image.load("image/world/cloud_1.png"), (widthScreen // 5, heightScreen // 10)),
            pygame.transform.scale(pygame.image.load("image/world/cloud_2.png"), (widthScreen // 5, heightScreen // 10))
        )
        self.__clouds = list()
        self.__defaultX = widthScreen
        self.__speed = widthScreen // 300

    def __createCloud(self):
        if randint(0, 100) > 99:
            self.__clouds.append([self.__images[randint(0, len(self.__images) - 1)], self.__generatePosition()])

    def __generatePosition(self):
        return [self.__defaultX, randint(0, self.__images[0].get_height())]

    def __deleteCloud(self):
        for cloud in self.__clouds:
            if cloud[1][0] <= -cloud[0].get_width():
                self.__clouds.remove(cloud)

    def resizeScreen(self, widthScreen, heightScreen):
        self.__images = (
            pygame.transform.scale(pygame.image.load("image/world/cloud_1.png"), (widthScreen // 5, heightScreen // 10)),
            pygame.transform.scale(pygame.image.load("image/world/cloud_2.png"), (widthScreen // 5, heightScreen // 10))
        )
        self.__resizeClouds()
        self.__defaultX = widthScreen
        self.__speed = widthScreen // 300

    def __resizeClouds(self):
        __width, __height = self.__images[0].get_size()
        for cloud in self.__clouds:
            cloud[0] = pygame.transform.scale(cloud[0], (__width, __height))

    def move(self):
        for cloud in self.__clouds:
            cloud[1][0] -= self.__speed

    def logic(self):
        self.__createCloud()
        self.__deleteCloud()

    def draw(self, screen):
        for cloud in self.__clouds:
            screen.blit(cloud[0], cloud[1])
