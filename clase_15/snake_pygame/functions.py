import pygame as py
import random
# from main import SCREEN_HEIGHT, SCREEN_WIDTH
import src as img
import colores as color
import apple as apl
import snake as sn

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
INCR_SCORE = 100


def random_gen():
    r_posX = random.randrange(0, SCREEN_WIDTH - 40, 40)
    r_posY = random.randrange(0, SCREEN_HEIGHT - 40, 40)
    return [r_posX, r_posY]


def draw_mov(pj, x, y):
    temp_x = pj['rect'].x + x
    temp_y = pj['rect'].y + y
    if (temp_x >= 0 and temp_x < 600) and \
            (temp_y >= 0 and temp_y < 600):
        pj['rect'].x += x
        pj['rect'].y += y
    else:
        print('Me re mori 🐍💀')
        pj['in_game'] = False


def update_mov(obj, img, surface):
    img = img or 'img'
    surface.blit(obj[img], obj['rect'])


def collision_obj(snake, apple):
    if snake['rect'].colliderect(apple['rect']):
        print('Me comí alta 🍎')
        snake['tails'] += 1
        # snake['score'] += INCR_SCORE
        # print(snake['score'])
        r_posX = random_gen()[0]
        r_posY = random_gen()[1]
        apple = apl.create_apple(r_posX, r_posY)
    return apple
