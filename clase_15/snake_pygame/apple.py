import pygame as py
import src as img
import colores as color

RES_IMG = (40, 40)


def resize_img(img):
    return py.transform.scale(img, RES_IMG)


def create_apple(x, y):
    dict_apple = {}
    dict_apple['img'] = resize_img(py.image.load(img.APPLE))
    dict_apple['rect'] = py.Rect(x, y, RES_IMG[0], RES_IMG[1])
    dict_apple['appear'] = True
    return dict_apple
