import pygame
from sys import exit

from ..objects import *

class Gameplay:
    def __init__(self, screen):
        self.__screen = screen
        self.__clock = pygame.time.Clock()
        self.__FPS = 60
        self.__lose = False
        self.__initObjects(*self.__screen.get_size())

    def __initObjects(self, width, height):
        self.__background = Background(width, height)
        self.__ground = Ground(width, height)
        self.__cloud = Cloud(width, height)
        self.__hero = Hero(width, height, self.__ground.y)
        self.__enemies = Enemies(width, height, self.__ground.y)
        self.__score = Score(width)

    def run(self):
        while not self.__lose:
            self.__checkEvents()
            self.__move()
            self.__logic()
            self.__draw()
        self.__score.add_score_in_file()

    def __checkEvents(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT or (events.type == pygame.KEYDOWN and events.key == pygame.K_ESCAPE):
                self.__exitFromGame()
            elif events.type == pygame.VIDEORESIZE:
                self.__resizeScreen()

    def __exitFromGame(self):
        pygame.quit()
        exit()

    def __resizeScreen(self):
        self.__background.resizeScreen(*self.__screen.get_size())
        self.__ground.resizeScreen(*self.__screen.get_size())
        self.__cloud.resizeScreen(*self.__screen.get_size())
        self.__hero.resizeScreen(*self.__screen.get_size(), self.__ground.y)
        self.__enemies.resizeScreen(*self.__screen.get_size(), self.__ground.y)
        self.__score.resizeScreen(self.__screen.get_width())

    def __move(self):
        self.__background.move()
        self.__ground.move()
        self.__cloud.move()
        self.__hero.move(pygame.key.get_pressed())
        self.__enemies.move()

    def __logic(self):
        self.__checkCollide()
        self.__background.logic()
        self.__ground.logic()
        self.__cloud.logic()
        self.__hero.logic()
        self.__enemies.logic()
        self.__score.logic()

    def __checkCollide(self):
        if self.__hero.rect.colliderect(self.__enemies.rect):
            self.__lose = True

    def __draw(self):
        self.__background.draw(self.__screen)
        self.__ground.draw(self.__screen)
        self.__cloud.draw(self.__screen)
        self.__hero.draw(self.__screen)
        self.__enemies.draw(self.__screen)
        self.__score.draw(self.__screen)

        pygame.display.flip()
        self.__clock.tick(self.__FPS)
