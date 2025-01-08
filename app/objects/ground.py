import pygame

class Ground:
    def __init__(self, widthScreen, heightScreen):
        self.__imageGround = pygame.transform.scale(pygame.image.load("image/world/ground.png"), (widthScreen, heightScreen // 4))
        self.__rectGround = self.__imageGround.get_rect()
        self.__rectGround.y = heightScreen - self.__rectGround.height

        self.__imageHorizon = pygame.transform.scale(pygame.image.load("image/world/horizon.png"), (widthScreen, heightScreen // 4))
        self.__rectHorizon = self.__imageHorizon.get_rect()
        self.__rectHorizon.y = self.__rectGround.y - self.__rectHorizon.height

        self.__speed = widthScreen // 70

    def resizeScreen(self, widthScreen, heightScreen):
        self.__imageGround = pygame.transform.scale(pygame.image.load("image/world/ground.png"), (widthScreen, heightScreen // 4))
        self.__rectGround.width, self.__rectGround.height = self.__imageGround.get_size()
        self.__rectGround.y = heightScreen - self.__rectGround.height

        self.__imageHorizon = pygame.transform.scale(pygame.image.load("image/world/horizon.png"), (widthScreen, heightScreen // 4))
        self.__rectHorizon.width, self.__rectHorizon.height = self.__imageHorizon.get_size()
        self.__rectHorizon.y = self.__rectGround.y - self.__rectHorizon.height

        self.__speed = widthScreen // 70



    def move(self):
        self.__rectHorizon.x -= self.__speed
        self.__rectGround.x -= self.__speed

    def logic(self):
        if self.__rectHorizon.x < -self.__rectHorizon.width:
            self.__rectHorizon.x = 0
            self.__rectGround.x = 0

    def __draw_horizon(self, screen):
        screen.blit(self.__imageHorizon, self.__rectHorizon)
        screen.blit(self.__imageHorizon, (self.__rectHorizon.x + self.__rectHorizon.width, self.__rectHorizon.y))

    def __draw_background(self, screen):
        screen.blit(self.__imageGround, self.__rectGround)
        screen.blit(self.__imageGround, (self.__rectGround.x + self.__rectGround.width, self.__rectGround.y))


    def draw(self, screen):
        self.__draw_horizon(screen)
        self.__draw_background(screen)

    @property
    def y(self):
        return self.__rectGround.y
