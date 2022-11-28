import pygame
from auxiliar import Aux
from constantes import *


class Npc:
    def __init__(self, name,speed_frame=1):
        # LISTAS - Sprites
        self.stay = Aux.get_surface_from_sprite(
            PATH_IMAGE + f'/inhabitants/{name}/idle.png', 3, 16)
        self.move_start = Aux.get_surface_from_sprite(
            PATH_IMAGE + f'/inhabitants/{name}/move_start.png', 1, 5)
        self.move = Aux.get_surface_from_sprite(
            PATH_IMAGE + f'/inhabitants/{name}/move.png', 2, 12)
        self.move_end = Aux.get_surface_from_sprite(
            PATH_IMAGE + f'/inhabitants/{name}/move_end.png', 1, 5)
        self.talk = Aux.get_surface_from_sprite(
            PATH_IMAGE + f'/inhabitants/{name}/talk.png', 4, 16)[:62]

        # imagenes
        self.frame = 0
        self.speed_frame = speed_frame
        self.animation = self.stay # qué animación se hizo última - toma un array
        self.flip_x = False
        self.flip_y = False
        self.image = pygame.transform.flip(self.animation[self.frame], self.flip_x, self.flip_y)  # tomar una imagen del array
        self.rect = self.image.get_rect()  # toma el rectangulo de esa imagen

        self.rect.x = ANCHO_VENTANA / 2 # HARDCODED
        self.rect.y = 200 # HARDCODED
        self.rect_pj = pygame.Rect(
            self.rect.x - 18, self.rect.y + 25, self.rect.width + 28, self.rect.height + 25) 
        # rect para interacciones

        # movimiento
        self.moving_x = False
        self.moving_y = False
        self.move_x = 0 
        self.move_y = 0 
        self.move_xy = ()
        self.speed_walk = 2 # no
        self.speed_run = 6 # no
        self.speed = self.speed_walk # no

        # JUMP
        self.can_jump = True # no
        self.is_jumping = False # no
        self.GRAVITY = 0.4 # no
        self.altura_salto = 20 # no
        self.y_velocity = self.altura_salto # no

    def control(self, pos_xy): # no
        # print(pos_xy)

        if self.rect.centerx > pos_xy[0]:
            self.moving_x = True
            self.moving_y = True
            # print('X: DEBO BAJAR')
            self.move_x = -5
            self.flip_x = True
            if self.rect.centery > pos_xy[1]:
                # print('Y: DEBO SUBIR')
                self.move_y = 5
            else:
                # print('Y: DEBO BAJAR')
                self.move_y = -5
        elif self.rect.centerx < pos_xy[0]:
            self.moving_x = True
            self.moving_y = True
            # print('X: DEBO SUBIR')
            self.move_x = 5
            self.flip_x = False
            if self.rect.centery > pos_xy[1]:
                # print('Y: DEBO SUBIR')
                self.move_y = 5
            else:
                # print('Y: DEBO BAJAR')
                self.move_y = -5
        self.move_xy = (pos_xy[0],pos_xy[1])
        self.frame = 0


    def colicion(self, obj=''):
        if pygame.Rect.colliderect(self.rect_pj, obj):
            self.talking = True
            self.animation = self.talk
        else:
            self.talking = False
            

    def update(self):
        """ if not self.talking:
            self.animation = self.stay """
        # print(self.move_xy)
        # print(self.moving)

        # relentizar fotogramas de pj (lower than game fps (60))
        self.frame += self.speed_frame
        if self.frame >= len(self.animation):
            self.frame = 0
            self.animation = self.stay
            self.talking = False

            
        # if (self.move_x and self.move_y) and self.moving:
        if self.move_xy and (self.moving_x or self.moving_y):
            self.animation = self.move

            if self.moving_x:
                self.rect.centerx += self.move_x
                self.rect_pj.centerx += self.move_x
            if self.moving_y:
                self.rect.centery -= self.move_y
                self.rect_pj.centery -= self.move_y


            if (self.move_x > 0 and self.rect.centerx >= self.move_xy[0]) or (self.move_x < 0 and self.rect.centerx <= self.move_xy[0]):
            # if (self.move_x > 0 and self.rect.centerx >= self.move_xy[0]):
                self.move_x = 0
                self.moving_x = False
            """ elif self.move_x < 0 and self.rect.centerx >= self.move_xy[0]:
                self.move_x = 0
                self.moving_x = False """
                
            # if self.move_y > 0 and self.rect.centery <= self.move_xy[1]:
            if (self.move_y > 0 and self.rect.centery <= self.move_xy[1]) or (self.move_y < 0 and self.rect.centery >= self.move_xy[1]):
                self.move_y = 0
                self.moving_y = False
            """ elif self.move_y < 0 and self.rect.centery >= self.move_xy[1]:
                self.move_y = 0
                self.moving_y = False """
            """ if self.rect.centerx >= self.move_xy[0]:
                self.move_x = 0
                self.moving_x = False
                # self.animation = self.stay
            if self.rect.centery == self.move_xy[1]:
                self.move_y = 0
                self.moving_y = False """
            if(not self.moving_x and not self.moving_y):
                self.animation = self.stay

            # if self.rect.y == self.move_xy[1]:
            #     self.rect.y = 0


        # self.rect.x += self.move_x

    def draw(self, surface):
        # print(int(self.frame))
        self.image = pygame.transform.flip(self.animation[int(self.frame)], self.flip_x, False)
        surface.blit(self.image, self.rect)
