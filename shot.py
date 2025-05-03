import pygame
import constants

from circleshape import CircleShape


class Shot(CircleShape):
    containers = tuple()

    def __init__(self, x,y):
        super().__init__(x,y,constants.SHOT_RADIUS)

    def draw(self, screen):
        width = 2
        pygame.draw.circle(screen, "red", self.position, constants.SHOT_RADIUS, width)

    def update(self, dt):
        self.position += self.velocity * dt
