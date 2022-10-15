import json
import re
import copy


def cargar_json(path: str) -> list:
    '''
    función que parsea un archivo json para utilizarlo en la app
    recibe un path con la dirección del archivo json
    devuelve una lista con la información del json
    '''

    with open(path, 'r') as file:
        lista_sw = json.load(file)
    return lista_sw['results']


def guardar_resultados(path: str, content: str) -> str:
    '''
    Función que se encarga de guardar el contenido que le llegue por parámetro en un archivo nuevo (en caso de existir, lo sobreescribe)
    Recibe una dirección y un contenido
    Devuelve la creación/sobreescritura del archivo
    '''

    aux_path = '../parcial_01/results/'
    with open(f'{aux_path}{path}', 'w') as file:
        file.writelines(content)


def es_entero(var: str) -> bool:
    '''
    Función que evalua si un valor recibido puede ser un entero o no
    Recibe una variable string para evaluar
    Devuelve un True si dicho valor puede ser entero, False en caso incorrecto
    '''
    retorno = False
    if not re.search('[.,a-zA-Z]+', var):
        retorno = True
    return retorno


def sanitizar_entero(lista: list, key: str) -> list:
    '''
    Función que castea una key determinada en una lista (castea a int)
    Recibe una lista y una key para recorrer y castear dicha key
    Devuelve la lista con la key casteada
    '''

    for el in lista:
        if es_entero(el[key]):
            el[key] = int(el[key])
        else:
            print('El origien de los datos tiene un formato inválido')
            break
    return lista


def b_sort(lista: list, key: str) -> list:
    '''
    función que ordena una lista en base a una key numérica
    Recibe una lista y una key para ordenar
    Devuelve la lista con orden descendente (en función de la key)
    '''
    lista = sanitizar_entero(lista, key)
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[j][key] > lista[i][key]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def final_lista_personajes_altura(lista: str) -> str:
    '''
    Función que lista los personajes ordenados por altura
    Recibe una lista
    Devuelve por consola los personajes 
    '''

    c_list = copy.deepcopy(lista)
    c_lista_ordenada = b_sort(c_list, 'height')
    csv_result = []
    for el in c_lista_ordenada:
        print(f'Nombre: {el["name"]} - Altura: {el["height"]}')
        csv_result.append(f'{el["name"]},{el["height"]}\n')
    return csv_result


def obtener_generos(lista: list) -> set:
    '''
    Función que obtiene todos los generos disponibles de una lista
    Recibe una lista
    Devuelve un set con todos los generos disponibles (sin repetición)
    '''
    generos = set([])
    for el in lista:
        generos.add(el['gender'])
    return generos


def obtener_primer_personaje_genero(lista: list, gen: str) -> dict:
    '''
    Función que toma el primer personaje que coincida con el genero que reciba por parámetro
    Recibe una lista y un genero para evaluar
    Devuelve un diccionario con la información del primer hreoe que encontró coincidencia
    '''
    for el in lista:
        if el['gender'] == gen:
            return el


def obtener_mas_alto_por_genero(lista: list, gen: str) -> str:
    '''
    Función que obtiene el personaje más alto en base a un genero recibido
    Recibe una lista de personajes y un genero para encontrar el más alto
    Devuelve el personaje más alto del genero recibido
    '''

    c_list = copy.deepcopy(lista)
    c_list = sanitizar_entero(c_list, 'height')

    max_altura = obtener_primer_personaje_genero(c_list, gen)
    for el in c_list:
        if el['gender'] == gen and el['height'] > max_altura['height']:
            max_altura = el
    return max_altura


def final_mostrar_personajes_genero(lista: list) -> str:
    '''
    Función que muestra los personajes con mayor altura por cada genero disponible en el archivo JSON
    Recibe una lista
    Devuelve un string por consola con los heroes con mayor altura por cada genero
    '''

    lista_generos = obtener_generos(lista)
    print(lista_generos)
    csv_result = []
    for genero in lista_generos:
        personaje_genero = obtener_mas_alto_por_genero(lista, genero)
        print('Genero: "{0}" - Nombre: {1} - Altura: {2}'.format(personaje_genero['gender'],
              personaje_genero['name'], personaje_genero['height']))
        csv_result.append(
            f'{personaje_genero["gender"]},{personaje_genero["name"]},{personaje_genero["height"]}\n')
    return csv_result


def final_ordenar_personajes_peso(lista: str) -> str:
    '''
    Función que lista los personajes ordenados por peso
    Recibe una lista
    Devuelve por consola los personajes 
    '''

    c_list = copy.deepcopy(lista)
    c_lista_ordenada = b_sort(c_list, 'mass')
    csv_result = []
    for el in c_lista_ordenada:
        print(f'Nombre: {el["name"]} - Peso: {el["mass"]}')
        csv_result.append(f'{el["name"]},{el["mass"]}\n')
    return csv_result


def final_buscador_personajes(lista: list, pattern: str) -> str:
    '''
    Función que busca heroes de la lista según la busqueda del usuario
    Recibe una lista de personajes y un patrón que ingrese el usuario
    Devuelve aquellos personajes donde encontró coincidencia
    '''

    print(f'Busqueda: {pattern}')
    csv_result = []
    for el in lista:
        if re.search(pattern, el['name'], re.IGNORECASE):
            print(f'> {el["name"]}')
            csv_result.append(f'{el["name"]}\n')
    return csv_result
