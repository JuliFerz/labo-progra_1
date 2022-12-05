import pygame
from auxiliar import Aux
from constantes import *

class TilePlatform(pygame.sprite.Sprite):
    def __init__(self, name, type, sub_type, x, y):
        super().__init__()
        self.name = name
        self.type = type
        self.sub_type = sub_type
        self.x = x
        self.y = y
        # self.image = Aux.get_surface_from_file(PATH_IMAGE+f'/tileset/p_type')
        self.image = pygame.image.load(
            PATH_IMAGE+'/tileset/{}/{}/{}.png'.format(
                self.type, self.sub_type, self.name
            )).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SIZE_TILE, SIZE_TILE))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.rect_collition = pygame.Rect(
            self.rect.x, self.rect.y + GROUND_RECT_BOTTOM, self.rect.w, self.rect.h - GROUND_RECT_BOTTOM)

