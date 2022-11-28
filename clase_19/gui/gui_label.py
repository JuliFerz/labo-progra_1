import pygame
from constantes import *
from gui_widget import Widget


class Label(Widget):
    # colocar image en vez de color
    # onclick llama a la función que quiero que me llame al hacer click
    # onclick_param envia un parametro a la función on click
    # si el texto de los botones son dinamicos (puede cambiar el texto durante el juego), hacer un método para que pueda actulizarse
    # calcular de forma óptima las coordenadas del texto en el recuadro del botón (que esté centrado el texto en el botón)
    def __init__(self, main_surface, main_rect, x, y, w, h, color_background, text, font, font_size, font_color):
        super().__init__(main_surface, main_rect, x, y, w, h, color_background)
        pygame.font.init()

        # form surface (screen -> form_surface -> [button_surface])
        self.main_surface = main_surface
        self.main_rect = main_rect

        # txt
        self._text = text
        self.font = pygame.font.Font(font, font_size)
        # self.font_sys = pygame.font.SysFont(self.font, font_size)
        self.font_color = font_color
            

    def render(self):
        self.text_render = self.font.render(self._text, True, self.font_color, self.color_background)
        self.slave_widget_surface.fill(self.color_background)
        self.slave_widget_surface.blit(self.text_render, (self.slave_widget_rect_collide.x/4, self.slave_widget_rect_collide.h/4))
        # self.slave_widget_surface.blit(self.text_render, (1,10))
    
    def draw(self):
        super().draw()
        self.render()
