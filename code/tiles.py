import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILE_SIZE, TILE_SIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        y_offset = HIT_BOX_OFFSET[sprite_type]
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - TILE_SIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hit_box = self.rect.inflate(0, y_offset)
