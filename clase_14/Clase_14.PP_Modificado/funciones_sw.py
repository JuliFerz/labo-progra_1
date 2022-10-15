# MIT License
#
# Copyright (c) 2022 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import json
import os
import re
from functools import reduce
from copy import deepcopy
from random import shuffle


# ? ARCHIVOS

def cargar_json(path: str) -> list[dict]:
    """
    It opens the file at the path specified, loads the json data into a dictionary, and returns the
    value of the key "results" in that dictionary

    :param path: str
    :type path: str
    :return: A list of dictionaries.
    """
    with open(path, "r") as archivo:
        dic_archivo = json.load(archivo)
    return dic_archivo["results"]


def exportar_a_csv(lista_personajes: list[dict], ruta_archivo: str) -> None:
    """
    It takes a list of dictionaries and a file path, and writes the information from the dictionaries to
    the file

    :param lista_personajes: list[dict]
    :type lista_personajes: list[dict]
    :param ruta_archivo: str
    :type ruta_archivo: str
    """
    with open(ruta_archivo, "w") as archivo:
        for personaje in lista_personajes:
            archivo.write(f'{obtener_info_csv(personaje)}\n')
        print(f'Archivo creado en {ruta_archivo}')

#! ARCHIVOS


# ? NUEVO
def castear_keys(lista_pj: list[dict], key: str):
    '''
    It recieve a list of dictionaries and key to cast the value

    :param list_pj: list[dict]
    :param key: str
    :return list_pj: list[dict]
    '''
    list(map(lambda el: el.update({key: int(el[key])}), lista_pj))
    return lista_pj


def obtener_genero(personaje: dict) -> str:
    '''
    It takes a dict and return his gender. If it not exist in the first level, it will be created and returned

    :param personaje: dict
    :return gender: str
    '''
    if personaje.get('gender'):
        gender = personaje['gender']
    else:
        for el in personaje:
            if el == 'data':
                gender = personaje[el]['gender']
        personaje.update({'gender': gender})
    return gender


def desordenar_lista(lista: list) -> list:
    '''
    It make a deep copy from a list and shuffle his elements. It returns the last element of this new random list

    :param lista: list
    :return c_lista: deepcopy(lista)[-1]
    '''
    c_lista = deepcopy(lista)
    shuffle(c_lista)
    return c_lista[-1]


#! NUEVO


# ? MOSTRAR

def mostrar(personajes: list[dict], key: str = 'mass') -> None:
    """
    It takes a list of dictionaries as input, and prints the name and the value of the key
    that matches the string for each dictionary in the list

    :param personajes: list[dict]
    :type personajes: list[dict]
    """
    header = f'#### Ordenados por {key.capitalize()} ####'
    print(header)
    for personaje in personajes:
        mensaje = obtener_info(personaje)
        print(f'• {mensaje}')
    print('#' * len(header))


#! MOSTRAR


# ? MENU

def imprimir_menu() -> None:
    mensaje = """
    1 - Listar los personajes ordenados por altura
    2 - Mostrar el personaje mas alto de cada genero
    3 - Ordenar los personajes por peso
    4 - Buscar un personaje 🔍
    5 - Filtrar personajes Femeninos
    6 - Filtrar personajes Masculinos
    7 - Filtrar personajes Sin Genero
    8 - Desordenar la lista de manera random y mostrar el ultimo de la lista
    9 - Exportar lista personajes a CSV
    10 - Salir
    """
    print(mensaje)

#! MENU


# ? BUSQUEDAS

def buscar_indice_max(lista_pjs: list, clave: str) -> int:
    """
    It takes a list of dictionaries and a key, and returns the index of the dictionary in the list that
    has the highest value for that key

    :param lista_pjs: list
    :type lista_pjs: list
    :param clave: str
    :type clave: str
    :return: The index of the maximum value of the key in the list of dictionaries.
    """
    i_max = reduce(lambda x, y:
                   y if int(lista_pjs[y][clave]) > int(lista_pjs[x][clave]) else x, range(len(lista_pjs)), 0)
    return i_max


def obtener_fragmento_palabra(match_resul: str, palabra_original: str) -> str:
    """
    It takes a match object and the original word, and returns the fragment of the original word that
    matched the pattern

    :param match_resul: The result of the match
    :type match_resul: str
    :param palabra_original: The original word that you want to find the fragment of
    :type palabra_original: str
    :return: the substring of the original word that matches the pattern.
    """
    span_index = match_resul.span()
    result = palabra_original[span_index[0]: span_index[1]]
    return result


def buscar_personaje_en_lista(personajes: list[dict], nombre: str) -> None:
    """
    It searches for a character in a list of characters
    and prints the information of the character if
    it is found

    :param personajes: list[dict]
    :type personajes: list[dict]
    :param nombre: str
    :type nombre: str
    :return: None
    """
    se_encontro = False
    for personaje in personajes:
        resultado_match = re.search(nombre, personaje["name"], re.IGNORECASE)
        if resultado_match:
            se_encontro = True
            message = obtener_info(personaje)
            print(message)
    if not se_encontro:
        print("No se encontro coincidencias\n")
    return None

#! BUSQUEDAS


# ? LISTAR

def listar_por_genero(personajes: list[dict], genero: str) -> list[dict]:
    """
    It takes a list of dictionaries and a string, and returns a list of dictionaries

    :param personajes: list[dict]
    :type personajes: list[dict]
    :param genero: str
    :type genero: str
    :return: A list of dictionaries
    """

    lista_mismo_genero = list(
        filter(lambda el: obtener_genero(el) == genero, personajes))
    return lista_mismo_genero


def listar_max_por_genero(lista_personajes: list, genero: str, clave: str = "height") -> list[dict]:
    """
    It takes a list of dictionaries, a string, and a string, and returns a list of dictionaries

    :param lista_personajes: list
    :type lista_personajes: list
    :param genero: str
    :type genero: str
    :param clave: str = "height", defaults to height
    :type clave: str (optional)
    :return: A list of dictionaries.
    """
    lista_seleccionado = []
    lista_max = listar_por_genero(lista_personajes, genero)
    seleccionado = lista_max[buscar_indice_max(lista_max, clave)]
    lista_seleccionado.append(seleccionado)
    return lista_seleccionado

#! LISTAR


# ? ORDENAR

def ordenar_lista(personajes: list[dict], clave: str) -> list[dict]:
    '''
    Ordena la lista de personajes en relacion al indice maximo y la clave que se le pase
    Recibe la lista de personajes y un str que representa la clave
    Devuelve una lista con los personajes ordenados
    '''
    castear_keys(personajes, clave)
    personajes.sort(key=lambda el: el[clave], reverse=True)
    return personajes


#! ORDENAR


# ? INFO

def obtener_info(personaje: dict) -> str:
    """
    It takes a dictionary as an argument and returns a string

    :param personaje: dict
    :type personaje: dict
    :return: A string with the name, height, mass and gender of the character.
    """
    gender = obtener_genero(personaje)
    message = f'Nombre: {personaje["name"]} | Altura: {personaje["height"]} | Peso: {personaje["mass"]} | Genero: {gender}'
    return message


def obtener_info_csv(personaje: dict) -> str:
    """
    It takes a dictionary as an argument and returns a string

    :param personaje: dict
    :type personaje: dict
    :return: A string
    """
    message = f'{personaje["name"]},{personaje["height"]},{personaje["mass"]},{personaje["gender"]}'
    return message

#! INFO


# ? VALIDACION

def validar_respuesta(respuesta: str, patron_regex: str):
    """
    If the response is not empty and matches the regular expression, return the response, otherwise
    return -1

    :param respuesta: The user's input
    :param patron_regex: This is the regular expression that will be used to validate the user's input
    :return: the value of the variable respuesta.
    """
    if respuesta:
        if re.match(patron_regex, respuesta):
            return respuesta
    return -1

#! VALIDACION


# ? SISTEMA

def continuar_consola() -> None:
    """
    It clears the console and waits for the user to press a key
    """
    _ = input('\nPresione una tecla para continuar...')
    os.system('cls')

#! SISTEMA
