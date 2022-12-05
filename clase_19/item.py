import pygame
from auxiliar import Aux
from constantes import *


class Item:
    def __init__(
            self,
            manager,
            entity,
            c_type,
            sub_type,
            name,
            mvm_frame_rate,
            anim_frame_rate,
            rows,
            columns,
            points,
            health,
            bullets,
            level_tiles=[],
            scale=32,
            x=0,
            y=0
            ):
        self._manager = manager
        
        # Sprites
        self.type = c_type
        self.sub_type = sub_type
        self.name = name
        self.item = Aux.get_surface_from_sprite(PATH_IMAGE + f'/{self.type}/{self.sub_type}/{self.name}.png', rows, columns)

        # Platforms
        self.level_tiles = level_tiles
        self.entity = entity

        # fps
        self.frame = 0
        self.frame_sum_mov = 0
        self.frame_sum_anim = 0
        self.mvm_frame_rate = mvm_frame_rate
        self.anim_frame_rate = anim_frame_rate

        # media
        self.scale = scale
        self.image = self.item[self.frame]
        self.image = pygame.transform.scale(self.image, (self.scale ,self.scale))

        # main rect
        self.rect = self.image.get_rect()

        # spawn
        self.rect.x = x
        self.rect.y = y

        # others
        self.points = points
        self.health = health
        self.bullets = bullets


    def upd_animation(self, delta_ms):
        self.frame_sum_anim += delta_ms
        if self.frame_sum_anim >= self.anim_frame_rate:
            self.frame_sum_anim = 0

            self.frame += 1
            self.check_frame_index()

    def check_frame_index(self):
        if self.frame + 1 >= len(self.item):
            self.frame = 0

    def update(self, delta_ms):
        self.frame_sum_mov += delta_ms
        if self.frame_sum_mov >= self.mvm_frame_rate:
            self.frame_sum_mov = 0

            self.upd_animation(delta_ms)
            self._manager.collide_rect()

    def draw(self, surface):
        if DEBUG:
            pygame.draw.rect(surface, RED, self.rect)
        self.image = self.item[self.frame]
        self.image = pygame.transform.scale(self.image, (self.scale ,self.scale))
        
        surface.blit(self.image, self.rect)