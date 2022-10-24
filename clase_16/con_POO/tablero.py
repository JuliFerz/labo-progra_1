import pygame as py
import tarjeta
import constantes as const
import boton as btn
import musica
import score
import re
import random


def init() -> dict:
    '''
    Crea un diccionario que contendrá toda la información del tablero (tarjetas, botones, score)
    No recibe parametros
    Retorna el diccionario creado
    '''
    dict_tablero = {}

    # TARJETA
    lista_tarjetas = []
    i = 1
    for x in range(0, const.ANCHO_PANTALLA, const.ANCHO_TARJETA):
        for y in range(0, const.ALTO_PANTALLA - const.ALTO_TEXTO, const.ALTO_TARJETA):
            card = tarjeta.Tarjeta(f'/0{i}.png', '/00.png', x, y)
            lista_tarjetas.append(card._initialize())
            if i < const.CANT_TOTAL_TARJETAS:
                i += 1
            else:
                i = 1
    dict_tablero['l_tarjetas'] = lista_tarjetas
    # TARJETA

    # BOTONES
    lista_btn = []
    start_btn = btn.Boton('/start.png', const.ANCHO_PANTALLA - const.ANCHO_BOTON, const.ALTO_PANTALLA - const.ALTO_BOTON)
    restart_btn = btn.Boton('/restart.png', const.ANCHO_PANTALLA - const.ANCHO_BOTON-const.ANCHO_BOTON, const.ALTO_PANTALLA - const.ALTO_BOTON)
    lista_btn.extend([start_btn._initialize()] + [restart_btn._initialize()]) # EXTEND
    dict_tablero['l_botones'] = lista_btn

    # SCORE
    txt_font = py.font.SysFont('Arial Narrow', 50)
    time_lapse = score.Score(txt_font, 'Tiempo: ', 0, const.ALTO_PANTALLA-const.ALTO_BOTON)
    dict_tablero['score'] = [time_lapse._initialize()]

    # MUSICA
    dict_tablero['background'] = musica.Music('/fondo.wav', 0.5)
    dict_tablero['win'] = musica.Music('/ganador.wav')

    dict_tablero['tiempo_tarjeta'] = 0
    dict_tablero['running'] = False
    return dict_tablero


def colicion(tablero: dict, pos_xy: tuple) -> None:
    '''
    Verifica la colición entre los clicks del mouse sobre el juego contra los rectangulos de las tarjetas y/o botones
    Recibe como parametro el tablero y una tupla (X, Y)
    '''
    fn = tarjeta.Fn(tablero)
    lista_tarjetas = fn.generate_list

    flip = musica.Music('/voltear.wav')
    if fn.get_visibles_no_descubiertas() < 2 and tablero['running']:
        for i in range(len(lista_tarjetas)):
            if lista_tarjetas[i]['rect'].collidepoint(pos_xy) and not lista_tarjetas[i]['descubierto']:
                tablero['tiempo_tarjeta'] = py.time.get_ticks()
                if not lista_tarjetas[i]['visible']:
                    flip.Play # MUSIC
                    lista_tarjetas[i]['visible'] = True
                break

    click = musica.Music('/clic.wav') # MUSIC
    for btn in tablero['l_botones']:
        if btn['rect'].collidepoint(pos_xy):
            if (re.search('/start.png', btn['path_imagen']) and not tablero['running']):
                click.Play # MUSIC
                tablero = restart_game(tablero)
                tablero['background'].PlayInLoop
                tablero['win'].Stop
                tablero['running'] = True

            elif (re.search('/restart.png', btn['path_imagen']) and tablero['running']):
                click.Play # MUSIC
                tablero = restart_game(tablero)


def update(tablero: dict):
    '''
    Una vez que comienza el juego, espera 1.5 seg desde que se toca una o dos tarjetas. Envia el tablero a match para validar si las que se han voletado son iguales, o no. Caso correcto quedaran volteadas, caso contrario volverán a su estado original
    Recibe como parametro el tablero
    '''
    tiempo_actual = py.time.get_ticks()

    fn = tarjeta.Fn(tablero)
    if((tiempo_actual >= tablero['tiempo_tarjeta'] + 600) and tablero['running']):
        time_lapse = score.Fn(tablero, 'Tiempo', int(tiempo_actual / 1000)) 
        time_lapse.update()

        lista_tarjetas = fn.generate_list
        fn.match()
        for el in lista_tarjetas:
            if not el['descubierto']:
                el['visible'] = False
    if(fn.get_descubiertas() == len(fn.generate_list) and tablero['running']):
        tablero['background'].Stop
        tablero['win'].Play
        tablero['running'] = False



def render(tablero: dict, superficie) -> None:
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero y la superficie para fundir los cambios
    '''
    # render cards
    fn_card = tarjeta.Fn(tablero, superficie)
    fn_card.draw()

    # render buttons
    fn_btn = btn.Fn(tablero, superficie)
    fn_btn.draw()

    # render time_lapse
    time_lapse = score.Fn(tablero=tablero, surface=superficie)
    time_lapse.draw()



def shuffle(tablero: dict) -> None:
    '''
    Se encarga de mezclar todos los elementos del tablero a través de sus rectángulos
    Recibe el tablero como parámetro
    '''
    fn = tarjeta.Fn(tablero)
    lista_tarjetas = fn.generate_list
    
    temp_list = []
    for card in lista_tarjetas:
        for key, value in card.items():
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
    fn = tarjeta.Fn(tablero)
    lista_tarjetas = fn.generate_list
    for el in lista_tarjetas:
        el['visible'] = False
        el['descubierto'] = False
    shuffle(tablero)
    return tablero
