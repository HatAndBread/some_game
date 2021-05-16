import pygame
from random import randint
from circle import Circle
from player import Player
from enemy import Enemy
from pygame.locals import *
# import locals for mypy assist?

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

my_circle = Circle([SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2])
player = Player([100, 100], 50, 50)

enemies = pygame.sprite.Group()

for num in range(0, 5):
    enemies.add(Enemy([randint(0, SCREEN_WIDTH), randint(
        0, SCREEN_HEIGHT)], 30, (210, 142, 12)))

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
    screen.fill((200, 200, 200))
    my_circle.wander()
    pygame.draw.circle(screen, my_circle.color, my_circle.pos, 75)
    screen.blit(player.surface, player.pos)
    for en in enemies.sprites():
        screen.blit(en.surface, en.pos)
        en.draw()
    if pygame.sprite.spritecollideany(player, enemies):
        print('There was a collision!')
    pygame.display.flip()

pygame.quit()
