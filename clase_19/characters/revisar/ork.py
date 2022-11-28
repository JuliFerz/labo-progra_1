import pygame
import random
from auxiliar import Aux
from constantes import *
from enemy import Enemy

class Ork(Enemy):
    def __init__(self,
                 c_type,
                 name,
                 animations,
                 mvm_frame_rate,
                 anim_frame_rate,
                 level_tiles=[],
                 x=0,
                 y=0,
                 speed_walk=1,
                 speed_run=1, # REVISAR
                 damage=0.1,
                 life=50,
                 lives=1):
        super().__init__()
        # LISTAS - Sprites
        self.type = c_type
        self.name = name
        self.check_animations(animations)
        self.get_animation(animations)

        """  # fps
        self.frame = 0
        self.frame_sum_mov = 0
        self.frame_sum_anim = 0
        self.mvm_frame_rate = mvm_frame_rate
        self.anim_frame_rate = anim_frame_rate

        # media & rect
        self.animation = self.animations['idle']
        self.flip_x = False
        self.flip_y = False
        self.image = pygame.transform.flip(self.animation[self.frame], self.flip_x, self.flip_y)
        self.rect = self.image.get_rect()
        self.rect_collition = pygame.Rect(self.rect.x + 38, self.rect.y + 80, self.rect.width - 200, self.rect.height - 75)

        # spawn
        self.rect.x = x
        self.rect.bottom = y
        self.rect_collition.bottom = y

        # movement
        self.move_x = 0
        self.speed_walk = speed_walk
        self.speed = self.speed_walk
        self.speed_run = self.speed * self.speed_run
        self.direction = pygame.math.Vector2(0, 0)
        self.walking = False

        # time & others
        self.cooldown = 1000
        self.time_enemy = pygame.time.get_ticks()

        # others
        self.damage = damage
        self.life = life
        self.lives = lives """

    # def get_animations(self, animations: list, separate_files: bool):
    def check_animations(self, animations: list):
        self.animations = {}
        for anim in animations:
            if not anim.get("custom_cut_w"):
                anim["custom_cut_w"] = 0
            if not anim.get("step"):
                anim["step"] = 1

    # REVISAR - propio
    def get_animations(self,animations:list):
        for anim in animations:
            self.animations.update({anim['action']: Aux.get_surface_from_sprite(PATH_IMAGE + f'/{self.type}/enemies/{self.name}/{anim["fileName"]}', anim["rows"], anim["columns"], anim["custom_cut_w"], anim["step"])[anim["f_from"]:anim["f_to"]]})
        return self.animations

    def move_rect_x(self):
        self.rect.x += self.direction.x
        self.rect_collition.x += self.direction.x

    # REVISAR - para gravedad
    """ def move_rect_y(self):
        self.rect.y += self.direction.y
        self.rect_collition.y += self.direction.y
        self.apply_gravity()"""

    def do_walk(self, flip=False):
        if flip:
            self.direction.x = -self.speed
        else:
            self.direction.x = self.speed
        self.flip_x = not flip

    def auto_movement(self):
        self.random_x = random.randrange(0, ANCHO_VENTANA - self.rect_collition.w)
        self.walking = True
        self.frame = 0
        if DEBUG:
            print('AUTO_CONTROL')
            print(f'pj: {self.rect.x} random: {self.random_x}')

        if self.random_x <= self.rect.x:
            self.do_walk(True)
        elif self.random_x > self.rect.x:
            self.do_walk(False)
    
    # REVISAR - para gravedad
    """ def apply_gravity(self):
        self.direction.y += GRAVITY
        if self.direction.y > GRAVITY + 2:
            self.is_falling = True
            self.is_on_floor = False """

    # REVISAR - para gravedad
    """ def vertical_collide(self, level_tiles):
        self.move_rect_y()
        for tile in level_tiles:
            if tile.rect_collition.colliderect(self.rect_collition):
                self.is_jumping = False
                if self.direction.y > 0:  # top - on floor
                    self.rect_collition.bottom = tile.rect_collition.top
                    self.rect.centery = self.rect_collition.centery
                    self.direction.y = 0
                    self.is_on_floor = True
                    self.can_jump = True
                    self.is_falling = False
                if self.direction.y < 0:  # bottom - on ceiling
                    self.rect_collition.top = tile.rect_collition.bottom
                    self.rect.centery = self.rect_collition.centery
                    self.direction.y = 0
                    self.is_falling = True """

    def get_animation(self, delta_ms):
        if self.direction.x != 0:
            self.animation = self.animations['walk']  # walk
            self.check_frame_index()
        else:
            self.animation = self.animations['stay']  # stay
            self.check_frame_index()
        self.upd_animation(delta_ms)

    def check_frame_index(self):
        if self.frame + 1 >= len(self.animation):
            self.frame = 0

    def control(self):
        ticks = pygame.time.get_ticks()
        if not self.walking and ticks > self.time_enemy + self.cooldown:
            self.auto_movement()

    def upd_movement(self, delta_ms):
        self.frame_sum_mov += delta_ms
        if self.frame_sum_mov >= self.mvm_frame_rate:
            self.frame_sum_mov = 0

            # caminar
            if self.walking:
                self.move_rect_x()
                if self.random_x == self.rect.x:
                    self.walking = False
                    self.direction.x = 0
                    self.time_enemy = pygame.time.get_ticks()
                    self.cooldown = random.randrange(1000, 5000, 1000)


    def upd_animation(self, delta_ms):
        self.frame_sum_anim += delta_ms
        if self.frame_sum_anim >= self.anim_frame_rate:
            self.frame += 1
            self.frame_sum_anim = 0
        if self.frame >= len(self.animation):
            self.frame = 0

    def update(self, delta_ms):
        # movement
        self.control()
        self.upd_movement(delta_ms)

        # animation
        self.get_animation(delta_ms)
        self.upd_animation(delta_ms)


    def draw(self, surface):
        if DEBUG:
            # pygame.draw.rect(surface, RED, self.rect)
            pygame.draw.rect(surface, BLUE, self.rect_collition)
        self.image = pygame.transform.flip(self.animation[int(self.frame)], self.flip_x, False)
        surface.blit(self.image, self.rect)
