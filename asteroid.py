import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        # self.rotation = 0

    def draw(self, screen):
        # pygame.draw.polygon(screen, "white", self.triangle(), 2)
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # def rotate(self, dt):
    #     self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.position += self.velocity * dt

    # def move(self, dt):
    #     forward = pygame.Vector2(0, 1).rotate(self.rotation)
    #     self.position += forward * PLAYER_SPEED * dt
