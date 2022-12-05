import pygame, sys
from constantes import *
# from form_gui import MenuForm
from form_main_menu import FormMainMenu
from form_main_menu_level_selection import FormMainMenuLevelSelection
# from form_level_selector import FormLevelSelector


# ([screen] -> form_surface -> button_surface)
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('PYGAME | Forms')
pygame.init()
clock = pygame.time.Clock()


form_main_menu = FormMainMenu(
    name='form_main_menu',
    main_surface=screen,
    x=50,
    y=50,
    w=ANCHO_VENTANA - 100,
    h=ALTO_VENTANA - 100,
    color_background=RED,
    color_border='',
    active=True) 

form_main_menu_selection = FormMainMenuLevelSelection(
    name='form_main_menu_selection',
    main_surface=screen,
    x=50,
    y=50,
    w=ANCHO_VENTANA - 100,
    h=ALTO_VENTANA - 100,
    color_background=RED,
    color_border='',
    active=False)


running = True
while running:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        # elif event.type == pygame.KEYDOWN: # Test
        #     if event.key == pygame.K_ESCAPE:
        #         running = False
        #         sys.exit()

    delta_ms = clock.tick(FPS)


    if form_main_menu.active:
        form_main_menu.update(event_list)
    elif form_main_menu_selection.active:
        form_main_menu_selection.update(event_list)

    pygame.display.flip()
    
pygame.quit()
sys.exit()