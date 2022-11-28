import pygame
from constantes import *
from form_gui import Form
from button_gui import Button

class MenuForm_A(Form):
    def __init__(self, name, main_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active)

        self.boton1 = Button(
            master=self,
            x=100,
            y=50,
            w=200,
            h=50,
            color_background=RED,
            color_border=GREEN,
            on_click=self.on_click,
            on_click_param='MenuForm_B',
            text='Menu',
            font='Verdana',
            font_size=30,
            font_color=BLUE)
        # self.boton2 = Button(
        #     master=self,
        #     x=200,
        #     y=50,
        #     w=200,
        #     h=50,
        #     color_background=RED,
        #     color_border=GREEN,
        #     on_click=self.on_click,
        #     on_click_param='Botón 2',
        #     text='Menu2',
        #     font='Verdana',
        #     font_size=30,
        #     font_color=BLUE)
        # Revisar si hacer lista de widgets (con todosl os botones, barras de estado, etc)
        # self.widget_list = [self.boton1, self.boton2]
        self.widget_list = [self.boton1]

    # boton1 = Button(screen, 10, 10)
    def on_click(self, param):
        self.update_active_forms(param)

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
