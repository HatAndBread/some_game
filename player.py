import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: [int, int], height: int, width: int):
        super(Player, self).__init__()
        self.pos = pos
        self.surface = pygame.Surface((height, width))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect()

    def move_up(self, distance):
        self.pos[1] -= distance

    def move_down(self, distance):
        self.pos[1] += distance

    def move_left(self, distance):
        self.pos[0] -= distance

    def move_right(self, distance):
        self.pos[0] += distance
