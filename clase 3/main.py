from data_stark import lista_heroes


def calcular_heroe_mas_alto():
    # -------------- SUPERHEROE MAS ALTO
    heroe_mas_alto = lista_heroes[0]
    for heroe in lista_heroes:
        altura_heroe = heroe
        if(float(heroe['altura']) > float(heroe_mas_alto['altura'])):
            heroe_mas_alto = altura_heroe
    print('El heroe mas ALTO es: "{0}" con altura: {1:.2f}'.format(
        heroe_mas_alto['nombre'], float(heroe_mas_alto['altura'])))


def calcular_heroe_mas_bajo():
    # -------------- SUPERHEROE MAS BAJO
    heroe_mas_bajo = lista_heroes[0]
    for heroe in lista_heroes:
        altura_heroe = heroe
        if(float(heroe['altura']) < float(heroe_mas_bajo['altura'])):
            heroe_mas_bajo = altura_heroe
    print('El heroe mas BAJO es: "{0}" con altura: {1:.2f}'.format(
        heroe_mas_bajo['nombre'], float(heroe_mas_bajo['altura'])))


def calcular_promedio_alturas():
    # -------------- PROMEDIO DE ALTURAS
    acumulador_alturas = 0
    for heroe in lista_heroes:
        acumulador_alturas += float(heroe['altura'])
    print('El promedio de alturas es: {0:.2f}'.format(
        acumulador_alturas / len(lista_heroes)))


def calcular_heroe_mas_pesado():
    # -------------- SUPERHEROE MAS PESADO
    heroe_mas_pesado = lista_heroes[0]
    for heroe in lista_heroes:
        peso_heroe = heroe
        if(float(heroe['peso']) > float(heroe_mas_pesado['peso'])):
            heroe_mas_pesado = peso_heroe
    print('El heroe MAS pesado es: "{0}" con peso: {1:.2f}'.format(
        heroe_mas_pesado['nombre'], float(heroe_mas_pesado['peso'])))


def calcular_heroe_menos_alto():
    # -------------- SUPERHEROE MENOS PESADO
    heroe_menos_pesado = lista_heroes[0]
    for heroe in lista_heroes:
        peso_heroe = heroe
        if(float(heroe['peso']) < float(heroe_menos_pesado['peso'])):
            heroe_menos_pesado = peso_heroe
    print('El heroe MENOS pesado es: "{0}" con peso: {1:.2f}'.format(
        heroe_menos_pesado['nombre'], float(heroe_menos_pesado['peso'])))


while True:
    answer = input('\n[1]: Traer el héroe más alto\n\
[2]: Traer el héroe más bajo\n\
[3]: Traer el promedio de alturas\n\
[4]: Traer el héroe más pesado\n\
[5]: Traer el héroe menos pesado\n\
[6]: Salir del programa\n\n> ')
    while(not answer.isnumeric() or (int(answer) < 1 or int(answer) > 6)):
        answer = input('[ERROR]: Seleccione una opcion correcta\n>')

    if(answer == '1'):
        calcular_heroe_mas_alto()
    elif(answer == '2'):
        calcular_heroe_mas_bajo()
    elif(answer == '3'):
        calcular_promedio_alturas()
    elif(answer == '4'):
        calcular_heroe_mas_pesado()
    elif(answer == '5'):
        calcular_heroe_menos_alto()
    elif(answer == '6'):
        break
