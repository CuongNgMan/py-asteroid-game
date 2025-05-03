
import pygame
import random

from circleshape import CircleShape
import constants


class Asteroid(CircleShape):
    containers = tuple()

    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        width = 2
        pygame.draw.circle(screen, "white", self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        asteroid_1 = self.create(self.position.x, self.position.y, new_radius)
        asteroid_2 = self.create(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = v1 * 1.2
        asteroid_2.velocity = v2 * 1.2

    def create(self, x, y, radius):
        return Asteroid(x,y, radius)
