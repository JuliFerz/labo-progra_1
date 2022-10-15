from functions import *


def stark_marvel_app_5() -> str:
    '''
    Funcion principal de la aplicación..
    Devuelve los datos de la opción elegida por el usuario
    '''
    path = '../clase_08_r/data_stark.json'
    lista_heroes = leer_archivo(path)
    os.system('cls')
    while True:
        answer = stark_menu_principal_desafio_5()
        if(answer == -1):
            print('[ERROR] Dato ingresado incorrecto')
        elif (answer == 'A'):
            stark_guardar_heroe_genero(lista_heroes, 'M')
        elif (answer == 'B'):
            stark_guardar_heroe_genero(lista_heroes, 'F')
        elif (answer == 'C'):
            stark_calcular_imprimir_heroe(lista_heroes, 'max', 'altura', 'M')
        elif (answer == 'D'):
            stark_calcular_imprimir_heroe(lista_heroes, 'max', 'altura', 'F')
        elif (answer == 'E'):
            stark_calcular_imprimir_heroe(lista_heroes, 'min', 'altura', 'M')
        elif (answer == 'F'):
            stark_calcular_imprimir_heroe(lista_heroes, 'min', 'altura', 'F')
        elif (answer == 'G'):
            stark_calcular_imprimir_guardar_promedio_altura_genero(
                lista_heroes, 'M')
        elif (answer == 'H'):
            stark_calcular_imprimir_guardar_promedio_altura_genero(
                lista_heroes, 'F')
        elif (answer == 'I'):
            stark_calcular_cantidad_por_tipo(lista_heroes, 'color_ojos')
        elif (answer == 'J'):
            stark_calcular_cantidad_por_tipo(lista_heroes, 'color_pelo')
        elif (answer == 'K'):
            stark_calcular_cantidad_por_tipo(lista_heroes, 'inteligencia')
        elif (answer == 'L'):
            stark_listar_heroes_por_dato(lista_heroes, 'color_ojos')
        elif (answer == 'M'):
            stark_listar_heroes_por_dato(lista_heroes, 'color_pelo')
        elif (answer == 'N'):
            stark_listar_heroes_por_dato(lista_heroes, 'inteligencia')
        elif (answer == 'Z'):
            os.system('cls')
            return


stark_marvel_app_5()
