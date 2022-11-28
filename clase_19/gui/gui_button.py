import pygame
from constantes import *
from gui_widget import Widget


class Button(Widget):
    # colocar image en vez de color
    # onclick llama a la función que quiero que me llame al hacer click
    # onclick_param envia un parametro a la función on click
    # si el texto de los botones son dinamicos (puede cambiar el texto durante el juego), hacer un método para que pueda actulizarse
    # calcular de forma óptima las coordenadas del texto en el recuadro del botón (que esté centrado el texto en el botón)
    def __init__(self, main_surface, main_rect, x, y, w, h, color_background, color_border, on_click, on_click_param, text, font, font_size, font_color):
        super().__init__(main_surface, main_rect, x, y, w, h, color_background, color_border)
        pygame.font.init()

        # pasar a general?
        # form surface (screen -> form_surface -> [button_surface])
        self.main_surface = main_surface
        self.main_rect = main_rect

        # fn buttons
        self.on_click = on_click
        self.on_click_param = on_click_param

        # txt
        self._text = text
        self.font = pygame.font.Font(font, font_size)
        # self.font_sys = pygame.font.SysFont(self.font, font_size)
        self.font_color = font_color

    def click_collition(self, mouse_xy):
        # colisionar SOLO con botones que estén dentro del segundo form
        if self.slave_widget_rect_collide.collidepoint(mouse_xy) and \
            self.main_rect.collidepoint(mouse_xy):
            self.on_click(self.on_click_param)

    def get_mouse_click(self, event_list):
        # print(pygame.mouse.get_pos())
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            # if event.type == pygame.MOUSEBUTTONDOWN:
                self.click_collition(event.pos)
            

    def render(self):
        self.text_render = self.font.render(self._text, True, self.font_color, self.color_background)
        self.slave_widget_surface.fill(self.color_background)
        self.slave_widget_surface.blit(self.text_render, (15,self.slave_widget_rect_collide.h/4))
        # self.slave_widget_surface.blit(self.text_render, (1,10))
    
    def update(self, event_list):
        self.get_mouse_click(event_list)
    
    def draw(self):
        super().draw()
        self.render()

        """  pygame.font.init()
        self.on_click = on_click
        self.on_click_param = on_click_param

        self._text = text
        self.font_sys = pygame.font.SysFont(font, font_size)
        self.font_color = font_color

    # media
    def render(self):
        self.slave_surface = pygame.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x  
        self.slave_rect.y = self.y

        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y

        # nuevo atributo para renderizar el texto
        self.image_text = self.font_sys.render(self._text, True, self.font_color, self.color_background)  # 1

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
        self.render() """
