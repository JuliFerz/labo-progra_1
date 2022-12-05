import pygame, sys
from gui.constantes import * # REVISAR
from gui.gui_button import Button
from gui.form_gui import Form
from gui.gui_label import Label
from gui.gui_widget import Widget
from gui.gui_responsive_label import ResponsiveLabel

from settings import get_levels


class HudLife(Widget):
    def __init__(self, main_surface, main_rect, x, y, w, h, color_background, color_border, max_life, value):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.color_background = color_background
        self.color_border = color_border

        # form surface (screen -> form_surface -> [button_surface])
        self.main_surface = main_surface
        self.main_rect = main_rect

        # slave
        self.slave_surface = pygame.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect(center=(self.x, self.y))
        self.slave_rect_collide = self.slave_surface.get_rect(
            center=(
                self.x + self.main_rect.x,
                self.y + self.main_rect.y
            ))

        # image
        self.bg_image = pygame.image.load(
            f'{PATH_IMAGE}/gui/jungle/load_bar/bg.png'
        )
        self.bg_image = pygame.transform.scale(self.bg_image,(self.w, self.h))

        # rect
        self.rect_bg_img = self.bg_image.get_rect()
        self.rect_bg_img.x, self.rect_bg_img.y = self.slave_rect_collide.x, self.slave_rect_collide.y
        self.rect_bg_img.w, self.rect_bg_img.h = self.slave_rect_collide.w, self.slave_rect_collide.h
        # self.rect_bg_img.w, self.rect_bg_img.h = self.slave_rect_collide.w/2, self.slave_rect_collide.h

        # image
        self.image = pygame.image.load(
            f'{PATH_IMAGE}/gui/jungle/load_bar/2.png'
        )
        self.image = pygame.transform.scale(self.image,(self.w-5, self.h-5))

        # rect
        self.rect_img = self.image.get_rect()
        self.rect_img.x, self.rect_img.y = self.slave_rect_collide.x+4, self.slave_rect_collide.y+4
        self.rect_img.w, self.rect_img.h = self.slave_rect_collide.w, self.slave_rect_collide.h
        # self.rect_img.w, self.rect_img.h = self.slave_rect_collide.w/2, self.slave_rect_collide.h

        # values
        self.max_life = max_life
        self.life = value
        self.amount = self.w / self.max_life
        self.acumulate_amount = 0
        
        # print(self.max_life, self.life)


    def get_health(self, amount):
        # if not self.w + self.acumulate_amount <= self.w:
            # self.acumulate_amount += amount
        # if self.acumulate_amount == 0:
        #     self.acumulate_amount = self.max_life

        self.image = pygame.transform.scale(self.image,(
            (self.w - self.acumulate_amount) + amount, self.h-5))
        # self.acumulate_amount = (self.w - self.acumulate_amount) + amount
        # print(f'AAAA {self.w - self.acumulate_amount} + {amount}')
        # print(f'TOTAL {(self.w - self.acumulate_amount) + amount}')

    def get_damage(self):
        if self.w - self.acumulate_amount >= 0:
            self.image = pygame.transform.scale(self.image,(self.w - self.acumulate_amount, self.h-5))
            self.acumulate_amount += self.amount
            # print(f'BBBBB {self.w} - {self.acumulate_amount}')

    # def update(self, amount):
    #     # if self.w + self.acumulate_amount >= 0 and self.w + self.acumulate_amount <= self.w:
        
    #     print(f'{self.w} + {self.acumulate_amount} = {self.w + self.acumulate_amount}')
    #     if self.w + amount >= 0 and self.w + amount <= self.w:

    #         print('>>><<<<>>>',amount)
    #         self.acumulate_amount += amount
    #         self.image = pygame.transform.scale(self.image,(self.w + self.acumulate_amount, self.h-5))
    
    def draw(self):
        self.main_surface.blit(self.bg_image, self.rect_bg_img)
        self.main_surface.blit(self.image, self.rect_img)
