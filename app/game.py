import pygame
from sys import exit

from .objects import *

class Game:
    def __init__(self, screen):
        self.__screen = screen
        self.__width, self.__height = self.__screen.get_size()
        self.__clock = pygame.time.Clock()
        self.__FPS = 30
        self.__lose = False

        self.__background = Background(self.__width, self.__height)
        self.__ground = Ground(self.__width, self.__height)
        self.__cloud = Cloud(self.__width, self.__height)
        self.__hero = Hero(self.__width, self.__height, self.__ground.y)
        self.__enemies = Enemies(self.__width, self.__height, self.__ground.y)
        self.__score = Score(self.__width)

    def run(self):
        while not self.__lose:
            self.__check_events()
            self.__move()
            self.__logic()
            self.__draw()
        self.__score.add_score_in_file()

    def __check_events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.__exitFromGame()

    def __exitFromGame(self):
        pygame.quit()
        exit()

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
