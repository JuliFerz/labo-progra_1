import pygame as py
from constantes import *
import tablero
import tarjeta


def init(path_imagen, x, y):
    d_btn = {}
    d_btn['path_imagen'] = PATH_RECURSOS+path_imagen
    d_btn['surface'] = py.transform.scale(py.image.load(
        d_btn['path_imagen']), (ANCHO_BOTON, ALTO_BOTON))
    d_btn['rect'] = d_btn['surface'].get_rect()
    d_btn['rect'].x = x
    d_btn['rect'].y = y
    return d_btn


# def CrearBTN(cant, d_tablero):
def CrearBTN():
    lista_btn = []
    lista_btn.append(init('/start.png', ANCHO_PANTALLA - ANCHO_BOTON, ALTO_PANTALLA - ALTO_BOTON))
    lista_btn.append(init('/restart.png', ANCHO_PANTALLA - ANCHO_BOTON-ANCHO_BOTON, ALTO_PANTALLA - ALTO_BOTON))
    return lista_btn


# CrearBTN(1)
