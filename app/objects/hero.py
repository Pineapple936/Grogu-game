import pygame

class Hero:
    def __init__(self, widthScreen, heightScreen, groundY):
        self.__images = {
            "run": (
                pygame.transform.scale(pygame.image.load("image/grogu/grogu_run_1.png"), (widthScreen // 10, heightScreen // 10)),
                pygame.transform.scale(pygame.image.load("image/grogu/grogu_run_2.png"), (widthScreen // 10, heightScreen // 10))),
            "jump": pygame.transform.scale(pygame.image.load("image/grogu/grogu_jump.png"), (widthScreen // 10, heightScreen // 10))
        }
        self.__image = self.__images["run"][0]
        self.__defaultY = groundY - self.__image.get_height()
        self.__rect = self.__image.get_rect()
        self.__rect.y = self.__defaultY
        self.__jumpStatus = False
        self.__defaultJumpSpeed = heightScreen // 12
        self.__jumpSpeed = self.__defaultJumpSpeed
        self.__verticalVelocity = heightScreen // 120
        self.__animCount = 0

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
        self.__switch_animation()

    def __switch_animation(self):
        if self.__jumpStatus:
            self.__image = self.__images["jump"]
        else:
            self.__animCount += 1
            if self.__animCount // 5 == 1 or self.__animCount // 5 == 2:
                self.__image = self.__images["run"][self.__animCount // 5 - 1]

            if self.__animCount == 10:
                self.__animCount = 0


    def draw(self, screen):
        screen.blit(self.__image, self.__rect)

    @property
    def rect(self):
        return self.__rect
