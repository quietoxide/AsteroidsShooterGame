import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    # SETUP
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # GAME VARIABLES
    clock = pygame.time.Clock()
    dt = 0.0

    # CONTAINERS
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, drawable, updatable)
    
    # RUNNING GAME LOOP
    while True:
        log_state()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        # COLLISION CHECK
        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for a in asteroids:
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()
            
        screen.fill("black")
    
        for sprite in drawable:
            sprite.draw(screen)
    
        pygame.display.flip()


    # CONSOLE GREETS
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
