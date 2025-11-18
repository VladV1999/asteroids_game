import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
import player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import circleshape
def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    p = player.Player(x, y)
    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for object in asteroids:
            if object.collides_with(p):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)
        print(f"{dt}")


if __name__ == "__main__":
    main()
