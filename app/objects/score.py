import pygame

class Score:
    def __init__(self, widthScreen):
        pygame.font.init()
        self.__font = pygame.font.SysFont('Comic Sans MS', widthScreen // 30)
        self.__scoreText = str()
        self.__stepForCounter = 0
        self.__counterPoints = 0

    def logic(self):
        self.__stepForCounter += 1
        if self.__stepForCounter == 10:
            self.__stepForCounter = 0
            self.__counterPoints += 1
        self.__scoreText = self.__font.render(f"Score: {self.__counterPoints}", True, (255, 255, 255))

    def draw(self, screen):
        screen.blit(self.__scoreText, (0, 0))
