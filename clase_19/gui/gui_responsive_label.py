import pygame
from gui.constantes import * # REVISAR
from gui.gui_widget import Widget


class ResponsiveLabel(Widget):
    def __init__(self, main_surface, main_rect, x, y, w, h, color_background, color_border, text, value, text_pos, font, font_size, font_color):
        super().__init__(main_surface, main_rect, x, y, w, h, color_background, color_border)
        pygame.font.init()
        
        # form surface (screen -> form_surface -> [button_surface])
        self.main_surface = main_surface
        self.main_rect = main_rect

        # image
        # self.image = pygame.image.load(
        #     'D:/Users/julian/Documents/Julian/UTN/1. Primer cuatrimestre/labo-progra_1/clase_19/src/images/gui/jungle/load_bar/2.png'
        # )
        # self.rect_img = self.image.get_rect()
        # self.rect_img.x, self.rect_img.y = self.slave_widget_rect_collide.x, self.slave_widget_rect_collide.y
        # self.rect_img.w, self.rect_img.h = self.slave_widget_rect_collide.w/2, self.slave_widget_rect_collide.h

        # txt
        self.value = value
        self._text = text
        self.text_pos = self.get_text_pos(text_pos)
        self.font = pygame.font.Font(font, font_size)
        self.font_color = font_color

        if self.color_background:
            self.text_render = self.font.render(self._text, True, self.font_color, self.color_background)
        else:
            self.text_render = self.font.render(self._text, True, self.font_color)

    

    def render(self):
        if self.color_background:
            self.slave_widget_surface.fill(self.color_background)
        # else:
            # self.slave_widget_surface.fill(self.color_border)
            # self.slave_widget_surface.blit(self.image, self.rect_img)
        try:
            self.slave_widget_surface.blit(self.text_render, self.text_pos)
        except:
            print('rompi 💀', self.text_pos, self._text)


    def update(self, value):
        self.text_render = self.font.render(f'{self._text}{value}', True, self.font_color)

    
    def draw(self):
        # super().draw()
        self.main_surface.blit(
            self.slave_widget_surface,
            self.slave_widget_rect_collide)
        self.render()
