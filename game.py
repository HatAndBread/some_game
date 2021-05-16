import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
    pygame.display.flip()
pygame.quit()
