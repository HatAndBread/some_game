import pygame
from random import randint
from pygame.locals import *
# import locals for mypy assist?

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Circle:
    def __init__(self, pos=[SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2], radius=100, color=[250, 50, 87]):
        self.__pos = pos
        self.__radius = radius
        self.__color = color

    def get_pos(self):
        return self.__pos

    def update_pos(self, pos: list):
        self.__pos = pos

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius: int):
        self.__radius = radius

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


my_circle = Circle()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((randint(150, 158), randint(0, 32), randint(12, 21)))
    pygame.draw.circle(screen, my_circle.get_color, my_circle.get_pos, 75)

    pygame.display.flip()
pygame.quit()
