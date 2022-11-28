import pygame, sys
from constantes import *
from mouse import Cursor
from level import Level
from settings import level_map
from gui import *

#  pygame.FULLSCREEN
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('PYGAME | Juego')
pygame.init()
clock = pygame.time.Clock()


# level = Level(level_map, screen) # REVISAR hacer en el form

pygame.mouse.set_visible(False)
cursor = Cursor()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.KEYDOWN: # Test
            if event.key == pygame.K_ESCAPE:
                running = False
                sys.exit()
            if event.key == pygame.K_p:
                pass
        elif event.type == pygame.KEYUP:
            ## Revisar
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ## Revisar
            pass

    delta_ms = clock.tick(FPS)

    # Draw Screen, Cursor (update) & FPS
    # screen.blit(imagen_fondo, imagen_fondo.get_rect())
    # cursor.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

    # Execute level
    # level.run(delta_ms) # REVISAR
    cursor.draw(screen)
    pygame.display.flip()
    
pygame.quit()
sys.exit()