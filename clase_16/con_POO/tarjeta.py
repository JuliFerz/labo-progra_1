import pygame as py
import re
import musica
from constantes import *


class Tarjeta:
    def __init__(self, path_img='', path_img_hide='', x='', y='', l_tarjetas='', superficie=''):
        if path_img:
            self.id = re.sub('[/.a-z]+', '', path_img)
            self.path_img = py.transform.scale(py.image.load(PATH_RECURSOS+path_img), (ANCHO_TARJETA, ALTO_TARJETA))
            self.path_img_hide = py.transform.scale(py.image.load(PATH_RECURSOS+path_img_hide), (ANCHO_TARJETA, ALTO_TARJETA))
            self.x = x
            self.y = y
        self.l_tarjetas = l_tarjetas
        self.superficie = superficie

    def _initialize(self):
        new_obj = {
            'id': self.id,
            'visible': True,
            'descubierto': False,
            'path_imagen': self.path_img,
            'surface': self.path_img,
            'surface_hide': self.path_img_hide,
            'rect': self.path_img.get_rect()
        }
        new_obj['rect'].x = self.x
        new_obj['rect'].y = self.y
        return new_obj

    def get_descubiertas(self):
        cantidad = 0
        for tarjeta in self.l_tarjetas:
            if tarjeta["descubierto"]:
                cantidad += 1
        return cantidad
    
    def get_visibles_no_descubiertas(self):
        cantidad = 0
        for tarjeta in self.l_tarjetas:
            if tarjeta["visible"] and not tarjeta["descubierto"]:
                cantidad += 1
        return cantidad
    
    def draw(self):
        for tarjeta in self.l_tarjetas:
            if tarjeta['visible']:
                self.superficie.blit(tarjeta['surface'], tarjeta['rect'])
            else:
                self.superficie.blit(tarjeta['surface_hide'], tarjeta['rect'])

    def match(self):
        aux_primer_tarjeta = ''
        aux_segunda_tarjeta = ''
        lista_tarjetas = self.l_tarjetas

        if self.get_visibles_no_descubiertas() == 2:
            check = musica.Music('/check.mp3', 0.5)
            for i in range(len(lista_tarjetas)):
                if lista_tarjetas[i]['visible'] and not lista_tarjetas[i]['descubierto']:
                    aux_primer_tarjeta = lista_tarjetas[i]

                    for j in range(i + 1, len(lista_tarjetas)):
                        if lista_tarjetas[j]['visible'] and not lista_tarjetas[j]['descubierto']:
                            aux_segunda_tarjeta = lista_tarjetas[j]

                            if (aux_primer_tarjeta['id'] == aux_segunda_tarjeta['id']):
                                check.Play # MUSIC
                                aux_primer_tarjeta['descubierto'] = True
                                aux_segunda_tarjeta['descubierto'] = True
    
