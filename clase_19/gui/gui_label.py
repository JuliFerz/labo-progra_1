import pygame
from gui.constantes import * # REVISAR
from gui.gui_widget import Widget


class Label(Widget):
    # colocar image en vez de color
    def __init__(self, main_surface, main_rect, x, y, w, h, color_background, text, text_pos, font, font_size, font_color, slave_background=''):
        super().__init__(main_surface, main_rect, x, y, w, h, color_background, '', slave_background)
        pygame.font.init()
        
        # form surface (screen -> form_surface -> [button_surface])
        self.main_surface = main_surface
        self.main_rect = main_rect

        # txt
        self._text = text
        self.text_pos = self.get_text_pos(text_pos)
        self.font = pygame.font.Font(font, font_size)
        self.font_color = font_color

        if self.slave_background:
            self.text_render = self.font.render(self._text, True, self.font_color)
        else:
            self.text_render = self.font.render(self._text, True, self.font_color, self.color_background)
    

    def render(self):
        if self.slave_background:
            self.slave_background.blit(self.text_render, self.text_pos)
        else:
            self.slave_widget_surface.fill(self.color_background)
            try:
                self.slave_widget_surface.blit(self.text_render, self.text_pos)
            except:
                print('rompi x.x', self.text_pos, self._text)

        # self.slave_widget_surface.fill(self.color_background)

        # REVISAR texto del label "bullets"
        # print(self.slave_widget_rect.x/4, self.slave_widget_rect.h/4)
        # self.slave_widget_surface.blit(self.text_render, (1,10))
    
    def draw(self):
        super().draw()
        self.render()
