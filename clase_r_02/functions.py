import re
import json
import copy
import os


def imprimir_menu():
    print('''
1. Listar los últimos N pokemones.
2. Ordenar y Listar pokemones por poder.
3. Ordenar y Listar pokemones por ID.
4. Calcular pokemones según cantidad promedio
5. Buscar pokemones por tipo
6. Exportar a csv (puntos: 1 al 4)
7. Salir.
''')


def error_mess(var='', sec_var=''):
    '''
    Funcion que imprime un mensaje de error genérico
    Recibe una variable (opcional) para mostrar en el mensaje
    Devuelve el mensaje de error
    '''
    os.system('cls')
    print('\n[ERROR]: Revise los datos de entrada')
    print(f'\t> Input: "{var}"') if var else ''
    print(f'\t> Input: "{sec_var}"') if sec_var else ''


def parse_json(path: str) -> list:
    '''
    Funcion que parsea un json para que sea entendible en python
    '''
    with open(path, 'r') as file:
        lista_pokedex = json.load(file)
    return lista_pokedex['pokemones']


def guardar_csv(path: str, content: str) -> str:
    '''
    Función que guarda el resultado pasado por parámetro en un archivo .csv
    Recibe una dirección y un contenido para guardar allí
    Devuelve la creación/modificación del archivo
    '''
    os.system('cls')
    aux_path = '../clase_r_02/results/'
    with open(f'{aux_path}{path}', 'w') as file:
        archivo = file.writelines(content)


def validar_numerico(var: str) -> bool:
    '''
    Función que valida si un string puede ser un numero entero
    Recibe una variable string para evaliar si puede ser entero
    En caso positivo, retoran True, caso contrario False
    '''
    retorno = False
    if not re.search('[.,a-zA-Z_()]+', var):
        retorno = True
    return retorno


def final_listar_pokemones(lista: list, qty: int) -> str:
    '''
    Funcion que lista n cantidad de pokemones (siendo "n" elección del usuario)
    Recibe una lista de pokemones y una cantidad a mostrar
    Devuelve un listado de los pokemones
    '''
    os.system('cls')
    retorno = False
    if validar_numerico(qty):
        qty = int(qty)
        if ((qty <= len(lista) and qty > 0) and lista):
            retorno = []
            for poke in lista[:qty]:
                print(
                    f'Nombre: {poke["nombre"]} - Tipo: {poke["tipo"]} - Poder: {poke["poder"]}')
                retorno.append(
                    f'{poke["id"]},{poke["nombre"]},{poke["poder"]}\n')
        else:
            error_mess(qty)
    return retorno


def b_sort(lista: list, key: str, modo: str) -> list:
    '''
    Función que ordena una lista recibida teniendo en cuenta una key (dato numerico) y un modo (asc o desc)
    Recibe una lista, una key (dato numerico de la lista) y un modo
    Devuelve la lista ordenada
    '''
    for i in range(len(lista)):
        for j in range(len(lista)):
            if modo == 'desc':
                if lista[i][key] > lista[j][key]:
                    lista[j], lista[i] = lista[i], lista[j]
            else:
                if lista[i][key] < lista[j][key]:
                    lista[j], lista[i] = lista[i], lista[j]
    return lista


def final_ordenar_listar_poder(lista: list, modo: str) -> str:
    '''
    Función que ordena la lista de pokemones según poder. El resultado será la lista ordenada según haya elegido el usuario (ascendente o descendente)
    Recibe una lista y un modo
    '''
    os.system('cls')
    c_list = copy.deepcopy(lista)
    retorno = False
    if lista and re.search('^desc$|^asc$', modo, re.IGNORECASE):
        sorted_list = b_sort(c_list, 'poder', modo)
        retorno = []
        for el in sorted_list:
            print(
                f'Nombre: {el["nombre"]} - Tipo: {el["tipo"]} - Poder: {el["poder"]}')
            retorno.append(f'{el["id"]},{el["nombre"]},{el["poder"]}\n')

    else:
        error_mess(modo)
    return retorno


def final_ordenar_listar_id(lista: list, modo: str) -> str:
    '''
    Función que ordena la lista de pokemones según poder. El resultado será la lista ordenada según haya elegido el usuario (ascendente o descendente)
    Recibe una lista y un modo
    '''
    os.system('cls')
    c_list = copy.deepcopy(lista)
    retorno = False
    if lista and re.search('^desc$|^asc$', modo, re.IGNORECASE):
        sorted_list = b_sort(c_list, 'id', modo)
        retorno = []
        for el in sorted_list:
            print(
                f'Nombre: {el["nombre"]} - Tipo: {el["tipo"]} - Id: {el["id"]}')
            retorno.append(f'{el["id"]},{el["nombre"]},{el["poder"]}\n')
    else:
        error_mess(modo)
    return retorno


def suma_y_cantidad_elem_lista(lista: list, key: str) -> list:
    '''
    Función que suma la cantidad de elementos que hay en una key lista, más la cantidad de pokemones que tienen esa key
    Recibe una lista y una key para sumar la cantidad de elementos que tenga
    Devuelve una lista con: [suma de cant. de key, contador]
    '''
    acumulador = 0
    contador = 0
    retorno = []
    for el in lista:
        contador += 1
        for i in range(len(el[key])):
            acumulador += 1
            retorno = [acumulador, contador]
    return retorno


def dividir(dividendo: int, divisor: int) -> float:
    '''
    funcion que divide
    Recibe un dividendo  y un divisor.
    Si el divisor es 0, retorna -1. Caso contrario, devuelve un flotante con la división
    '''
    retorno = -1
    if divisor > 0:
        retorno = dividendo / divisor
    return retorno


def final_promedio_pokemones(lista: list, key: str, modo: str) -> str:
    '''
    Función que muestra por pantalla una lista de pokemones cuya key sea superior o inferior (a eleccion del user) del promedio de dicha key
    Recibe una lista, una key para evaluar y un modo para saber si mostrar los menores al promedio, o los mayores
    Devuelve por pantalla dicho resultado
    '''
    os.system('cls')
    retorno = False
    key = key.lower()
    if lista and type(lista[0][key] == type([])
                      and re.search('^menor$|^mayor$', modo, re.IGNORECASE)):
        modo = modo.lower()
        retorno = []
        lista_el = suma_y_cantidad_elem_lista(lista, key)
        promedio_el = dividir(lista_el[0], lista_el[1])
        print(f'PROMEDIO: {promedio_el}')
        for el in lista:
            if modo == 'menor' and len(el[key]) < promedio_el:
                print(
                    f'Nombre: {el["nombre"]} - Tipo: {el["tipo"]} - {key}: {el[key]}')
            elif modo == 'mayor' and len(el[key]) > promedio_el:
                print(
                    f'Nombre: {el["nombre"]} - Tipo: {el["tipo"]} - {key}: {el[key]}')
            retorno.append(f'{el["id"]},{key},{el["nombre"]}\n')

    else:
        error_mess(key, modo)
    return retorno


def obtener_lista_tipos(lista: list, key: str) -> set:
    '''
    Función que obtiene una lista de los elementos disponibles en el json de pokedex
    Recibe una lista y una key
    Devuelve un set con los tipos que tienen los pokemones
    '''
    retorno = set([])
    for el in lista:
        for tipo in el[key]:
            retorno.add(tipo)
    return retorno


def buscar_tipo_pokemon(lista: list, tipo: str) -> bool:
    '''
    Funcion que busca los pokemones que tengan un tipo en particular (elegido por el usuario)
    Recibe una lista y un tipo
    Devuelve True en caso de que el tipo se encuentre en los pokemones, o false en caso contrario
    '''

    tipo_pokemones = obtener_lista_tipos(lista, 'tipo')

    for tipo_p in tipo_pokemones:
        if not re.search(tipo, tipo_p, re.IGNORECASE):
            retorno = False
        else:
            retorno = True
            break
    return retorno


def final_mostrar_pokemones_tipo(lista: list, tipo: str) -> str:
    '''
    Funcion que muestra los pokemones que tengan un tipo en particular (elegido por el usuario)
    Recibe una lista y un tipo
    Devuelve los pokemones que hayan resultado de dicha busqueda. En caso de falla, devuelve un error
    '''
    os.system('cls')
    retorno = False
    tiene_tipo = buscar_tipo_pokemon(lista, tipo)
    if tiene_tipo:
        retorno = []
        for poke in lista:
            for tipos in poke['tipo']:
                if re.search(tipo, tipos, re.IGNORECASE):
                    print(f'Nombre: {poke["nombre"]} - Tipo: {poke["tipo"]}')
                retorno.append(
                    f'{poke["id"]},{poke["nombre"]},{poke["poder"]}\n')
    else:
        error_mess(tipo)
    return retorno
