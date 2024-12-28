import pygame

from .objects import *

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.__screen = pygame.display.set_mode((width, height))
        self.__clock = pygame.time.Clock()
        self.__FPS = 30
        self.__lose = False

        self.__background = Background(width, height)
        self.__ground = Ground(width, height)
        self.__cloud = Cloud(width, height)
        self.__hero = Hero(width, height, self.__ground.y)
        self.__enemies = Enemies(width, height, self.__ground.y)
        self.__score = Score(width)

    def run(self):
        while not self.__lose:
            self.__check_events()
            self.__move()
            self.__logic()
            self.__draw()

    def __check_events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.__lose = True

    def __move(self):
        self.__background.move()
        self.__ground.move()
        self.__cloud.move()
        self.__hero.move(pygame.key.get_pressed())
        self.__enemies.move()

    def __checkCollide(self):
        if self.__hero.rect.colliderect(self.__enemies.rect):
            self.__lose = True

    def __logic(self):
        self.__checkCollide()
        self.__background.logic()
        self.__ground.logic()
        self.__cloud.logic()
        self.__hero.logic()
        self.__enemies.logic()
        self.__score.logic()

    def __draw(self):
        self.__background.draw(self.__screen)
        self.__ground.draw(self.__screen)
        self.__cloud.draw(self.__screen)
        self.__hero.draw(self.__screen)
        self.__enemies.draw(self.__screen)
        self.__score.draw(self.__screen)

        pygame.display.flip()
        self.__clock.tick(self.__FPS)


if __name__ == "__main__":
    game = Game(900, 500)
    game.run()
