# import statements
import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game_objects.asteroid.asteroid import Asteroid
from game_objects.asteroid.asteroidfield import AsteroidField
from game_objects.player.player import Player
from game_objects.player.shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    #define groups
    Player.containers = pygame.sprite.Group()
    Asteroid.containers = pygame.sprite.Group()
    AsteroidField.containters = pygame.sprite.Group()
    Shot.containers = pygame.sprite.Group()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    # create the player object
    # **IMPORTANT** player objects MUST be created AFTER the static class field of containers (like shown above) is added to the player class
    # this ensures that each instance of a created player class is added to the container collection
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()





    # set FPS
    fps = pygame.time.Clock()
    delta_time = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(delta_time)
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game Over!")
                sys.exit()
            else:
                for shot in shots:
                    if shot.detect_collision(asteroid):
                        asteroid.split()
                        shot.kill()


        screen.fill("black")
        for item in drawables:
            item.draw(screen)
        pygame.display.flip()

        # the tick method returns the delta time(difference in time) between now and the last time the tick method is called (in seconds)
        # by passing in 60 we are targeting a limited 60 frames per second refresh, to keep frames consistent and not tied to current cpu speed
        # dividing the returned value from the tick call by 1000 we are converting from milliseconds to seconds
        delta_time = fps.tick(60) / 1000


    #print("Starting asteroids!")

if __name__ == "__main__":
    main()