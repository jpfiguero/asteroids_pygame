from circleshape import *
from constants import *

class Player(CircleShape):
    """
    The Player constructor should take x and y integers as input, then:
    Call the parent class's constructor, also passing in PLAYER_RADIUS
    Create a field called rotation, initialized to 0
    """
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """
        To draw the player, override the draw method of CircleShape.
        It should take the screen object as a parameter, and call pygame.draw.polygon.
        It takes:
        - The screen object
        - A color (use "white")
        - A list of points (use self.triangle() that we provided for you)
        - A line width (use 2)
        """
        color = "white"
        points = self.triangle()
        width = 2
        pygame.draw.polygon(screen, color, points, width)
