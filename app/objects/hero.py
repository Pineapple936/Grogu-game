import pygame

class Hero:
    def __init__(self, widthScreen, heightScreen, groundY):
        self.__image = pygame.transform.scale(pygame.image.load("image/grogu/grogu_start.png"), (widthScreen // 10, heightScreen // 10))
        self.__defaultY = groundY - self.__image.get_height()
        self.__rect = self.__image.get_rect()
        self.__rect.y = self.__defaultY
        self.__jumpStatus = False
        self.__defaultJumpSpeed = heightScreen // 12
        self.__jumpSpeed = self.__defaultJumpSpeed
        self.__verticalVelocity = heightScreen // 120

    def __check_button(self, keys):
        if keys[pygame.K_SPACE] and not self.__jumpStatus:
            self.__jumpStatus = True
            self.__jumpSpeed = self.__defaultJumpSpeed

    def __jump(self):
        if self.__jumpStatus:
            self.__rect.y -= self.__jumpSpeed
            self.__jumpSpeed -= self.__verticalVelocity

    def move(self, keys):
        self.__check_button(keys)
        self.__jump()

    def logic(self):
        if self.__rect.y > self.__defaultY:
            self.__jumpStatus = False
            self.__rect.y = self.__defaultY

    def draw(self, screen):
        screen.blit(self.__image, self.__rect)

    @property
    def rect(self):
        return self.__rect
