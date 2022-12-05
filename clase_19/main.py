import pygame, sys
from constantes import *
from mouse import Cursor
from level import Level
from menu import Menu
from settings import game_levels, game_config

#  pygame.FULLSCREEN
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('PYGAME | Juego')
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

start_time = pygame.time.get_ticks()
# level = Level(level_map, screen) # REVISAR hacer en el form

level = Menu(screen, game_levels, game_config)

pygame.mouse.set_visible(False)
cursor = Cursor()
running = True

while running:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    delta_ms = clock.tick(FPS)
    cursor.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

    # Execute level
    level.run(event_list, delta_ms) # REVISAR
    
    cursor.draw(screen)
    pygame.display.flip()
    
pygame.quit()
sys.exit()