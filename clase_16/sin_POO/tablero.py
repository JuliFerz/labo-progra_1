import pygame as py
import tarjeta
import constantes as const
import boton as btn
import score
import re
import math
import random


def init() -> dict:
    '''
    Crea un diccionario que contendrá toda la información del tablero (tarjetas, botones, score)
    No recibe parametros
    Retorna el diccionario creado
    '''
    lista_tarjetas = []
    dict_tablero = {}
    i = 1
    for x in range(0, const.ANCHO_PANTALLA, const.ANCHO_TARJETA):
        for y in range(0, const.ALTO_PANTALLA - const.ALTO_TEXTO, const.ALTO_TARJETA):
            lista_tarjetas.append(tarjeta.init(f'/0{i}.png', '/00.png', x, y))
            if i < const.CANT_TOTAL_TARJETAS:
                i += 1
            else:
                i = 1
    dict_tablero['l_tarjetas'] = lista_tarjetas
    dict_tablero['l_botones'] = btn.CrearBTN()
    dict_tablero['tiempo_tarjeta'] = 0
    dict_tablero['score'] = score.CrearScore()
    dict_tablero['running'] = False
    return dict_tablero


def colicion(tablero: dict, pos_xy: tuple) -> None:
    '''
    Verifica la colición entre los clicks del mouse sobre el juego contra los rectangulos de las tarjetas y/o botones
    Recibe como parametro el tablero y una tupla (X, Y)
    '''
    lista_tarjetas = tablero['l_tarjetas']
    if tarjeta.cant_tarjetas_visibles_no_descubiertas(lista_tarjetas) < 2 and tablero['running']:
        for i in range(len(lista_tarjetas)):
            if lista_tarjetas[i]['rect'].collidepoint(pos_xy) and not lista_tarjetas[i]['descubierto']:
                tablero['tiempo_tarjeta'] = py.time.get_ticks()
                if not lista_tarjetas[i]['visible']:
                    lista_tarjetas[i]['visible'] = True
                break

    for btn in tablero['l_botones']:
        if btn['rect'].collidepoint(pos_xy):
            if (re.search('/start.png', btn['path_imagen']) and not tablero['running']):
                tablero = restart_game(tablero)
                tablero['running'] = True

            elif (re.search('/restart.png', btn['path_imagen']) and tablero['running']):
                tablero = restart_game(tablero)


def update(d_tablero: dict):
    '''
    Una vez que comienza el juego, espera 1.5 seg desde que se toca una o dos tarjetas. Envia el tablero a match para validar si las que se han voletado son iguales, o no. Caso correcto quedaran volteadas, caso contrario volverán a su estado original
    Recibe como parametro el tablero
    '''
    # tiempo_actual = int(py.time.get_ticks() / 1000)
    # score.actualizar_texto(d_tablero, 'Tiempo', tiempo_actual)
    # if((tiempo_actual >= int(d_tablero['tiempo_tarjeta'] / 1000) + 1) and d_tablero['running']):
    tiempo_actual = py.time.get_ticks()
    score.actualizar_texto(d_tablero, 'Tiempo', int(tiempo_actual / 1000))
    if((tiempo_actual >= d_tablero['tiempo_tarjeta'] + 800) and d_tablero['running']):
        lista_tarjetas = d_tablero['l_tarjetas']
        tarjeta.match(d_tablero)
        for el in lista_tarjetas:
            if not el['descubierto']:
                el['visible'] = False


def render(tablero: dict, superficie) -> None:
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero y la superficie para fundir los cambios
    '''
    lista_tarjetas = tablero['l_tarjetas']
    lista_botones = tablero['l_botones']
    lista_score = tablero['score']
    for tarjeta in lista_tarjetas:
        if tarjeta['visible']:
            superficie.blit(tarjeta['surface'], tarjeta['rect'])
        else:
            superficie.blit(tarjeta['surface_hide'], tarjeta['rect'])

    for boton in lista_botones:
        superficie.blit(boton['surface'], boton['rect'])

    for score in lista_score:
        superficie.blit(score['surface'], score['rect'])


def shuffle(tablero: dict) -> None:
    '''
    Se encarga de mezclar todos los elementos del tablero a través de sus rectángulos
    Recibe el tablero como parámetro
    '''
    lista_tarjetas = tablero['l_tarjetas']
    temp_list = []
    for tarjeta in lista_tarjetas:
        for key, value in tarjeta.items():
            temp_list.append(value) if key == 'rect' else ''
    random.shuffle(temp_list)
    for i in range(len(lista_tarjetas)):
        lista_tarjetas[i].update({'rect': temp_list[i]})


def restart_game(tablero: dict) -> dict:
    '''
    Se encarga de reiniciar el juego colocando todas las tarjetas no visibles y sin descubrir
    Recibe el tablero como parámetro
    Retorna el diccionario tablero
    '''
    lista_tarjetas = tablero['l_tarjetas']
    for el in lista_tarjetas:
        el['visible'] = False
        el['descubierto'] = False
    shuffle(tablero)
    return tablero
