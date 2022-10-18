import pygame as py
import random
import src
import colores as color
import apple as apl
import snake as sn
import music

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
INCR_SCORE = 100


def txt_render(font, var, color):
    return font.render(f'Score: {var}', True, color)


def txt_update(surface, txt, x, y):
    return surface.blit(txt, (x, y))


def play_music(music: str):
    py.mixer.music.set_volume(0.7)
    return music.play()


def random_gen() -> list:
    r_posX = random.randrange(0, SCREEN_WIDTH - 40, 40)
    r_posY = random.randrange(0, SCREEN_HEIGHT - 40, 40)
    return [r_posX, r_posY]


def draw_mov(pj: dict, x: int, y: int):
    temp_x = pj['rect'].x + x
    temp_y = pj['rect'].y + y
    if (temp_x >= 0 and temp_x < 600) and \
            (temp_y >= 0 and temp_y < 600):
        pj['rect'].x += x
        pj['rect'].y += y
    else:
        print('Me re mori 🐍💀')
        py.mixer.stop()
        play_music(music.punch)
        pj['in_game'] = False


def update_mov(obj: dict, img: str, surface: py.surface):
    img = img or 'img'
    surface.blit(obj[img], obj['rect'])


def collision_obj(snake: dict, apple: dict) -> dict:
    if snake['rect'].colliderect(apple['rect']):
        play_music(music.crunchy)
        print('Me comí alta 🍎')
        # snake['tails'] += 1
        snake['score'] += INCR_SCORE
        r_posX = random_gen()[0]
        r_posY = random_gen()[1]
        apple = apl.create_apple(r_posX, r_posY)
    return apple
