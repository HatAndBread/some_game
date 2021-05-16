import pygame
from random import randint
from circle import Circle
from pygame.locals import *
# import locals for mypy assist?

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

my_circle = Circle([SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((randint(150, 158), randint(0, 32), randint(12, 21)))
    my_circle.wander()
    pygame.draw.circle(screen, my_circle.color, my_circle.pos, 75)

    pygame.display.flip()
pygame.quit()
