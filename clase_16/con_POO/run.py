import pygame
from tablero import Tablero
from tarjeta import Tarjeta
from boton import Boton
from score import Score
from musica import Music
from constantes import *
import time # check

pygame.init()
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('The Simpsons Memotest')

running = True

# set tick timer
tick = pygame.USEREVENT
pygame.time.set_timer(tick, 1000)



# -------------------------------------------------------
l_tarjetas = []
l_botones = []
score = []

# TARJETAS
i = 1
for x in range(0, ANCHO_PANTALLA, ANCHO_TARJETA):
    for y in range(0, ALTO_PANTALLA - ALTO_TEXTO, ALTO_TARJETA):
        card = Tarjeta(f'/0{i}.png', '/00.png', x, y)
        l_tarjetas.append(card._initialize())
        if i < CANT_TOTAL_TARJETAS:
            i += 1
        else:
            i = 1
# BOTONES
start_btn = Boton('/start.png', ANCHO_PANTALLA - ANCHO_BOTON, ALTO_PANTALLA - ALTO_BOTON)
restart_btn = Boton('/restart.png', ANCHO_PANTALLA - ANCHO_BOTON-ANCHO_BOTON, ALTO_PANTALLA - ALTO_BOTON)
l_botones.extend([start_btn._initialize()] + [restart_btn._initialize()])

# SCORE
txt_font = pygame.font.SysFont('Arial Narrow', 50)
time_lapse = Score(txt_font, 'Tiempo: ', 0, ALTO_PANTALLA-ALTO_BOTON)
score.append(time_lapse._initialize())

# MUSICA
background = Music('/fondo.wav', 0.5)
win = Music('/ganador.wav')

# OTROS
start = False
# -------------------------------------------------------
tablero_juego = Tablero(l_tarjetas, l_botones, score, background, win, start)


################

################

clock_fps = pygame.time.Clock() # bloquea el while a x cantidad de FPS

while running:
    tiempo = clock_fps.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            tablero_juego.colicion(event.pos)
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                print('a')
                print()
        if event.type == pygame.USEREVENT:
            if event.type == tick:
                pass

    pantalla_juego.fill((255, 255, 255))
    tablero_juego.update()
    tablero_juego.render(pantalla_juego)
    pygame.display.flip()

pygame.quit()
