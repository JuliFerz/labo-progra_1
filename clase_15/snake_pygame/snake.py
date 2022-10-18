import pygame as py
import src as img
import colores as color


RES_IMG = (40, 40)


def resize_img(img: str):
    return py.transform.scale(img, RES_IMG)


def create_snake(x: int, y: int) -> dict:
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
        # 'tails': 1,
        'size': 2,
        'score': 0
    }
    return dict_sn


def generate_tail(snake, tails):
    pass
