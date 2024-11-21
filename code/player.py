import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/player/0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hit_box = self.rect.inflate(0, -26)

        self.direction = pygame.math.Vector2()

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction.x -= PLAYER_SPEED
        elif keys[pygame.K_d]:
            self.direction.x += PLAYER_SPEED
        else:
            self.direction.x = 0

        if keys[pygame.K_w]:
            self.direction.y -= PLAYER_SPEED
        elif keys[pygame.K_s]:
            self.direction.y += PLAYER_SPEED
        else:
            self.direction.y = 0

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hit_box.x += self.direction.x * PLAYER_SPEED
        self.collisions('Horizontal')
        self.hit_box.y += self.direction.y * PLAYER_SPEED
        self.collisions('Vertical')
        self.rect.center = self.hit_box.center

    def collisions(self, direction):
        if direction == 'Horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hit_box.colliderect(self.hit_box):
                    if self.direction.x > 0:
                        self.hit_box.right = sprite.hit_box.left
                    if self.direction.x < 0:
                        self.hit_box.left = sprite.hit_box.right

        if direction == 'Vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hit_box.colliderect(self.hit_box):
                    if self.direction.y > 0:
                        self.hit_box.bottom = sprite.hit_box.top
                    if self.direction.y < 0:
                        self.hit_box.top = sprite.hit_box.bottom

    def update(self):
        self.input()
        self.move()
