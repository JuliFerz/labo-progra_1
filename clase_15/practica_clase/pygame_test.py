import pygame
import pygments
import colores

pygame.init()

ANCHO_VENTANA = 500
ALTO_VENTANA = 500

ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
# ventana_ppal.fill(COLOR_NARANJA)  # color a la ventana
pygame.display.set_caption('Pygame test')

print(type(ventana_ppal))  # Es de la clase SUPERFICIE ('pygame.Surface')

# REFRESCA TODO :
# pygame.display.flip()
# REFRESCA LO QUE LE PASEMOS POR PARAMETRO; SIN ÉL REFRESCA TODO (como flip):
# pygame.display.update()

running = True
pos_circulo = [30, 60]

# TIMER
# si se crea otro USEREVENT para un timer, deberá colocarse al final +1 +2 +n según cantidad de timer creados
timer_seg = pygame.USEREVENT + 0
pygame.time.set_timer(timer_seg, 1000)


# LEER IMAGEN
imagen_fondo = pygame.image.load('./clase_15/clase/a.png')
# escalar imagen (cambiar resolución)
imagen_fondo = pygame.transform.scale(imagen_fondo, (250, 250))
rect_imagen = pygame.Rect((0, 0), (250, 250))


# CREAR TEXTO
# crear fuente
fuente = pygame.font.SysFont('Arial', 30)
# renderizar texto (crear superficie)
texto = fuente.render('HOLA NAJIMI', True, colores.ROJO)  # es una superficie


# escala = [50, 50]
flag_mostrar_txt = False

while running:

    # Guardar lista de eventos (aparece TODO). El método get guarda la lista con TODOS los eventos
    lista_eventos = pygame.event.get()

    # FOR que analiza los eventos:
    for evento in lista_eventos:  # loopeo esa lista con los eventos
        if evento.type == pygame.QUIT:  # QUIT es apretar la X de la ventana
            # print(evento.type) # Se ejecuta el evento "256"
            running = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # el mouse viene con un dato adicional: la posición
            print(evento.pos)  # Hace una tupla (x, y)
            # Cambiamos la posición del ciruclo con cada click
            pos_circulo = list(evento.pos)
        if evento.type == pygame.USEREVENT:
            if evento.type == timer_seg:
                if pos_circulo[0] < ANCHO_VENTANA + 80:
                    pos_circulo[0] = pos_circulo[0] + 10
                    pass
                else:
                    pos_circulo[0] = -80
                    pass
            if evento.type == timer_seg:
                flag_mostrar_txt = True
                pass
        """ if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                pos_circulo[1] = pos_circulo[1] + 10
                """
    # leer el teclado FUERA del for de los eventos
    efecto = 30
    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_DOWN]:
        pos_circulo[1] = pos_circulo[1] + 1 / efecto
    if lista_teclas[pygame.K_UP]:
        pos_circulo[1] = pos_circulo[1] - 1 / efecto
    if lista_teclas[pygame.K_LEFT]:
        pos_circulo[0] = pos_circulo[0] - 1 / efecto
    if lista_teclas[pygame.K_RIGHT]:
        pos_circulo[0] = pos_circulo[0] + 1 / efecto

    ventana_ppal.fill(colores.NARANJA)
    pygame.draw.circle(ventana_ppal, colores.NEGRO, pos_circulo, (80))
    pygame.draw.rect(ventana_ppal, colores.ROJO, (30, 60, 100, 200))

    # Fundir una imagen (para que la imagen esté arriba de todo en la superficie). Blit posiciona el elemento al principio de todo
    # ventana_ppal.blit(imagen_fondo, (coordenada, coordenada, tamaño, tamaño))

    pygame.draw.rect(ventana_ppal, colores.ROJO, rect_imagen)
    ventana_ppal.blit(imagen_fondo, rect_imagen)

    # if flag_mostrar_txt:
    # ventana_ppal.blit(texto, (300, 300))

    # imagen_fondo = pygame.transform.scale(imagen_fondo, escala)

    pygame.display.update()

pygame.quit()
