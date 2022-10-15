from functions import *
import re
import os


def menu_principal():
    '''
    Función principal que imprime el menu y toma los datos del cliente para mostrar/guardar los datos a elección
    '''
    path = '../clase_11_r/data_stark.json'
    lista_heroes = parse_json(path)
    os.system('cls')
    while True:
        menu_app()
        answer = input('\nElija una opcion:\n> ')
        if re.search('^[1-6]{1}$', answer):
            if answer == '1':
                aux_answer = input('Elija la cantidad de heroes a listar:\n> ')
                final_listar_heroes(lista_heroes, aux_answer)
            elif answer == '2':
                aux_answer = input(
                    'Elija el orden que desea recibir los datos ["asc"]: Ascendente | ["desc"]: Descendente:\n> ')
                final_ordenar_listar_altura(lista_heroes, aux_answer)
            elif answer == '3':
                aux_answer = input(
                    'Elija el orden que desea recibir los datos ["asc"]: Ascendente | ["desc"]: Descendente:\n> ')
                final_ordenar_listar_fuerza(lista_heroes, aux_answer)
            elif answer == '4':
                aux_key = input(
                    'Escriba qué dato numérico desea calcular el promedio ["altura", "peso" o "fuerza]\n> ')
                aux_tipo = input(
                    'Elija si desea evaluar por menor o mayor en el promedio ["menor"]: Buscar los menores | ["mayor"]: Buscar los mayores:\n> ')
                final_listar_heroes_segun_promedio(
                    lista_heroes, aux_key, aux_tipo)
            elif answer == '5':
                final_listar_heroes_inteligencia(lista_heroes)
            elif answer == '6':
                os.system('cls')
                break
        else:
            print('[ERROR] Elija una opción correcta')
            continue


menu_principal()
