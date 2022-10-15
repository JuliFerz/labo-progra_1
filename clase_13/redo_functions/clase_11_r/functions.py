import re
import json
import os
from functools import reduce


def parse_json(path: str) -> list:
    '''
    Función que parsea un json para devolver una lista de diccionarios para trabajar
    Recibe una variable str con la dirección del archivo
    Devuelve una lista formateada
    '''
    with open(path, 'r') as file:
        lista_heroes = json.load(file)
    return lista_heroes['heroes']


lista_sw = parse_json('../clase_11_r/data_stark.json')
# print(lista_sw)


def guardar_resultados(path: str, content: str) -> str:
    '''
    Función que guarda los resultados en un archivo externo con fomrato csv
    Recibe una dirección y el conteido que debe guardar
    Devuelve la creación/sobreescritura del archivo con el contenido recibido
    '''
    aux_path = '../clase_11_r/results/'

    if re.search('.csv$', path):
        with open(f'{aux_path}{path}', 'w') as file:
            file.writelines(content)
        print('Datos guardados correctamente!')
    else:
        print(f'Formato de archivo incorrecto: {path}')


def menu_app():
    '''
    Función que imprime el menú con las opciones disponibles
    '''
    print('''
[1] Listar héroes según cantidad.
[2] Ordenar y listar heroes por altura ([ASC]: Forma ascendente [DESC]: Forma descendente).
[3] Ordenar y listar heroes por fuerza ([ASC]: Forma ascendente [DESC]: Forma descendente).
[4] Calcular un promedio de heroes ([MAYOR]: Listar del mayor al menor [MENOR]: Listar del menor al mayor).
[5] Listar heroes por inteligencia.
[6] Salir.
    ''')


def validar_tipo_numero(value: int) -> bool:
    '''
    Función que valida si el valor recibido (de tipo string) puede ser un entero o no
    Recibe un valor string
    Devuelve True en caso de ser positivo, o False en caso de no poder ser un int
    '''
    retorno = False
    if value and not re.search('[()<>a-zA-Z_!.,#]+', value):
        retorno = True
    return retorno


def mensaje_error(var='', sec_var=''):
    '''
    Funcion que imprime un mensaje de error genérico
    Recibe una variable (opcional) para mostrar en el mensaje
    Devuelve el mensaje de error
    '''
    os.system('cls')
    print('\n[ERROR]: Revise los datos de entrada')
    print(f'\t> Input: "{var}"') if var else ''
    print(f'\t> Input: "{sec_var}"') if sec_var else ''


def mostrar_mensaje(lista: list, key: str, qty: int = None):
    '''
    Función que muestra un mensaje pre-seteado por consola
    Recibe una lista, una key y una cantidad (opcional) 
    Devuelve el resultado del string al recorrer la lista
    '''
    list(map(lambda el: print(' • Nombre: {0} | {1}: {2}'.format(
        el.get('nombre'), key.capitalize(), el[key] or 'N/A')), lista[:qty]))


def almacenar_dato_csv(lista: list, key: str, qty: int = None):
    '''
    Función que guarda un resultado para un futuro archivo csv
    Recibe una lista, una key y una cantidad (opcional) 
    Develve la información obtenida por recorrer la lista
    '''
    result = list(
        map(lambda el: f'{el["nombre"]},{key},{el[key]}\n', lista[:qty]))
    return result


def final_listar_heroes(lista: list, qty: int) -> str:
    '''
    Función que lista los heroes por N cantidad. Si la cantidad excede la longitud de los heroes, retorna -1
    Recibe una lista y un int para la cantidad de heroes a mostrar
    Devuelve los heroes según la cantidad elegida
    '''
    os.system('cls')
    retorno = -1
    if validar_tipo_numero(qty):
        qty = int(qty)
        if (lista and qty <= len(lista)):
            mostrar_mensaje(lista, 'identidad', qty)
            format_csv = almacenar_dato_csv(lista, 'identidad', qty)

        guardar_resultados(
            f'listado_{qty}_heroes.csv', format_csv)
    elif lista:
        mensaje_error(qty)
    return retorno


def sort_list(lista: list, key: str, orden: str) -> list:
    '''
    Función que ordena una lista en base a una key y un orden recibido (asc o desc)
    Recibe una lista de heroes para ordenar, una key para saber con qué valor ordenar y un orden para saber si es asc o desc
    Retorna una copia de la lista con el orden especificado
    '''
    c_list = lista.copy()
    reverse = False
    if orden == 'desc':
        reverse = True
    c_list.sort(key=lambda el: el[key], reverse=reverse)
    return c_list


def final_ordenar_listar_altura(lista: list, orden: str) -> str:
    '''
    Funcion que ordena los heroes según altura y según orden especificada por usuario (ascendente o descendente)
    Recibe una lista de heroes y un orden
    Devuelve los resultados en función de la búsqueda
    '''
    os.system('cls')
    retorno = -1
    copy_list = lista.copy()
    if lista and re.search('^asc$|^desc$', orden, re.IGNORECASE):
        lista_ordenada = sort_list(copy_list, 'altura', orden)
        mostrar_mensaje(lista_ordenada, 'altura')
        format_csv = almacenar_dato_csv(lista_ordenada, 'altura')

        retorno = lista_ordenada
        guardar_resultados(f'listado_{orden}_altura_heroes.csv', format_csv)
    else:
        mensaje_error(orden)
    return retorno


def final_ordenar_listar_fuerza(lista: list, orden: str) -> str:
    '''
    Funcion que ordena los heroes según fuerza y según orden especificada por usuario (ascendente o descendente)
    Recibe una lista de heroes y un orden
    Devuelve los resultados en función de la búsqueda
    '''
    os.system('cls')
    retorno = -1
    copy_list = lista.copy()
    if lista and re.search('^asc$|^desc$', orden, re.IGNORECASE):
        lista_ordenada = sort_list(copy_list, 'fuerza', orden)
        mostrar_mensaje(lista_ordenada, 'fuerza')
        format_csv = almacenar_dato_csv(lista_ordenada, 'fuerza')

        retorno = lista_ordenada
        guardar_resultados(f'listado_{orden}_fuerza_heroes.csv', format_csv)
    else:
        mensaje_error(orden)
    return retorno


def sumar_valores_heroes(lista: list, key: str) -> int:
    '''
    Función que suma los valores numericos de la key de los heroes
    Recibe una lista de heroes y una key para sumar el valor
    Devuelve la suma de dicha key
    '''
    return reduce(lambda x, y: x + y[key], lista, 0)


print(sumar_valores_heroes(lista_sw, 'altura'))


def cant_key_heroes(lista: list, key: str) -> int:
    '''
    Función que suma la cantidad de heroes que tienen la key recibida
    Recibe una lista de heroes y una key para sumar la cantidad de heroes
    Devuelve la cantidad de heroes que tienen esa key
    '''
    lista_temp = list(filter(lambda x: x.get(key), lista))
    return reduce(lambda x, y: x + 1, lista_temp, 0)


def dividir_nros(dividendo: int, divisor: int) -> int:
    '''
    Función que divide dos numeros
    Retorna el resultado de dicha división si el divisor es válido (> 0). Caso negativo, devuelve -1
    '''
    retorno = -1
    if divisor > 0:
        retorno = dividendo / divisor
    return retorno


def calcular_promedio_heroes(lista: list, key: str) -> int:
    '''
    Función que calcula el promedio de un valor numérico de los heroes 
    Recibe una lista de heroes, una key para calcular su promedio 
    Devuelve los heroes según las condiciones dadas
    '''
    retorno = -1

    if lista[0].get(key) and (type(lista[0].get(key) == type(0)) or
                              type(lista[0].get(key) == type(0.0))):
        valor_sumado = sumar_valores_heroes(lista, key)
        cant_key = cant_key_heroes(lista, key)
        retorno = dividir_nros(valor_sumado, cant_key)
    else:
        mensaje_error(key)
    return retorno


def final_listar_heroes_segun_promedio(lista: list, key: str, tipo: str) -> str:
    '''
    Función que evalúa qué heroe tiene valor menor o mayor (a elección) del promedio calculado en otra función
    Recibe una lista de heroes, una key para evaluar y un tipo para saber si calcula menor o mayor
    Devuelve los heroes que cumplan con la condición (menor/mayor) sobre el promedio calculado
    '''
    os.system('cls')
    c_list = lista.copy()
    if c_list[0].get(key) and len(c_list) > 0 and re.search('^menor$|^mayor$', tipo, re.IGNORECASE):
        promedio_calculado = calcular_promedio_heroes(c_list, key)
        print(f'Promedio: {promedio_calculado}')
        if tipo.lower() == 'menor':
            lista_temp = list(
                filter(lambda el: el[key] < promedio_calculado, c_list))
        elif tipo.lower() == 'mayor':
            lista_temp = list(
                filter(lambda el: el[key] > promedio_calculado, c_list))

        mostrar_mensaje(lista_temp, key)
        format_csv = almacenar_dato_csv(lista_temp, key)

        guardar_resultados(
            f'listado_{tipo.lower()}_heroes_segun_promedio_{key}.csv', format_csv)
    else:
        mensaje_error(key, tipo)


def calcular_heroes_inteligencia(lista: list) -> list:
    '''
    Función que calcula cuánta cantidad de heroes hay por cada tipo de inteligencia
    Recibe una lista de heroes
    Devuelve una lista de diccionarios por cada inteligencia (colocando los nombres por cada uno)
    '''
    dict_temp = {}
    if len(lista) > 0:
        list(map(lambda el: dict_temp.update({el['inteligencia']: [el['nombre']]})
                 if not el['inteligencia'] in dict_temp
                 else dict_temp[el['inteligencia']].append(el['nombre']), lista))
    return dict_temp


def final_listar_heroes_inteligencia(lista: list) -> str:
    '''
    Función que lista todos los heroes por tipo de inteligencia
    Recibe una lista de heroes
    Devuelve por consola cada heroe por cada tipo de inteligencia
    '''
    os.system('cls')
    heroes_inteligencia = calcular_heroes_inteligencia(lista)
    format_csv = []

    for key in heroes_inteligencia:
        print(f'\nINTELIGENCIA: {key.capitalize() or "N/A"}')
        for nombre in heroes_inteligencia[key]:
            print(f'• Nombre: {nombre}')
            format_csv.append('{0},{1}\n'.format(key or 'N/A', nombre))

    guardar_resultados(f'listado_heroes_inteligencia.csv', format_csv)
