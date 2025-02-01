import pygame
from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOT_COOLDOWN, PLAYER_SHOT_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED
from game_objects.circleshape import CircleShape
from game_objects.player.shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "White", self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        #decrease shot timer
        self.timer -= dt

        # player forward / backward movement
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        #player turning
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        #player shoot
        if keys[pygame.K_SPACE]:
            self.shoot()

    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        self.timer = PLAYER_SHOT_COOLDOWN
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, PLAYER_SHOT_RADIUS)
        shot.velocity = forward * PLAYER_SHOOT_SPEED