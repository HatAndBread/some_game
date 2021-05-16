import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos: [int, int], radius: int, color: (int, int, int)):
        super(Enemy, self).__init__()
        self.pos = pos
        self.radius = radius
        self.surface = pygame.Surface([radius*2, radius*2], pygame.SRCALPHA)
        self.color = color
        self.rect = self.surface.get_rect()

    def draw(self):
        pygame.draw.circle(self.surface, self.color,
                           self.rect.center, self.radius)
