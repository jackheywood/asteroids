import pygame
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, DESPAWN_MARGIN


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

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
