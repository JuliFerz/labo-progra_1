import pygame
from constantes import *
from widget_gui import Widget
from button_gui import Button


class Form():
    form_dict = {}
    # saber si formulario esta activo
    # saber si formulario esta visible (o ejecutando)
    def __init__(self, name, main_surface, x, y, w, h, color_background, color_border, active,):
        self.form_dict[name] = self
        self.main_surface = main_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border

        self.surface = pygame.Surface((w, h))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active

        self.main_surface.fill('black')
        self.surface.fill(self.color_background)

    def update_active_forms(self, name):
        for form in self.form_dict.values():
            form.active = False
        self.form_dict[name].active = True

    # media
    def render(self):
        pass

    def draw(self):
        self.main_surface.blit(self.surface, self.slave_rect)

    def update(self, event_list):
        pass


class MenuForm(Form):
    def __init__(self, main_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(main_surface, x, y, w, h, color_background, color_border, active)

        self.boton1 = Button(
            master=self,
            x=100,
            y=50,
            w=200,
            h=50,
            color_background=RED,
            color_border=GREEN,
            on_click=self.on_click,
            on_click_param='Botón 1',
            text='Menu',
            font='Verdana',
            font_size=30,
            font_color=BLUE)
        self.boton2 = Button(
            master=self,
            x=200,
            y=50,
            w=200,
            h=50,
            color_background=RED,
            color_border=GREEN,
            on_click=self.on_click,
            on_click_param='Botón 2',
            text='Menu2',
            font='Verdana',
            font_size=30,
            font_color=BLUE)
        # Revisar si hacer lista de widgets (con todosl os botones, barras de estado, etc)
        self.widget_list = [self.boton1, self.boton2]

    # boton1 = Button(screen, 10, 10)
    def on_click(self, param):
        print('Click en', param)

    # media
    def render(self):
        pass

    def update(self, event_list):
        for button in self.widget_list:
            button.update(event_list)

    def draw(self):
        super().draw()
        for button in self.widget_list:
            button.draw()
