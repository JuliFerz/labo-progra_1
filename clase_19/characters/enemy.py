import pygame
import random
from auxiliar import Aux
from constantes import *


class Enemy:
    def __init__(self,
                 manager,
                 entity,
                 c_type,
                 name,
                 animations,
                 separate_files,
                 mvm_frame_rate,
                 anim_frame_rate,
                 level_tiles=[],
                 x=0,
                 y=0,
                 speed_walk=1,
                 damage=0.1,
                 life=50,
                 lives=1):
        self._manager = manager
         
        # LISTAS - Sprites
        self.type = c_type
        self.name = name
        self.separate_files = separate_files
        self.get_animations(animations)

        # platforms
        self.level_tiles = level_tiles
        self.entity = entity 

        # fps
        self.frame = 0
        self.frame_sum_mov = 0
        self.frame_sum_anim = 0
        self.mvm_frame_rate = mvm_frame_rate
        self.anim_frame_rate = anim_frame_rate

        # media
        self.animation = self.animations['stay']
        self.flip_x = False
        self.flip_y = False
        self.image = pygame.transform.flip(self.animation[self.frame], self.flip_x, self.flip_y)
        
        # main rect
        self.rect = self.image.get_rect()

        # spawn
        self.rect.x = x
        self.rect.bottom = y

        # collide rect
        self.rect_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.rect_detect = pygame.Rect(self.rect.x - (self.rect.w/2), self.rect.y - (self.rect.h/4), self.rect.width + (self.rect.w * 3), self.rect.height - (self.rect.h/3))

        # movement
        self.move_x = 0
        self.speed_walk = speed_walk
        self.speed = self.speed_walk
        self.speed_run = self.speed * 2 # REVISAR - json
        self.direction = pygame.math.Vector2(0, 0)
        self.random_x = random.randrange(0, ANCHO_VENTANA - self.rect_collition.w)
        self.walking = False

        # time & others
        self.cooldown = 1000
        self.time_enemy = pygame.time.get_ticks()

        # gravity
        self.is_falling = False
        self.is_collide_x = False

        # others
        self.damage = damage
        self.life = life
        self.lives = lives
        self.in_vision_pj = False
        self.collide_pj = False

    def get_animations(self, animations: list):
        self.animations = {}
        for anim in animations:
            if not anim.get("custom_cut_w"):
                anim["custom_cut_w"] = 0
            if not anim.get("step"):
                anim["step"] = 1

            if self.separate_files:
                self.animations.update(
                    {anim['action']: Aux.get_surface_from_files(
                        PATH_IMAGE + f'/{self.type}/enemies/{self.name}/{anim["fileName"]}/',
                        anim["fileName"],
                        anim["qty_images"],
                        w=100,
                        h=110)
                        [anim["f_from"]:anim["f_to"]]})
        return self.animations

    def move_rect_x(self):
        if not self.collide_pj:
            self.rect.x += self.direction.x
            self.rect_collition.x += self.direction.x
            self.rect_detect.x += self.direction.x
        if self.flip_x:
            ## L ##
            self.rect_detect.x = self.rect.x - ((self.rect.w * 3) - self.rect.w/2)
        else:
            ## R ##
            self.rect_detect.x = self.rect.x - (self.rect.w/2)
        self.rect_detect.y = self.rect.y - (self.rect.h/4)

    def move_rect_y(self):
        self.rect.y += self.direction.y
        self.rect_collition.y += self.direction.y
        # self.rect_detect.y += self.direction.y # no se pone aca porque direction.y varia mucho entre 0 a 1.5 (aprox), entonces el rect_detect se mueve mucho
        self.apply_gravity() 

    def apply_gravity(self):
        self.direction.y += GRAVITY
        if self.direction.y > GRAVITY + 2:
            self.is_falling = True
            # self.is_on_floor = False

    def do_walk(self, flip=False):
        if flip:
            if self.in_vision_pj:
                self.direction.x = -self.speed * self.speed_run
            else:
                self.direction.x = -self.speed
        else:
            if self.in_vision_pj:
                self.direction.x = self.speed * self.speed_run
            else:
                self.direction.x = self.speed
        self.flip_x = flip

    def auto_movement(self, x_from=0, x_to=ANCHO_VENTANA):
        self.walking = True
        if x_to == ANCHO_VENTANA: x_to = ANCHO_VENTANA - self.rect.w

        if not self.in_vision_pj:
            self.random_x = random.randrange(x_from, x_to)
            self.frame = 0
            if DEBUG:
                print('AUTO_CONTROL')
                print(f'pj: {self.rect.x} random: {self.random_x}')

        if self.rect.x <= self.random_x:
            self.do_walk(False)
        elif self.rect.x > self.random_x:
            self.do_walk(True)

    def vertical_collide(self):
        self.move_rect_y()
        for tile in self.level_tiles:
            if tile.rect_collition.colliderect(self.rect_collition):
                self.is_jumping = False
                if self.direction.y > 0:  # top - on floor
                    self.rect_collition.bottom = tile.rect_collition.top
                    self.rect.centery = self.rect_collition.centery
                    self.direction.y = 0
                    # self.is_on_floor = True
                    # self.can_jump = True
                    self.is_falling = False
                if self.direction.y < 0:  # bottom - on ceiling
                    self.rect_collition.top = tile.rect_collition.bottom
                    self.rect.centery = self.rect_collition.centery
                    self.direction.y = 0
                    self.is_falling = True

    def horizontal_collide(self):
        self.move_rect_x()
        for tile in self.level_tiles:
            if tile.rect_collition.colliderect(self.rect_collition):
                if self.direction.x < 0:  # moving left
                    self.rect_collition.left = tile.rect_collition.right
                    self.rect.centerx = self.rect_collition.centerx
                if self.direction.x > 0:  # moving right
                    self.rect_collition.right = tile.rect_collition.left
                    self.rect.centerx = self.rect_collition.centerx
                self.is_collide_x = True
                self.walking = False
                if not self.in_vision_pj: self.restart_auto_movement()

    def get_animation(self, delta_ms):
        if self.direction.y > 3 or self.is_falling:
            self.animation = self.animations['jump']
        if not self.is_falling:
            if self.direction.x != 0:
                
                if self.collide_pj:
                    self.animation = self.animations['attack']
                else:
                    self.animation = self.animations['walk']
                self.check_frame_index()

            else:
                self.animation = self.animations['stay']
                self.check_frame_index()
        self.upd_animation(delta_ms)

    def check_frame_index(self):
        if self.frame + 1 >= len(self.animation):
            self.frame = 0

    def restart_auto_movement(self):
        if not self.collide_pj: self.direction.x = 0 
        self.time_enemy = pygame.time.get_ticks()
        self.cooldown = random.randrange(1000, 5000, 1000) # puedo poner saltos de a 500

    def _control(self):
        self.rect_detect.y = self.rect.y - (self.rect.h/4)

        if not self.in_vision_pj:
            ticks = pygame.time.get_ticks()
            if not self.walking and ticks > self.time_enemy + self.cooldown:
                self.is_collide_x = False
                self.auto_movement()
        else:
            self.auto_movement()

    def upd_movement(self, delta_ms):
        self.frame_sum_mov += delta_ms
        if self.frame_sum_mov >= self.mvm_frame_rate:
            self.frame_sum_mov = 0

            # rect.y
            self.vertical_collide()

            # Si esta caminando y no esta colisionando, chequear si llegue al punto
            if (self.walking and not self.is_collide_x):
                if (self.direction.x > 0 and self.rect.centerx >= self.random_x) or \
                    (self.direction.x < 0 and self.rect.centerx <= self.random_x):
                    self.walking = False
                    self.restart_auto_movement()
            
            # Si esta caminando y ve al pj, no esta colisionando con plataforma
            elif self.walking and self.in_vision_pj:
                self.is_collide_x = False

            self.horizontal_collide()
            self._manager.horizontal_collide_pj()

    def upd_animation(self, delta_ms):
        self.frame_sum_anim += delta_ms
        if self.frame_sum_anim >= self.anim_frame_rate:
            self.frame += 1
            self.frame_sum_anim = 0

        if self.frame >= len(self.animation):
            self.frame = 0

    def update(self, delta_ms):
        # movement
        self._control() # auto_movement
        self.upd_movement(delta_ms)
        # vertical_collide -> move_rect_y
        # horizontal_collide -> move_rect_x

        # animation
        self.get_animation(delta_ms)
        self.upd_animation(delta_ms)

    def draw(self, surface):
        if DEBUG:
            pygame.draw.rect(surface, RED, self.rect)
            pygame.draw.rect(surface, GREEN, self.rect_detect)
            pygame.draw.rect(surface, BLUE, self.rect_collition)
        self.image = pygame.transform.flip(self.animation[int(self.frame)], self.flip_x, False)
        
        surface.blit(self.image, self.rect)
