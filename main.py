# import statements
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game_objects.player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    #define groups
    Player.containers = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)

    # create the player object
    # **IMPORTANT** player objects MUST be created AFTER the static class field of containers (like shown above) is added to the player class
    # this ensures that each instance of a created player class is added to the container collection
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)





    # set FPS
    fps = pygame.time.Clock()
    delta_time = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(delta_time)

        screen.fill("black")
        for item in drawables:
            item.draw(screen)
        pygame.display.flip()

        delta_time = fps.tick(60) / 1000


    #print("Starting asteroids!")

if __name__ == "__main__":
    main()