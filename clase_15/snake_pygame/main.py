import pygame
import random
import snake as sn
import apple as apl
import functions as fn
import colores as color
import src as img  # SACAR
# 7

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

pygame.init()

main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SNAKE | Pygame')


# TIMER - pos (1seg)
pos_timer = pygame.USEREVENT
# seg_timer = 1000
pygame.time.set_timer(pos_timer, 500)

# SNAKE & res
_posX = 80
_posY = 0
mov_snake = 40

# AUX VAR
keypressed = False
# x, y, up, down
last_key = [False, False, False, False]
boost = 1


# crear objetos
snake = sn.create_snake(_posX, _posY)
snake_img = 'R_HEAD'
print('SNAKE 🐍', snake)


r_posX = fn.random_gen()[0]
r_posY = fn.random_gen()[1]
apple = apl.create_apple(r_posX, r_posY)
print('APPLE 🍎', apple)


running = True
while running:
    for event in pygame.event.get():
        # QUIT game
        if event.type == pygame.QUIT:
            running = False

        # MOVIMIENTO - snake
        if event.type == pygame.KEYDOWN and snake['in_game']:
            # if snake['in_game']:
            if event.key == pygame.K_LEFT:
                fn.draw_mov(snake, -mov_snake, 0)
                snake_img = 'L_HEAD'
            if event.key == pygame.K_RIGHT:
                fn.draw_mov(snake, mov_snake, 0)
                snake_img = 'R_HEAD'
            if event.key == pygame.K_UP:
                fn.draw_mov(snake, 0, -mov_snake)
                snake_img = 'UP_HEAD'
            if event.key == pygame.K_DOWN:
                fn.draw_mov(snake, 0, mov_snake)
                snake_img = 'DW_HEAD'
            # print(f'se presiono: {pygame.key.name(event.key)}')

        apple = fn.collision_obj(snake, apple)  # chequear si colisionó o no

        main_screen.fill(color.NEGRO)
        fn.update_mov(apple, '', main_screen)
        fn.update_mov(snake, snake_img, main_screen)
    pygame.display.update()
pygame.quit()
