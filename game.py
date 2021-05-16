import pygame
from random import randint
from circle import Circle
from player import Player
from pygame.locals import *
# import locals for mypy assist?

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

my_circle = Circle([SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2])
player = Player([100, 100], 50, 50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running == False
        elif event.type == pygame.QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_DOWN]:
        player.move_down(1)
    if pressed_keys[pygame.K_UP]:
        player.move_up(1)
    if pressed_keys[pygame.K_LEFT]:
        player.move_left(1)
    if pressed_keys[pygame.K_RIGHT]:
        player.move_right(1)
    screen.fill((0, 0, 0))
    my_circle.wander()
    pygame.draw.circle(screen, my_circle.color, my_circle.pos, 75)
    screen.blit(player.surface, player.pos)
    pygame.display.flip()

pygame.quit()
