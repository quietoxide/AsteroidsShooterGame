import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,SHOT_RADIUS)
        
    def draw(self, screen: pygame.Surface) -> None:
        color = "white"
        own_position = self.position
        radius = self.radius
        width_line = LINE_WIDTH
        
        pygame.draw.circle(screen, color, own_position, radius, width_line)

    def update(self, dt: float)->None:
        self.position += self.velocity * dt


        