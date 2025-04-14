from circleshape import *
from constants import *

class Asteroid(CircleShape):
    """
    """
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        color = "red"
        pygame.draw.circle(screen,color,self.position, self.radius,width=2)

    def update(self, dt):
        """
        Override the update() method so that it moves in a straight line at constant speed.
        On each frame, it should add (self.velocity * dt) to its position
        (get self.velocity from its parent class, CircleShape).
        """
        self.position += self.velocity * dt

