import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, another: "CircleShape") -> bool:
        """
        Each CircleShape's position property is a pygame.Vector2.
        Use its distance_to method to calculate the distance between the two shapes.
        :param another: CircleShape
        :return: True/false
        """
        return self.position.distance_to(another.position) <= self.radius+another.radius


