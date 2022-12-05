import pygame
# from level import Level
from auxiliar import Aux
from constantes import *


class Bullet:
    def __init__(self, entity, instance, pos_x, flip, mouse_xy=''):
        # self.bullet = pygame.draw.rect(surface, RED, (x, y, 3, 3))
        # self.bullet = Aux.get_surface_from_sprite(PATH_IMAGE+'/assets/bullet/bullet.png',1,4,2)
        self.bullet = Aux.get_surface_from_sprite(PATH_IMAGE+'/assets/bullet/bullet_3.png',1,1)

        # entity
        self.entity = entity # NUEVO
        self.pj_instance = instance

        # FPS
        self.anim_frame_rate = 85
        self.frame_sum_anim = 0

        # media
        self.flip_x = flip
        self.frame = 0
        self.image = pygame.transform.flip(self.bullet[self.frame], self.flip_x, False)
        self.rect_pj = pos_x
        self.rect_pj_mouse = mouse_xy
        self.rect = self.image.get_rect(center = self.rect_pj)
        # self.rect.center = pos_xy

    
        # movement
        self.direction = pygame.math.Vector2(0, 0)
        self.is_shooting = False
        self.speed = 17


    """ def shoot(self, pos_xy: tuple, flip: bool):
        self.is_shooting = True
        self.rect.center = pos_xy
        if flip:
            self.direction.x = -1
        else:
            self.direction.x = 1
        self.flip_x = flip """

    """ def upd_animation(self, delta_ms):
        self.frame_sum_anim += delta_ms
        if self.frame_sum_anim >= self.anim_frame_rate:
            self.frame_sum_anim = 0

            self.frame += 1
            self.check_frame_index()
    
    def check_frame_index(self):
        if self.frame + 1 >= len(self.bullet):
            self.frame = 0 """


    def move_rect_x(self):
        self.is_shooting = True
        if self.flip_x:
            self.direction.x = -1
        else:
            self.direction.x = 1
        self.rect.x += self.direction.x * self.speed

    """ def move_rect_y(self):
        if self.rect_pj_mouse:
            if self.rect_pj_mouse[1] < self.rect_pj[1]:
                # print('SUBIRRRR')
                self.direction.y = -1
            elif self.rect_pj_mouse[1] > self.rect_pj[1]:
                # print('BAJARRRR')
                self.direction.y = 1
            elif self.rect_pj_mouse[1] == self.rect_pj[1]:
                # print('BAJARRRR')
                self.direction.y = 0
            self.rect.y += self.direction.y * self.speed """

    def update(self, delta_ms=''):
        ## animation ##
        # self.upd_animation(delta_ms)

        ## movement ##
        self.move_rect_x()
        # self.move_rect_y()
    
    def draw(self, surface):
        if self.is_shooting:
            if DEBUG: 
                pygame.draw.rect(surface, RED, self.rect)

            self.image = pygame.transform.flip(self.bullet[self.frame], self.flip_x, False)
            surface.blit(self.image, self.rect)
