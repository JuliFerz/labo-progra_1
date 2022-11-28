import pygame
from auxiliar import Aux
from constantes import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, type=0):
        super().__init__()
        self.get_tiles()

        self.image = Aux.get_surface_from_sprite(
            PATH_IMAGE + '/tileset/sheet1.png', 8, 8)[type]
        self.image = pygame.transform.scale(self.image, (SIZE_TILE, SIZE_TILE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_collition = pygame.Rect(
            self.rect.x, self.rect.y + GROUND_RECT_BOTTOM, self.rect.w, self.rect.h - GROUND_RECT_BOTTOM)
        self.type = type

    def get_tiles(self):
        pass


""" class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, type=0):
        super().__init__()
        self.get_tiles()

        self.image = Aux.get_surface_from_sprite(PATH_IMAGE + '/tileset/sheet1.png', 8, 8)[type]
        self.image = pygame.transform.scale(self.image, (SIZE_TILE, SIZE_TILE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_collition = pygame.Rect(
            self.rect.x, self.rect.y + GROUND_RECT_BOTTOM, self.rect.w, self.rect.h - GROUND_RECT_BOTTOM)
        self.type = type

    def get_tiles(self):
        pass """


class NewPlatform(pygame.sprite.Sprite):
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
            ))
        self.image = pygame.transform.scale(self.image, (SIZE_TILE, SIZE_TILE))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.rect_collition = pygame.Rect(
            self.rect.x, self.rect.y + GROUND_RECT_BOTTOM, self.rect.w, self.rect.h - GROUND_RECT_BOTTOM)

