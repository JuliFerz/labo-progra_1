import pygame
import time
from constantes import *
import tablero 


pygame.init()  # Se inicializa pygame
# pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA + 100))
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('The Simpsons Memotest')

running = True
cuadrado = pygame.Rect(30, 30, 60, 60)


# set tick timer
tick = pygame.USEREVENT
pygame.time.set_timer(tick, 1000)


tablero_juego = tablero.init()
# print(tablero_juego)

clock_fps = pygame.time.Clock() # bloquea el while a x cantidad de FPS


while running:
    tiempo = clock_fps.tick(15) # bloquea a 60 FPS
    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)  # mouse position
            tablero.colicion(tablero_juego, event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # tablero.shuffle(tablero_juego) # test
                pass
            elif event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.USEREVENT:
            if event.type == tick:
                # print("Ya paso un segundo")
                pass

    # Se pinta el fondo de la ventana de blanco
    pantalla_juego.fill((255, 255, 255))
    tablero.update(tablero_juego)
    tablero.render(tablero_juego, pantalla_juego)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
