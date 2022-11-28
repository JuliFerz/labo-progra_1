import pygame
from constantes import *
from gui_widget import Widget
from gui_button import Button


class Form():
    dict_forms = {}
    # saber si formulario esta activo
    # saber si formulario esta visible (o ejecutando)
    def __init__(self, name, main_surface, x, y, w, h, color_background, color_border, active):
        self.dict_forms[name] = self
        # (screen -> [form_surface] -> button_surface)
        self.__main_surface = main_surface
        # self.main_surface_rect = self.__main_surface.get_rect()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        # TEST - poner imagen que se mueve

        # slave surface
        self.slave_surface = pygame.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect(topleft=(self.x, self.y))
        self.active = active
        self.slave_surface.fill(self.color_background)

    def update_view_form(self, id):
        print('Pressed:', id)
        for form in self.dict_forms.values():
            form.active = False
        self.dict_forms[id].active = True
        

    # media
    def render(self):
        pass

    def draw(self):
        self.__main_surface.fill('black')
        self.__main_surface.blit(self.slave_surface, self.slave_rect)

    def update(self, event_list):
        pass
