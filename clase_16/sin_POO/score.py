import pygame as py
from constantes import *
import tablero
import tarjeta


def init(id, font, txt, x, y):
    d_score = {}
    # d_score['path_imagen'] = PATH_RECURSOS+path_imagen
    d_score['id'] = id
    d_score['surface'] = font.render(txt, True, NEGRO)
    d_score['value'] = 0
    d_score['rect'] = d_score['surface'].get_rect()
    d_score['rect'].x = x
    d_score['rect'].y = y
    return d_score


def CrearScore():
    temp_list = []
    txt_font = py.font.SysFont('Arial Narrow', 50)
    temp_list.append(init('time', txt_font, f'Tiempo: ', 0, ALTO_PANTALLA-ALTO_BOTON))
    # temp_list.append(init('score', txt_font, f'Score: ', 0, ALTO_PANTALLA-ALTO_BOTON+50))
    # temp_list.append(init('max_score', txt_font, f'Max score: ', ANCHO_BOTON+10, ALTO_PANTALLA-ALTO_BOTON+50))
    return temp_list


def actualizar_texto(tablero, txt, value):
    l_score = tablero['score']
    txt_font = py.font.SysFont('Arial Narrow', 50)
    l_score[0]['surface'] = txt_font.render(f'{txt}: {value}', True, NEGRO)
