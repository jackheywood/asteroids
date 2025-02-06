import pygame
from constants import *


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color="white"):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.is_offscreen():
            self.kill()

    def is_offscreen(self):
        return (
                self.position.x > SCREEN_WIDTH + self.radius + DESPAWN_MARGIN
                or self.position.x < -self.radius - DESPAWN_MARGIN
                or self.position.y > SCREEN_HEIGHT + self.radius + DESPAWN_MARGIN
                or self.position.y < -self.radius - DESPAWN_MARGIN
        )

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
