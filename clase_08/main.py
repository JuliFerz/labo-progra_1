from functions import *
path = './clase_08/data_stark.json'
lista_heroes = leer_archivo(path)


def stark_marvel_app_5(lista: list) -> str:
    '''
    Funcion principal de la aplicación..
    Devuelve los datos de la opción elegida por el usuario
    '''
    while True:
        answer = stark_menu_principal_desafio_5()
        if(answer == -1):
            print('[ERROR] Dato ingresado incorrecto')
        elif (answer == 'A'):
            stark_guardar_heroe_genero(lista, 'M')
        elif (answer == 'B'):
            stark_guardar_heroe_genero(lista, 'F')
        elif (answer == 'C'):
            stark_calcular_imprimir_heroe(lista, 'max', 'altura', 'M')
        elif (answer == 'D'):
            stark_calcular_imprimir_heroe(lista, 'max', 'altura', 'F')
        elif (answer == 'E'):
            stark_calcular_imprimir_heroe(lista, 'min', 'altura', 'M')
        elif (answer == 'F'):
            stark_calcular_imprimir_heroe(lista, 'min', 'altura', 'F')
        elif (answer == 'G'):
            stark_calcular_imprimir_guardar_promedio_altura_genero(lista, 'M')
        elif (answer == 'H'):
            stark_calcular_imprimir_guardar_promedio_altura_genero(lista, 'F')
        elif (answer == 'I'):
            stark_calcular_cantidad_por_tipo(lista, 'color_ojos')
        elif (answer == 'J'):
            stark_calcular_cantidad_por_tipo(lista, 'color_pelo')
        elif (answer == 'K'):
            stark_calcular_cantidad_por_tipo(lista, 'inteligencia')
        elif (answer == 'L'):
            stark_listar_heroes_por_dato(lista, 'color_ojos')
        elif (answer == 'M'):
            stark_listar_heroes_por_dato(lista, 'color_pelo')
        elif (answer == 'N'):
            stark_listar_heroes_por_dato(lista, 'inteligencia')
        elif (answer == 'Z'):
            return


stark_marvel_app_5(lista_heroes)
