import pygame
from auxiliar import Aux
from constantes import *


class Npc:
    def __init__(self, name,speed_frame=1):
        # LISTAS - Sprites
        self.stay = Aux.get_surface_from_sprite(
            PATH_IMAGE + f'/inhabitants/{name}/idle.png', 1, 9)  # quieto 
        self.stay_2 = Aux.get_surface_from_sprite(
            PATH_IMAGE + f'/inhabitants/{name}/idle_2.png', 6, 15)  # quieto 
        # self.appear = Aux.get_surface_from_sprite(
            # PATH_IMAGE + f'/inhabitants/{name}/appear.png', 9, 3)[:24]  # aparecer 
        # self.disappear = Aux.get_surface_from_sprite(
            # PATH_IMAGE + f'/inhabitants/{name}/disappear.png', 10, 3)  # desaparecer 
        # self.walk = Aux.get_surface_from_sprite(
        #     PATH_IMAGE + f'/inhabitants/{name}/walk.png', 6, 3)[:15]  # caminar 
        self.talk = Aux.get_surface_from_sprite(
            PATH_IMAGE + f'/inhabitants/{name}/talk.png', 6, 15)  # feliz 

        # imagenes
        self.frame = 0
        self.speed_frame = speed_frame
        self.animation = self.stay_2 # qué animación se hizo última - toma un array
        self.flip_x = False
        self.flip_y = False
        self.image = pygame.transform.flip(self.animation[self.frame], self.flip_x, self.flip_y)  # tomar una imagen del array
        self.rect = self.image.get_rect()  # toma el rectangulo de esa imagen

        self.rect.x = ANCHO_VENTANA - 800 # HARDCODED
        self.rect.y = ALTO_VENTANA - 310 # HARDCODED
        self.rect_pj = pygame.Rect(
            self.rect.x - 18, self.rect.y + 25, self.rect.width + 28, self.rect.height + 25) 
        # rect para interacciones

        # movimiento
        self.talking = False
        self.move_x = 0 # no
        self.speed_walk = 2 # no
        self.speed_run = 6 # no
        self.speed = self.speed_walk # no

        # JUMP
        self.can_jump = True # no
        self.is_jumping = False # no
        self.GRAVITY = 0.4 # no
        self.altura_salto = 20 # no
        self.y_velocity = self.altura_salto # no

    def control(self, list_keys=''): # no
        # print(self.rect.x)
        """ if list_keys:
            if list_keys[pygame.K_LEFT]:
                # self.flip_x = False
                if self.flip_x:
                    self.flip_x = False
                    # self.rect.x = 665
                    self.rect.x += 65
                self.animation = self.walk
                self.move_x = -self.speed
            if list_keys[pygame.K_RIGHT]:
                # self.flip_x = True
                if not self.flip_x:
                    self.flip_x = True
                    # self.rect.x = 590
                    self.rect.x -= 68

                self.animation = self.walk
                self.move_x = self.speed
            # if list_keys[pygame.K_s] or list_keys[pygame.K_DOWN]:
                # pass
        else:
            self.move_x = 0
            self.animation = self.stay
            self.speed = self.speed_walk """

    def colicion(self, obj=''):
        # self.talking = False
        # print(self.talking)
        if pygame.Rect.colliderect(self.rect_pj, obj):
            self.talking = True
            self.animation = self.talk
        else:
            self.talking = False
            

    def update(self, obj=''):
        if not self.talking:
            self.animation = self.stay_2
        
        # relentizar fotogramas de pj (lower than game fps (60))
        self.frame += self.speed_frame
        if self.frame >= len(self.animation):
            self.frame = 0
            self.animation = self.stay_2
            self.talking = False

        if obj.x > self.rect.x:
            self.flip_x = True
        else:
            self.flip_x = False
            

        # self.rect.x += self.move_x

    def draw(self, surface):
        self.image = pygame.transform.flip(self.animation[int(self.frame)], self.flip_x, False)
        surface.blit(self.image, self.rect)
