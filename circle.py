from random import randint


class Circle:
    def __init__(self, pos=[100, 100], radius=100, color=[250, 50, 87]):
        self.pos = pos
        self.radius = radius
        self.color = color

    def wander(self):
        self.pos = [self.pos[0] + randint(-1, 1), self.pos[1] + randint(-1, 1)]
