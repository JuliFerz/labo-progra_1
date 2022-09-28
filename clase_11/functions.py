import re
import json


def parse_json(path: str) -> list:
    '''
    Función que parsea un json para devolver una lista de diccionarios para trabajar
    Recibe una variable str con la dirección del archivo
    Devuelve una lista formateada
    '''
    with open(path, 'r') as file:
        lista_heroes = json.load(file)
    return lista_heroes['heroes']


def guardar_resultados(path: str, content: str) -> str:
    '''
    Función que guarda los resultados en un archivo externo con fomrato csv
    Recibe una dirección y el conteido que debe guardar
    Devuelve la creación/sobreescritura del archivo con el contenido recibido
    '''
    aux_path = './clase_11/results/'

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


def final_listar_heroes(lista: list, qty: int) -> str:
    '''
    Función que lista los heroes por N cantidad. Si la cantidad excede la longitud de los heroes, retorna -1
    Recibe una lista y un int para la cantidad de heroes a mostrar
    Devuelve los heroes según la cantidad elegida
    '''
    retorno = -1
    if validar_tipo_numero(qty):
        qty = int(qty)
        if (lista and qty <= len(lista)):
            format_csv = []
            for heroe in lista[:qty]:
                h_identidad = heroe.get('identidad') or 'N/A'
                print(' • Nombre: {0} | Identidad: {1}'.format(
                    heroe.get('nombre'), h_identidad))

                format_csv.append('{0},{1}\n'.format(
                    heroe.get('nombre'), h_identidad))
            guardar_resultados(f'listado_{qty}_heroes.csv', format_csv)
    elif lista:
        print(f'[ERROR] Verifique la cantidad solicitada: {qty}')
    return retorno


def sort_list(lista: list, key: str, orden: str) -> list:
    '''
    Función que ordena una lista en base a una key y un orden recibido (asc o desc)
    Recibe una lista de heroes para ordenar, una key para saber con qué valor ordenar y un orden para saber si es asc o desc
    Retorna una copia de la lista con el orden especificado
    '''
    c_list = lista.copy()

    for i in range(len(c_list)):
        for j in range(len(c_list)):
            if orden == 'asc':
                if c_list[i][key] < c_list[j][key]:
                    c_list[i], c_list[j] = c_list[j], c_list[i]
            elif orden == 'desc':
                if c_list[i][key] > c_list[j][key]:
                    c_list[i], c_list[j] = c_list[j], c_list[i]
    return c_list


def final_ordenar_listar_altura(lista: list, orden: str) -> str:
    '''
    Funcion que ordena los heroes según altura y según orden especificada por usuario (ascendente o descendente)
    Recibe una lista de heroes y un orden
    Devuelve los resultados en función de la búsqueda
    '''
    retorno = -1
    copy_list = lista.copy()
    if lista and re.search('^asc$|^desc$', orden, re.IGNORECASE):
        lista_ordenada = sort_list(copy_list, 'altura', orden)
        format_csv = []
        for el in lista_ordenada:
            a_heroe = el.get('altura') or 'N/A'
            print(' • Nombre: {0} | Altura: {1}'.format(
                el.get('nombre'), a_heroe))

            format_csv.append('{0},{1}\n'.format(
                el.get('nombre'), a_heroe))
        guardar_resultados(f'listado_{orden}_altura_heroes.csv', format_csv)

        retorno = lista_ordenada

    return retorno


def final_ordenar_listar_fuerza(lista: list, orden: str) -> str:
    '''
    Funcion que ordena los heroes según fuerza y según orden especificada por usuario (ascendente o descendente)
    Recibe una lista de heroes y un orden
    Devuelve los resultados en función de la búsqueda
    '''
    retorno = -1
    copy_list = lista.copy()
    if lista and re.search('^asc$|^desc$', orden, re.IGNORECASE):
        lista_ordenada = sort_list(copy_list, 'fuerza', orden)
        format_csv = []
        for el in lista_ordenada:
            f_heroe = el.get('fuerza') or 'N/A'

            print(' • Nombre: {0} | Fuerza: {1}'.format(
                el.get('nombre'), f_heroe))

            format_csv.append('{0},{1}\n'.format(
                el.get('nombre'), f_heroe))
        guardar_resultados(f'listado_{orden}_fuerza_heroes.csv', format_csv)
        retorno = lista_ordenada

    return retorno


def sumar_valores_heroes(lista: list, key: str) -> int:
    '''
    Función que suma los valores numericos de la key de los heroes
    Recibe una lista de heroes y una key para sumar el valor
    Devuelve la suma de dicha key
    '''
    retorno = 0
    for el in lista:
        if el.get(key):
            retorno += el[key]
    return retorno


def cant_key_heroes(lista: list, key: str) -> int:
    '''
    Función que suma la cantidad de heroes que tienen la key recibida
    Recibe una lista de heroes y una key para sumar la cantidad de heroes
    Devuelve la cantidad de heroes que tienen esa key
    '''
    retorno = 0
    for el in lista:
        if el.get(key):
            retorno += 1
    return retorno


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

    if type(lista[0].get(key) == type(0)) or \
            type(lista[0].get(key) == type(0.0)):
        valor_sumado = sumar_valores_heroes(lista, key)
        cant_key = cant_key_heroes(lista, key)
        retorno = dividir_nros(valor_sumado, cant_key)
    else:
        print(
            f'[ERROR] Verifique los datos de entrada:\n• Key: "{key}"')
    return retorno


def final_listar_heroes_segun_promedio(lista: list, key: str, tipo: str) -> str:
    '''
    Función que evalúa qué heroe tiene valor menor o mayor (a elección) del promedio calculado en otra función
    Recibe una lista de heroes, una key para evaluar y un tipo para saber si calcula menor o mayor
    Devuelve los heroes que cumplan con la condición (menor/mayor) sobre el promedio calculado
    '''
    c_list = lista.copy()
    if len(c_list) > 0 and re.search('^menor$|^mayor$', tipo, re.IGNORECASE):
        promedio_calculado = calcular_promedio_heroes(c_list, key)
        print(f'Promedio: {promedio_calculado}')
        format_csv = []
        for heroe in c_list:
            if tipo.lower() == 'menor':
                if heroe[key] < promedio_calculado:
                    print(
                        ' • Nombre: {0} | Característica: {1} -> {2}'.format(heroe.get('nombre'), key, heroe[key]))
                    format_csv.append('{0},{1},{2}\n'.format(
                        heroe.get('nombre'), key, heroe[key]))
            elif tipo.lower() == 'mayor':
                if heroe[key] > promedio_calculado:
                    print(
                        ' • Nombre: {0} | Característica: {1} -> {2}'.format(heroe.get('nombre'), key, heroe[key]))
                    format_csv.append('{0},{1},{2}\n'.format(
                        heroe.get('nombre'), key, heroe[key]))

        guardar_resultados(
            f'listado_{tipo.lower()}_heroes_segun_promedio_{key}.csv', format_csv)
    else:
        print('[ERROR] Verifique los datos de entrada')


def calcular_heroes_inteligencia(lista: list) -> list:
    '''
    Función que calcula cuánta cantidad de heroes hay por cada tipo de inteligencia
    Recibe una lista de heroes
    Devuelve una lista de diccionarios por cada inteligencia (colocando los nombres por cada uno)
    '''

    list_intel = set([])
    dict_temp = {}
    if len(lista) > 0:
        for el in lista:
            tipo_inteligencia = el['inteligencia'] or 'N/A'
            list_intel.add(tipo_inteligencia)
            if not tipo_inteligencia in dict_temp:
                dict_temp[tipo_inteligencia] = [el['nombre']]
            else:
                dict_temp[tipo_inteligencia].append(el['nombre'])
    return dict_temp


def final_listar_heroes_inteligencia(lista: list) -> str:
    '''
    Función que lista todos los heroes por tipo de inteligencia
    Recibe una lista de heroes
    Devuelve por consola cada heroe por cada tipo de inteligencia
    '''

    heroes_inteligencia = calcular_heroes_inteligencia(lista)
    format_csv = []
    for key in heroes_inteligencia:
        print(f'\nINTELIGENCIA: {key}')
        for nombre in heroes_inteligencia[key]:
            print(f'• Nombre: {nombre}')
            format_csv.append('{0},{1}\n'.format(key, nombre))

    guardar_resultados(f'listado_heroes_inteligencia.csv', format_csv)
