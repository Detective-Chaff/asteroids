import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from game_objects.circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    # The split method will spawn 2 new asteroids from the current caller asteroid as long as the current asteroid has radius larger
    # than the ASTEROID_MIN_RADIUS.
    # The new asteroids will spawn opposite each other based on a random angle between 20 and 50 degrees of the current asteroids facing direction
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # get angle value
            new_angle = random.uniform(20, 50)
            # set new radius
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # set new direction of each asteroid based off of the new new angle from current asteroid's facing direction
            # asteroid1's direction is the result of rotating the calling asteroids durrent direction by the new angle value
            # to ensure the 2 new asteroids are spawned opposite each other
            # asteroid2's direction is the result of rotating the calling asteroids durrent direction by the negative new angle value
            direction1 = self.velocity.rotate(new_angle)
            direction2 = self.velocity.rotate(-new_angle)
            
            # Create new asteroids
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            #set new velocities of new asteroids and increase their speed
            asteroid1.velocity = direction1 * 1.2
            asteroid2.velocity = direction2 * 1.2

