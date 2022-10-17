import pygame as py
import src as img
import colores as color


""" 
def rect_snake(surface, x, y):

    dict_pj = {}
    dict_pj['surface'] = py.draw.rect(surface, color.VERDE, (x, y, 25, 25))
    dict_pj['rect_pos'] = py.Rect(x, y, 25, 25)
    dict_pj['score'] = 0
    return dict_pj

RES_IMG = (25, 25)
"""
RES_IMG = (40, 40)


def resize_img(img: str):
    return py.transform.scale(img, RES_IMG)


def create_snake(x: int, y: int) -> dict:
    # dict_sn = {}
    dict_sn = {
        'UP_HEAD': resize_img(py.image.load(img.UP_HEAD)),
        'DW_HEAD': resize_img(py.image.load(img.DW_HEAD)),
        'L_HEAD': resize_img(py.image.load(img.L_HEAD)),
        'R_HEAD': resize_img(py.image.load(img.R_HEAD)),
        'UP_TAIL': resize_img(py.image.load(img.UP_TAIL)),
        'DW_TAIL': resize_img(py.image.load(img.DW_TAIL)),
        'L_TAIL': resize_img(py.image.load(img.L_TAIL)),
        'R_TAIL': resize_img(py.image.load(img.R_TAIL)),
        'ROTATE_UL': resize_img(py.image.load(img.ROTATE_UL)),
        'ROTATE_UR': resize_img(py.image.load(img.ROTATE_UR)),
        'ROTATE_DL': resize_img(py.image.load(img.ROTATE_DL)),
        'ROTATE_DR': resize_img(py.image.load(img.ROTATE_DR)),
        'rect': py.Rect(x, y, RES_IMG[0], RES_IMG[1]),
        'in_game': True,
        'tails': 1,
        'score': 0
    }
    """ dict_sn['UP_HEAD'] = resize_img(py.image.load(img.UP_HEAD))
    dict_sn['DW_HEAD'] = resize_img(py.image.load(img.DW_HEAD))
    dict_sn['L_HEAD'] = resize_img(py.image.load(img.L_HEAD))
    dict_sn['R_HEAD'] = resize_img(py.image.load(img.R_HEAD))
    dict_sn['UP_TAIL'] = resize_img(py.image.load(img.UP_TAIL))
    dict_sn['DW_TAIL'] = resize_img(py.image.load(img.DW_TAIL))
    dict_sn['L_TAIL'] = resize_img(py.image.load(img.L_TAIL))
    dict_sn['R_TAIL'] = resize_img(py.image.load(img.R_TAIL))
    dict_sn['ROTATE_UL'] = resize_img(py.image.load(img.ROTATE_UL))
    dict_sn['ROTATE_UR'] = resize_img(py.image.load(img.ROTATE_UR))
    dict_sn['ROTATE_DL'] = resize_img(py.image.load(img.ROTATE_DL))
    dict_sn['ROTATE_DR'] = resize_img(py.image.load(img.ROTATE_DR))
    dict_sn['rect'] = py.Rect(x, y, RES_IMG[0], RES_IMG[1])
    dict_sn['in_game'] = True
    dict_sn['qty_tail'] = 0
    dict_sn['score'] = 0 """
    return dict_sn


def generate_tail(snake, tails):

    pass
