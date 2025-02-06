import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)

        split_velocity_1 = self.velocity.rotate(angle)
        split_velocity_2 = self.velocity.rotate(-angle)

        self.__spawn_split_asteroid(split_velocity_1)
        self.__spawn_split_asteroid(split_velocity_2)

    def __spawn_split_asteroid(self, velocity):
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid.velocity = velocity * 1.2
