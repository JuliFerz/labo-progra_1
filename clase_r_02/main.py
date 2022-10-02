import re
import os
import functions as _f
path = '../clase_r_02/pokedex.json'


def poke_app():
    '''
    Función principal del programa. Imprime el menu y recibe por input la opción elegida por el usuario
    No recibe parámetros
    Retorna por consola los resultados en cuestión
    '''
    lista_pokedex = _f.parse_json(path)
    os.system('cls')

    resultado = ''
    while True:
        _f.imprimir_menu()
        answer = input('Elija una opción:\n> ')

        if re.search('^[1-7]{1}$', answer):

            if answer == '1':
                qty = input('Elija la cantidad de pokemones a mostrar:\n> ')
                resultado = _f.final_listar_pokemones(lista_pokedex, qty)
            elif answer == '2':
                mode = input(
                    'Elija el modo para ordenar\n\t[asc]: Ascendente [desc]: Descendente\n> ')
                resultado = _f.final_ordenar_listar_poder(lista_pokedex, mode)
            elif answer == '3':
                mode = input(
                    'Elija el modo para ordenar\n\t[asc]: Ascendente [desc]: Descendente\n> ')
                resultado = _f.final_ordenar_listar_id(lista_pokedex, mode)
            elif answer == '4':
                answer_prom = input(
                    'De qué key desea buscar?\n\t Evoluciones\n\t Fortaleza\n\t Debilidad\n\t Tipo\n> ')
                answer_orden = input(
                    'Elija el modo para buscar\n\t[menor]: Busca los menores al promedio\n\t[mayor]: Busca los mayores al promedio\n> ')
                resultado = _f.final_promedio_pokemones(
                    lista_pokedex, answer_prom, answer_orden)
            elif answer == '5':
                answer_tipo = input(
                    f'Por qué tipo desea buscar?\n{_f.obtener_lista_tipos(lista_pokedex, "tipo")}\n> ')
                _f.final_mostrar_pokemones_tipo(lista_pokedex, answer_tipo)
            elif answer == '6':
                _f.guardar_csv('resultados.csv', resultado)

            elif answer == '7':
                os.system('cls')
                break

        else:
            _f.error_mess(answer)


poke_app()
