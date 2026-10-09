import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        color = "white"
        own_position = self.position
        radius = self.radius
        width_line = LINE_WIDTH
        
        pygame.draw.circle(screen, color, own_position, radius, width_line)

    def update(self, dt: float)->None:

        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            
            a1_new_vector = self.velocity.rotate(random_angle)
            a2_new_vector = self.velocity.rotate(-random_angle)

            smaller_a_new_radius = self.radius - ASTEROID_MIN_RADIUS

            a1 = Asteroid(self.position.x, self.position.y, smaller_a_new_radius)
            a2 = Asteroid(self.position.x, self.position.y, smaller_a_new_radius)

            a1.velocity = a1_new_vector * 1.2
            a2.velocity = a2_new_vector * 1.2