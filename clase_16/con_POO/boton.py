import pygame as py
from constantes import *


class Boton:
    def __init__(self, path_imagen, x, y):
        self.path_imagen = PATH_RECURSOS+path_imagen
        self.surface = py.transform.scale(py.image.load(self.path_imagen), (ANCHO_BOTON, ALTO_BOTON))
        self.x = x
        self.y = y

    def _initialize(self):
        new_obj = {
            'path_imagen': self.path_imagen,
            'surface': self.surface,
            'rect': self.surface.get_rect(),
        }
        new_obj['rect'].x = self.x
        new_obj['rect'].y = self.y
        return new_obj


class Fn:
    def __init__(self, tablero, surface=''):
        self.tablero = tablero
        self.surface = surface

    def __get_list(self):
        return self.tablero['l_botones']

    def draw(self):
        for btn in self.__get_list():
            self.surface.blit(btn['surface'], btn['rect'])
