import pygame as py
import random
import snake as sn
import apple as apl
import functions as fn
import colores as color
import music
import src  # SACAR
# 7

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

py.init()

main_screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption('🐍 SNAKE | Pygame')


# TIMER - pos (1seg)
pos_timer = py.USEREVENT
delay = 200
py.time.set_timer(pos_timer, delay)

# SNAKE & res
_posX = 80
_posY = 0
mov_snake = 40

# AUX VAR


# texto
txt_font = py.font.SysFont('Arial Narrow', 50)  # REVISAR
# txt_score = txt_font.render(f'Score ', True, color.BLANCO)

# crear objetos
snake = sn.create_snake(_posX, _posY)
snake_img = 'R_HEAD'
print('SNAKE 🐍', snake)


r_posX = fn.random_gen()[0]
r_posY = fn.random_gen()[1]
apple = apl.create_apple(r_posX, r_posY)
print('APPLE 🍎', apple)


# set music
py.mixer.init()
fn.play_music(music.background_m)

running = True
while running:
    # background_m.play()

    for event in py.event.get():
        # QUIT game
        if event.type == py.QUIT:
            running = False

        # DIRECCION - snake
        if event.type == py.KEYDOWN and snake['in_game']:
            if event.key == py.K_LEFT:
                snake_img = 'L_HEAD'
            if event.key == py.K_RIGHT:
                snake_img = 'R_HEAD'
            if event.key == py.K_UP:
                snake_img = 'UP_HEAD'
            if event.key == py.K_DOWN:
                snake_img = 'DW_HEAD'
            if event.key == py.K_ESCAPE:
                running = False
                py.QUIT
        # REINICIO
        elif event.type == py.KEYDOWN and not snake['in_game']:
            if event.key == py.K_r:
                print('Reinicio 🔁')
                fn.play_music(music.background_m)
                snake = sn.create_snake(_posX, _posY)
                snake_img = 'R_HEAD'
                r_posX = fn.random_gen()[0]
                r_posY = fn.random_gen()[1]
                apple = apl.create_apple(r_posX, r_posY)
                snake['in_game'] = True
            # print(f'se presiono: {py.key.name(event.key)}')

        # MOVIMIENTO - snake
        if event.type == py.USEREVENT:
            if event.type == pos_timer and snake['in_game']:
                pass
                key_list = py.key.get_pressed()
                if snake_img == 'L_HEAD':
                    fn.draw_mov(snake, -mov_snake, 0)
                elif snake_img == 'R_HEAD':
                    fn.draw_mov(snake, mov_snake, 0)
                elif snake_img == 'UP_HEAD':
                    fn.draw_mov(snake, 0, -mov_snake)
                elif snake_img == 'DW_HEAD':
                    fn.draw_mov(snake, 0, mov_snake)
                else:
                    fn.draw_mov(snake, mov_snake, 0)
                    snake_img = 'R_HEAD'

    apple = fn.collision_obj(snake, apple)  # chequear si colisionó o no
    main_screen.fill(color.NEGRO)

    txt_score = fn.txt_render(txt_font, snake['score'], color.BLANCO)
    fn.txt_update(main_screen, txt_score, (SCREEN_WIDTH / 2) - 60, 0)

    fn.update_mov(apple, '', main_screen)
    fn.update_mov(snake, snake_img, main_screen)
    py.display.update()
py.quit()
