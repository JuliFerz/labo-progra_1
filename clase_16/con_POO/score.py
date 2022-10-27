import pygame as py
from constantes import *


class Score:
    def __init__(self, font='', txt='', x='', y='', score='', value='', superficie=''):
        if font:
            self.font = font.render(txt, True, NEGRO)
            self.x = x
            self.y = y
        self.txt = txt
        self.score = score
        self.value = value
        self.superficie = superficie

    def _initialize(self):
        new_obj = {
            'surface': self.font,
            'value': 0,
            'rect': self.font.get_rect(),
        }
        new_obj['rect'].x = self.x
        new_obj['rect'].y = self.y
        return new_obj

    def update(self):
        txt_font = py.font.SysFont('Arial Narrow', 50)
        self.score[0]['surface'] = txt_font.render(f'{self.txt}: {self.value}', True, NEGRO)

    def draw(self):
        for score in self.score:
            self.superficie.blit(score['surface'], score['rect'])
