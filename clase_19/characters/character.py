import pygame
from auxiliar import Aux
from constantes import *


class Character:
    def __init__(self,
                 manager,
                 entity,
                 c_type,
                 name,
                 animations,
                 mvm_frame_rate,
                 anim_frame_rate,
                 control_type,
                 level_tiles=[],
                 x=0,
                 y=0,
                 speed_walk=1,
                 jump_height=0,
                 damage=0.1,
                 life=50,
                 lives=1):
        self._manager = manager
        
        # Sprites
        self.type = c_type
        self.name = name
        self.get_animations(animations)

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
        self.animation = self.animations['stay']
        self.flip_x = False
        self.image = pygame.transform.flip(self.animation[self.frame], self.flip_x, False)

        # main rect
        self.rect = self.image.get_rect()

        # spawn
        self.rect.x = x
        self.rect.y = y
        # self.rect_collition.y = y

        # collide rect
        self.rect_collition = pygame.Rect(self.rect.x + (self.rect.w / 2) - (
            self.rect.w / 9), self.rect.y, (self.rect.w / 3) + 5, self.rect.h)
        self.rect_collition.centerx = self.rect.centerx

        # movement
        self.control_type = control_type
        self.speed_walk = speed_walk  # 2
        self.speed = self.speed_walk
        self.speed_run = self.speed * 3  # 6
        # JUMP
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_height = -jump_height

        self.can_jump = True
        self.is_jumping = False
        self.is_on_floor = False
        self.is_falling = False
        # self.on_ground = False
        # self.on_ceiling = False
        # self.on_left = False
        # self.on_right = False

        # others
        self.damage = damage  # particular
        self.life = life  # particular
        self.lives = lives  # particular
        self.exp = 0 # json

        self.bullet_group = []
        self.can_shoot = True
        self.qty_bullets = 1000000

    def get_animations(self, animations: list):
        self.animations = {}
        for anim in animations:
            if not anim.get("custom_cut_w"):
                anim["custom_cut_w"] = 0
            if not anim.get("step"):
                anim["step"] = 1

            self.animations.update(
                {anim['action']: Aux.get_surface_from_sprite(PATH_IMAGE + f'/{self.type}/players/{self.name}/{anim["fileName"]}', anim["rows"], anim["columns"], anim["custom_cut_w"], anim["step"])[anim["f_from"]:anim["f_to"]]})
        return self.animations

    def control(self):
        list_keys = pygame.key.get_pressed()
        mouse_key_pressed = pygame.mouse.get_pressed()

        if self.control_type == 'A':
            # REVISAR - Pasar a otro objeto
            ## X MOVEMENT ##
            if list_keys[pygame.K_d] and not list_keys[pygame.K_a]:
                self.do_walk(False)
            elif list_keys[pygame.K_a] and not list_keys[pygame.K_d]:
                self.do_walk(True)
            elif list_keys[pygame.K_d] and list_keys[pygame.K_a]:
                self.direction.x = 0
            # elif list_keys[pygame.K_w]:
                # self.do_climb()
            else:
                self.direction.x = 0
            if list_keys[pygame.K_LSHIFT]:
                self.do_sprint()
            else:
                self.speed = self.speed_walk

            ## Y MOVEMENT ##
            if list_keys[pygame.K_w] and (self.is_on_floor or self.can_jump):
                self.do_jump()
            
            ## ACTIONS ##
            if (list_keys[pygame.K_j]) and self.can_shoot:
            # if list_keys[pygame.K_j]:
                self.do_shoot()
            # elif mouse_key_pressed[0] and self.can_shoot:
                # self.do_shoot(pygame.mouse.get_pos())

            elif (not list_keys[pygame.K_j] and not mouse_key_pressed[0]) and not self.can_shoot:
                self.can_shoot = True

        if self.control_type == 'B':
            ## X MOVEMENT ##
            if list_keys[pygame.K_RIGHT] and not list_keys[pygame.K_LEFT]:
                self.do_walk(False)
            elif list_keys[pygame.K_LEFT] and not list_keys[pygame.K_RIGHT]:
                self.do_walk(True)
            elif list_keys[pygame.K_RIGHT] and list_keys[pygame.K_LEFT]:
                self.direction.x = 0
            # elif list_keys[pygame.K_w]:
                # self.do_climb()
            else:
                self.direction.x = 0
            if list_keys[pygame.K_RCTRL]:
                self.do_sprint()
            else:
                self.speed = self.speed_walk

            ## Y MOVEMENT ##
            if list_keys[pygame.K_UP] and (self.is_on_floor or self.can_jump):
                # if list_keys[pygame.K_SPACE]:
                self.do_jump()

             ## ACTIONS ##
            if list_keys[pygame.K_m] and self.can_shoot:
            # if list_keys[pygame.K_m]:
                self.do_shoot()
            elif not list_keys[pygame.K_m] and not self.can_shoot:
                self.can_shoot = True

    def do_shoot(self, mouse_xy=''):
        if self.qty_bullets > 0:
            self.can_shoot = False
            self.qty_bullets -= 1

            self._manager.shoot(self.entity, self.rect_collition.center, self.flip_x)

    def do_walk(self, flip=False):
        if flip:
            self.direction.x = -1
        else:
            self.direction.x = 1
        self.flip_x = flip

    def do_jump(self):
        self.direction.y = self.jump_height
        self.is_jumping = True
        self.is_on_floor = False
        self.can_jump = False

    def do_sprint(self):
        self.speed = self.speed_run

    def do_climb(self):
        pass

    def move_rect_x(self):
        self.rect.x += self.direction.x * self.speed
        self.rect_collition.x += self.direction.x * self.speed

    def move_rect_y(self):
        self.rect.y += self.direction.y
        self.rect_collition.y += self.direction.y
        self.apply_gravity()

    def apply_gravity(self):
        self.direction.y += GRAVITY
        if self.direction.y > GRAVITY + 2:
            self.is_falling = True
            self.is_on_floor = False

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

    def vertical_collide(self):
        self.move_rect_y()
        for tile in self.level_tiles:
            if tile.rect_collition.colliderect(self.rect_collition):
                self.is_jumping = False
                if self.direction.y > 0:  # top - on floor
                    self.rect_collition.bottom = tile.rect_collition.top
                    self.rect.centery = self.rect_collition.centery
                    # self.direction.y = 0
                    self.is_on_floor = True
                    self.can_jump = True
                    self.is_falling = False
                if self.direction.y < 0:  # bottom - on ceiling
                    self.rect_collition.top = tile.rect_collition.bottom
                    self.rect.centery = self.rect_collition.centery
                    # self.direction.y = 0
                    self.is_falling = True
                self.direction.y = 0

    def get_animation(self, delta_ms):
        if self.direction.y < 0 and self.is_jumping or self.is_falling:
            self.animation = self.animations['jump']
        elif self.direction.y > 1.6 and self.is_jumping or self.is_falling:
            self.animation = self.animations['jump']
        else:
            if self.is_on_floor:
                if self.direction.x != 0:
                    self.animation = self.animations['walk']  # walk
                    self.check_frame_index()
                else:
                    self.animation = self.animations['stay']  # stay
                    self.check_frame_index()
        self.upd_animation(delta_ms)

    def upd_animation(self, delta_ms):
        self.frame_sum_anim += delta_ms
        if self.frame_sum_anim >= self.anim_frame_rate:
            self.frame_sum_anim = 0

            self.frame += 1
            self.check_frame_index()

    def check_frame_index(self):
        if self.frame + 1 >= len(self.animation):
            self.frame = 0

    def update(self, delta_ms):
        # print(self.rect.center)
        self.frame_sum_mov += delta_ms
        if self.frame_sum_mov >= self.mvm_frame_rate:
            self.frame_sum_mov = 0

            # movement
            self.control()
            self.vertical_collide()
            self.horizontal_collide()
            # self._manager.horizontal_collide_enemy()
            # self._manager.vertical_collide_enemy()

            # animation
            self.get_animation(delta_ms)
            self.upd_animation(delta_ms)

    def draw(self, surface):
        if DEBUG:
            pygame.draw.rect(surface, RED, self.rect)
            pygame.draw.rect(surface, BLUE, self.rect_collition)
        self.image = pygame.transform.flip(self.animation[self.frame], self.flip_x, False)

        surface.blit(self.image, self.rect)