from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    """
    """
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        color = "red"
        pygame.draw.circle(screen,color,self.position, self.radius,width=2)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            random_angle = random.uniform(20,50)
            # Use the rotate method on the asteroid's velocity vector to create 2 new vectors,
            # that are rotated by random_angle and -random_angle respectively
            # (they should split in opposite directions).
            vector_1 = self.velocity.rotate(random_angle)
            vector_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = vector_1*1.2
            new_asteroid_2.velocity = vector_2*1.2
            self.kill()

    def update(self, dt):
        """
        Override the update() method so that it moves in a straight line at constant speed.
        On each frame, it should add (self.velocity * dt) to its position
        (get self.velocity from its parent class, CircleShape).
        """
        self.position += self.velocity * dt

