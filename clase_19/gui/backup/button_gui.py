import pygame
from constantes import *
from widget_gui import Widget


class Button(Widget):
    # colocar image en vez de color
    # onclick llama a la función que quiero que me llame al hacer click
    # onclick_param envia un parametro a la función on click
    # si el texto de los botones son dinamicos (puede cambiar el texto durante el juego), hacer un método para que pueda actulizarse
    # calcular de forma óptima las coordenadas del texto en el recuadro del botón (que esté centrado el texto en el botón)
    def __init__(self, master, x, y, w, h, color_background, color_border, on_click, on_click_param, text, font, font_size, font_color):
        super().__init__(master, x, y, w, h, color_background, color_border)
        pygame.font.init()
        self.on_click = on_click
        self.on_click_param = on_click_param

        self._text = text
        self.font_sys = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.render()

    # media
    def render(self):
        # nuevo atributo para renderizar el texto
        self.image_text = self.font_sys.render(self._text, True, self.font_color, self.color_background)  # 1
        
        self.slave_surface = pygame.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y

        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y


        self.slave_surface.fill(self.color_background)  # 3
        self.slave_surface.blit(self.image_text, (10, 10))  # 2

    def click_collition(self, mouse_xy):
        if self.slave_rect.collidepoint(mouse_xy):
            self.on_click(self.on_click_param)

    def get_mouse_click(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                self.click_collition(event.pos)

    def update(self, event_list):
        self.get_mouse_click(event_list)
        self.render()
