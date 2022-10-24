import pygame
import score
import math
import random
from functools import reduce

# from clase_16.constantes import PATH_RECURSOS
from constantes import *


def init(nombre_imagen,nombre_imagen_hide, x, y):
    # agregar ID de tarjeta - se usa path_imagen
    nueva_tarjeta = {}
    nueva_tarjeta["visible"] = True
    nueva_tarjeta["descubierto"] = False
    nueva_tarjeta["path_imagen"] = PATH_RECURSOS+nombre_imagen
    nueva_tarjeta["surface"] = pygame.transform.scale(pygame.image.load(nueva_tarjeta["path_imagen"]), (ANCHO_TARJETA, ALTO_TARJETA))
    nueva_tarjeta["surface_hide"] = pygame.transform.scale(pygame.image.load(PATH_RECURSOS+nombre_imagen_hide), (ANCHO_TARJETA, ALTO_TARJETA))
    nueva_tarjeta["rect"] = nueva_tarjeta["surface"].get_rect()
    nueva_tarjeta["rect"].x = x
    nueva_tarjeta["rect"].y = y
    return nueva_tarjeta


def cant_tarjetas_descubiertas(lista_tarjetas):
    cantidad = 0
    for tarjeta in lista_tarjetas:
        if tarjeta["descubierto"]:
            cantidad += 1
    return cantidad


def cant_tarjetas_visibles_no_descubiertas(lista_tarjetas):
    cantidad = 0
    # print(cantidad)
    for tarjeta in lista_tarjetas:
        if tarjeta["visible"] and not tarjeta["descubierto"]:
            cantidad += 1
    return cantidad


def match(tablero):
    aux_primer_tarjeta = ''
    aux_segunda_tarjeta = ''
    lista_tarjetas = tablero['l_tarjetas']
    if cant_tarjetas_visibles_no_descubiertas(lista_tarjetas) == 2:

        for i in range(len(lista_tarjetas)):
            if lista_tarjetas[i]['visible'] and not lista_tarjetas[i]['descubierto']:
                aux_primer_tarjeta = lista_tarjetas[i]

                for j in range(i + 1, len(lista_tarjetas)):
                    if lista_tarjetas[j]['visible'] and not lista_tarjetas[j]['descubierto']:

                        aux_segunda_tarjeta = lista_tarjetas[j]
                        if (aux_primer_tarjeta['path_imagen'] == aux_segunda_tarjeta['path_imagen']):

                            aux_primer_tarjeta['descubierto'] = True
                            aux_segunda_tarjeta['descubierto'] = True
                            

