from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
import pygame, sys
from constants import *
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    clock = pygame.time.Clock()
    dt = 0
    Shot.containers = (updateable, drawable, shots)
    AsteroidField.containers = updateable
    Asteroid.containers = (asteroid, updateable, drawable)
    Player.containers = (updateable, drawable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
        for a in asteroid:
            if a.is_coliding(player):
                print("Game Over!")
                sys.exit()
            for s in shots:
                if a.is_coliding(s):
                    s.kill()
                    a.split()

        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
