import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    containers = tuple()
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)  # type: ignore
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius         # type: ignore
        b = self.position - forward * self.radius - right # type: ignore
        c = self.position - forward * self.radius + right # type: ignore
        return [a, b, c]

    def __rotate__(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def __move__(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.__move__(dt)
            
        if keys[pygame.K_s]:
            self.__move__(-dt)

        if keys[pygame.K_a]:
            self.__rotate__(-dt)

        if keys[pygame.K_d]:
            self.__rotate__(dt)
