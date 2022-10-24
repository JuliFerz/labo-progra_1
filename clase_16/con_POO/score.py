import pygame as py
from constantes import *


class Score:
    def __init__(self, font, txt, x, y):
        self.txt = txt
        self.font = font.render(txt, True, NEGRO)
        self.x = x
        self.y = y

    def _initialize(self):
        new_obj = {
            'surface': self.font,
            'value': 0,
            'rect': self.font.get_rect(),
        }
        new_obj['rect'].x = self.x
        new_obj['rect'].y = self.y
        return new_obj

class Fn:
    def __init__(self, tablero = '', txt = '', value = '', surface = ''):
        self.tablero = tablero
        self.txt = txt
        self.value = value
        self.surface = surface

    def __get_list(self):
        return self.tablero['score']

    def update(self):
        txt_font = py.font.SysFont('Arial Narrow', 50)
        self.__get_list()[0]['surface'] = txt_font.render(f'{self.txt}: {self.value}', True, NEGRO)

    def draw(self):
        for score in self.__get_list():
            self.surface.blit(score['surface'], score['rect'])
