import pygame

class Score:
    def __init__(self, widthScreen):
        pygame.font.init()
        self.__font = pygame.font.Font("font/Monocraft.otf", widthScreen // 30)
        self.__stepForCounter = 0
        self.__counterPoints = 0

    def resizeScreen(self, widthScreen):
        self.__font = pygame.font.Font("font/Monocraft.otf", widthScreen // 30)

    def logic(self):
        self.__stepForCounter += 1
        if self.__stepForCounter == 20:
            self.__stepForCounter = 0
            self.__counterPoints += 1

    def draw(self, screen):
        screen.blit(self.__font.render(f"Score: {self.__counterPoints}", True, (255, 255, 255)), (0, 0))

    def add_score_in_file(self):
        with open("score/score.txt", "w") as file:
            file.write(str(self.__counterPoints))
