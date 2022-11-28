import pygame, sys
from constantes import *
from form_menu_A_gui import MenuForm_A
from form_menu_B_gui import MenuForm_B



screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('PYGAME | Forms')
pygame.init()
clock = pygame.time.Clock()


MenuForm_A = MenuForm_A(
    name='MenuForm_A',
    main_surface=screen,
    x=0,
    y=100,
    w=300,
    h=400,
    color_background=GREEN,
    color_border='',
    active=True)
MenuForm_B = MenuForm_B(
    name='MenuForm_B',
    main_surface=screen,
    x=200,
    y=100,
    w=300,
    h=400,
    color_background=(0, 255, 255),
    color_border='',
    active=False)

print(MenuForm_A.form_dict)

running = True
while running:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.KEYDOWN: # Test
            if event.key == pygame.K_ESCAPE:
                running = False
                sys.exit()

    delta_ms = clock.tick(FPS)

    if MenuForm_A.active:
        MenuForm_A.update(event_list)
        MenuForm_A.draw()
    elif MenuForm_B.active:
        MenuForm_B.update(event_list)
        MenuForm_B.draw()
    pygame.display.flip()
    
pygame.quit()
sys.exit()