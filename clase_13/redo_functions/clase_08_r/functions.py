from functions_5 import *
import json
import re
import os
from functools import reduce


def imprimir_menu_desafio_5() -> str:
    '''
    Funcion que imprime el menu de la aplicación.
    '''
    imprimir_dato('''
\n[A] Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M\n\
[B] Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F\n\
[C] Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n\
[D] Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n\
[E] Recorrer la lista y determinar cuál es el superhéroe más bajo de género M\n\
[F] Recorrer la lista y determinar cuál es el superhéroe más bajo de género F\n\
[G] Recorrer la lista y determinar la altura promedio de los  superhéroes de género M\n\
[H] Recorrer la lista y determinar la altura promedio de los  superhéroes de género F\n\
[I] Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n\
[J] Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n\
[K] Determinar cuántos superhéroes tienen cada tipo de inteligencia.\n\
[L] Listar todos los superhéroes agrupados por color de ojos.\n\
[M] Listar todos los superhéroes agrupados por color de pelo.\n\
[N] Listar todos los superhéroes agrupados por tipo de inteligencia\n\
[Z] Salir del programa\n\
''')


def stark_menu_principal_desafio_5() -> str:
    '''
    Funcion que toma la opcion elegida por el usuario del menu principal
    Valida y devuelve la respuesta de la opción elegida
    '''
    retorno = -1
    imprimir_menu_desafio_5()
    answer = input('\n> ')
    if (re.search('^[a-nA-NzZ]{1}$', answer)):
        return answer.upper()

    return retorno


def leer_archivo(file_name: str) -> list:
    '''
    Funcion que accede a un archivo (modo lectura) según el nombre de archivo que recibe
    Retorna la lista de heroes como lista que contiene diccionarios
    '''
    with open(file_name, 'r') as file:
        lista_heroes = json.load(file)
    return lista_heroes['heroes']


def leer_archivo_manual(file_name: str) -> list:
    with open(file_name, 'r') as file:
        result = file.read()

    keys = re.findall('"(.+)": "', result)
    values = re.findall('": "(.+)?"', result)

    temp_list = []
    temp_dict = {}
    for i in range(len(keys)):
        if not keys[i] in temp_dict:
            temp_dict[keys[i]] = values[i]
        elif keys[i] == keys[0]:
            temp_list.append(temp_dict)
            temp_dict = {}
            temp_dict[keys[i]] = values[i]
    temp_list.append(temp_dict)

    return temp_list


def guardar_archivo(file_name: str, content: str) -> str:
    '''
    Funcion que crea/sobreescribe un archivo en base al contenido que recibe
    Recibe un nombre de archivo y un contenido
    Devuelve la creación del archivo (o sobreescritura) con el contenido especificado
    '''
    retorno = False
    mensaje = f'Error al crear el archivo: {file_name}\nRevisar nombre y formato válido (.csv)'
    aux_path = '../clase_08_r/results/'

    if(re.search('[a-zA-Z]+\.csv$', file_name)):
        with open(f'{aux_path}{file_name}', 'w') as file:
            file.writelines(content)
        retorno = True
        mensaje = f'Se creó el archivo: {file_name}'

    print(mensaje)
    return retorno


def capitalizar_palabras(text: str) -> str:
    '''
    Funcion que capitaliza el string que reciba como parametro
    '''
    split_text = text.split(' ')
    retorno = False
    if len(split_text) >= 1 and len(text) > 1:
        retorno = ' '.join(list(map(lambda el: el.capitalize(), split_text)))
    return retorno


def obtener_nombre_capitalizado(heroe: dict) -> str:
    '''
    Funcion capitaliza el nombre de un heroe
    Recibe un heroe (dict)
    Devuelve un string con el nombre de dicho heroe capitalizado
    '''
    retorno = -1
    if type(heroe) == type({}) and heroe.get('nombre'):
        nombre_heroe = capitalizar_palabras(heroe['nombre'])
        retorno = f'Nombre: {nombre_heroe}'
    return retorno


def obtener_nombre_y_dato(heroe: dict, key: str) -> str:
    '''
    Funcion que formatea en un string el nombre del heroe y un dato adicional del mismo
    Recibe un heroe (dict) y una key del dato a obtener del heroe
    Devuelve un string con el nombre de dicho heroe, incluída la key
    '''
    retorno = -1
    nombre_heroe = obtener_nombre_capitalizado(heroe)
    if key in heroe:
        retorno = f'{nombre_heroe} | {key.capitalize()}: {heroe[key]}'
    return retorno


def es_genero(heroe: dict, gen: str) -> bool:
    '''
    Funcion que evalua si el héroe es del genero que reciba en "gen"
    Devuelve True en caso de ser positiva la evaluación o False en caso contrario
    '''
    retorno = False
    if (re.search('^[fFmM]{1}$|^[nbNB]{2}$', gen) and
            heroe['genero'] == gen.upper()):
        retorno = True
    return retorno


def stark_guardar_heroe_genero(lista_heroes: list, gen: str) -> bool:
    '''
    Funcion que evalua en una lista de heroes si coinciden con el genero recibido
    Recibe una lista de heroes y un genero a evaluar por cada uno
    Devuelve true en caso de poder exportar el resultado en un archivo. Caso contrario, False.
    '''
    os.system('cls')
    retorno = False
    lista_nombres = []

    if re.search('^[fFmM]{1}$', gen):
        genero_archivo = 'F' if gen.upper() == 'F' else 'M'
        for heroe in lista_heroes:
            if(es_genero(heroe, gen)):
                nombre_heroe = obtener_nombre_capitalizado(heroe)
                lista_nombres.append(f'{heroe["nombre"]},\n')
                imprimir_dato(nombre_heroe)

        retorno = guardar_archivo(
            f'heroes_{genero_archivo}.csv', lista_nombres)
    else:
        print('\n[ERROR] Genero incorrecto')
    return retorno


def primer_heroe_heroina(lista: list, gen: str) -> dict:
    retorno = -1
    if (re.search('^[fFmM]{1}$|^[nbNB]{2}$', gen)):
        retorno = list(
            filter(lambda el: el['genero'] == gen.upper(), lista))[0]

    return retorno


def calcular_min_genero(lista: list, key: str, gen: str) -> dict:
    '''
    Funcion que calcula el mínimo de un determinado valor de los heroes o heroínas (valores numericos)
    Recibe una lista de heroes, una key para indicar el dato del heroe/heroína a evaluar para calcular el minimo
    Devuelve el heroe o heroína con la evaluación mínima del dato deseado a evaluar
    '''

    retorno = -1
    if (lista and re.search('^[fFmM]{1}$|^[nbNB]{2}$', gen)):
        temp_list = list(filter(lambda el: el['genero'] == gen.upper(), lista))
        temp_list.sort(key=lambda el: float(el[key]))
        retorno = temp_list[0]
    return retorno


def calcular_max_genero(lista: list, key: str, gen: str) -> dict:
    '''
    Funcion que calcula el máximo de un determinado valor de los heroes o heroínas (valores numericos)
    Recibe una lista de heroes, una key para indicar el dato del heroe/heroína a evaluar para calcular el máximo
    Devuelve el heroe o heroína con la evaluación mínima del dato deseado a evaluar
    '''

    retorno = -1
    c_list = lista.copy()
    if (c_list and re.search('^[fFmM]{1}$|^[nbNB]{2}$', gen)):
        temp_list = list(filter(lambda el: el['genero'] == gen.upper(), lista))
        temp_list.sort(key=lambda el: float(el[key]), reverse=True)
        retorno = temp_list[0]
    return retorno


def calcular_max_min_dato_genero(lista: list, tipo: str, key: str, gen: str) -> dict:
    '''
    Funcion que calcula el máximo/mínimo de un determinado valor de los heroes (valores numericos) por su género
    Recibe una lista de heroes (de tipo list), un "tipo" para saber si calcular min o max, una key de tipo str para indicar el tipo de dato a evaluar para calcular el máximo y el género deseado
    Devuelve el heroe/heroína con la evaluación mínima o máxima del dato deseado a evaluar
    '''
    retorno = -1
    if (lista and (tipo == 'max' or tipo == 'min')):
        if(tipo == 'max'):
            retorno = calcular_max_genero(lista, key, gen)
        elif(tipo == 'min'):
            retorno = calcular_min_genero(lista, key, gen)
    return retorno


def stark_calcular_imprimir_heroe(lista: list, tipo: str, key: str, gen: str) -> str:
    '''
    Funcion que calcula el máximo/mínimo de un determinado valor de los heroes (valores numericos) con el género especificado
    Recibe una lista de heroes, un "tipo" para saber si calcular min o max, una key que indique el dato a evaluar y el género de cada heroe
    Devuelve por consola el nombre y el dato especificado del héroe con la evaluación min/max (segun corresponda)
    '''
    os.system('cls')
    retorno = False
    if (lista and (tipo == 'max' or tipo == 'min') and
            re.search('^[fFmM]{1}$|^[nbNB]{2}$', gen)):
        if(tipo == 'max'):
            temp = calcular_max_min_dato_genero(lista, 'max', key, gen)
            temp = obtener_nombre_y_dato(temp, key)
            retorno = 'Mayor {0}: {1}'.format(key, temp)
        else:
            temp = calcular_max_min_dato_genero(lista, 'min', key, gen)
            temp = obtener_nombre_y_dato(temp, key)
            retorno = 'Menor {0}: {1}'.format(key, temp)
        imprimir_dato(retorno)
        retorno = guardar_archivo('heroes_{0}_{1}_{2}.csv'.format(
            tipo, key, gen.upper()), retorno)
    else:
        print(f'\n[ERROR] Verifique los valores:\n• {tipo}\n• {gen}')
    return retorno


def sumar_dato_heroe_genero(lista: list, key: str, gen: str) -> int:
    '''
    Funcion que suma un determinado valor de cada heroes (valores numericos) por el genero especificado
    Recibe una lista de heroes, una key para sumar el valor de cada heroe y un genero
    Devuelve la suma del dato especificado por cada héroe
    '''
    retorno = -1
    if lista and type(lista[0]) == type({}):
        retorno = reduce(
            lambda x, y: x + float(y[key]) if y['genero'] == gen.upper() else x, lista, 0)
    return retorno


def cantidad_heroes_genero(lista: list, gen: str) -> int:
    '''
    Función que itera sobre la lista de heroes y muestra la cantidad de heroes por el genero especificado
    Recibe una lista de heroes y un genero
    Devuelve la suma contadora del genero
    '''
    return reduce(lambda x, y: x + 1 if y['genero'] == gen.upper() else x, lista, 0)


def calcular_promedio_genero(lista: list, key: str, gen: str) -> int:
    '''
    Funcion que calcula promedio en base a un dato específico en los heroes y su genero
    Recibe una lista de heroes, una key del heroe y un genero
    Devuelve el promedio de dicho valor pasado como key
    '''
    dato_sumado = sumar_dato_heroe_genero(lista, key, gen)
    qty_heroes = cantidad_heroes_genero(lista, gen)
    promedio = dividir(dato_sumado, qty_heroes)
    return promedio


def stark_calcular_imprimir_guardar_promedio_altura_genero(lista: list, gen: str) -> str:
    '''
    Funcion que calcula el promedio de alturas de los heroes
    Recibe una lista de heroes (de tipo list)
    Devuelve el promedio de altura de los mismos
    '''
    os.system('cls')
    retorno = -1
    gen = gen.upper()
    if re.search('^[fFmM]{1}$', gen):
        genero_archivo = 'M' if gen == 'M' else 'F'

        if lista:
            promedio_altura = calcular_promedio_genero(lista, 'altura', gen)
            retorno = 'Altura promedio genero {0}: {1:.2f}'.format(
                gen, promedio_altura)
        else:
            retorno = 'Error: Lista de heroes vacia.'
        imprimir_dato(retorno)

        retorno = guardar_archivo(
            f'heroes_promedio_altura_{genero_archivo}.csv', retorno)
    else:
        print('\n[ERROR] Genero incorrecto')
    return retorno


def calcular_cantidad_tipo(lista: list, key: str) -> dict:
    '''
    Funcion que calcula la cantidad de keys que reciba en una lista de heroes
    Recibe una lista de heroes y una key para evaluar y acumular el dato
    Devuelve un diccionario con los resultaos
    '''

    temp_dict = {}
    if lista:
        for heroe in lista:
            if heroe.get(key):
                key_value = capitalizar_palabras(heroe.get(key))
                if key_value in temp_dict:
                    temp_dict[key_value] += 1
                else:
                    temp_dict[key_value] = 1
    else:
        temp_dict = {'Error': 'La lista se encuentra vacía'}
    return temp_dict


def guardar_cantidad_heroes_tipo(dict_datos: dict, key: str) -> bool:
    '''
    Funcion que exporta en un archivo los datos del diccionario recibido con la cantidad de tipo de un determinado dato en el listado de heroes
    Recibe un diccionario y una key para parsear los resultados en un csv
    Devuelve la exportación de un archivo .csv
    '''
    retorno = False
    results = []
    for dict_key in dict_datos:
        content = 'Caracteristica: {0} {1} - Cantidad de heroes: {2},\n'.format(
            key,
            dict_key,
            dict_datos[dict_key])
        results.append(content)

    retorno = guardar_archivo(
        f'heroes_cantidad_{key}.csv', results)

    return retorno


def stark_calcular_cantidad_por_tipo(lista: list, key: str) -> bool:
    '''
    Funcion que exporta una lista con datos calculados a partir de una key determinada por cada heroe
    Recibe una lista de heroes y una key para calcular
    Retorna un bool en caso de un resultado satisfactorio, o False en caso contrario
    '''
    os.system('cls')
    retorno = False
    dict_datos = calcular_cantidad_tipo(lista, key)
    retorno = guardar_cantidad_heroes_tipo(dict_datos, key)
    return retorno


def obtener_lista_de_tipos(lista: list, key: str) -> tuple:
    '''
    Funcion que genera una lista de todos los tipos de datos de una key en una lista de heroes
    Recibe una lista de heroes y una key para obtener los valores de cada heroe
    Devuelve una lista con todos los valores disponibles de dicha key
    '''
    return set(map(lambda el: capitalizar_palabras(el[key]) or 'N/A', lista))


def normalizar_dato(dato_heroe: str, default: str = 'N/A') -> str:
    '''
    Función que recibe un tipo de dato de un heroe y lo retorna sin modificacion.
    En caso de estar vacío, retornará el parámetro default recibido como argumento
    '''
    if not dato_heroe:
        dato_heroe = default
    return dato_heroe


def normalizar_heroe(heroe: dict, key: str) -> str:
    '''
    Funcion que capitaliza el valor de la key del heroe y el nombre del mismo
    Recibe un heroe y una key para buscarla en el heroe
    Retorna el heroe con los datos normalizados y capitalizados
    '''
    if not re.search('N/A', heroe[key]):
        heroe[key] = normalizar_dato(capitalizar_palabras(heroe[key]))
    heroe['nombre'] = capitalizar_palabras(heroe['nombre'])
    return heroe


def obtener_heroes_por_tipo(lista: list, set_datos: set, key: str) -> dict:
    '''
    Funcion que genera un diccionario donde cada key es el valor del tipo de dato a evaluar (por ejemplo los colores de ojos) y el valor de cada key serán los nombres de cada heroe con ese tipo de dato que coincida
    Recibe una lista de heroes, un set de datos y una key para evaluar
    Devuelve un diccionario
    '''

    dict_temp = {}
    for dato in set_datos:
        for heroe in lista:
            dato_heroe = normalizar_heroe(heroe, key)

            if dato in dict_temp and dato_heroe[key] == dato:
                dict_temp[dato].append(dato_heroe['nombre'])
            elif dato_heroe[key] == dato:
                dict_temp[dato] = [dato_heroe['nombre']]

    return dict_temp


def guardar_heroes_por_tipo(dict_tipos: dict, key: str) -> bool:
    '''
    Funcion que exporta un archivo con los nombres de los heroes en base a la key especificada
    Recibe un diccionario con los tipos de datos (hecho previamente) y una key para evaluar
    Devuelve un archivo csv con los resultados (retorna True en caso positivo, False en caso contrario)
    '''
    retorno = False
    results = []
    for tipo in dict_tipos:
        results.append(f'{key} {tipo}: {" | ".join(dict_tipos[tipo])},\n')

    retorno = guardar_archivo(f'heroes_segun_{key}.csv', results)

    return retorno


def stark_listar_heroes_por_dato(lista: list, key: str) -> bool:
    '''
    Funcion que genera un archivo con los nombres de los heroes en base a una key recibida. Reutiliza tres funciones
    Recibe una lista de heroes y una key para evaluar
    Retorna True en caso de haber logrado la exportación, o False en caso contrario
    '''
    os.system('cls')
    retorno = False
    set_datos = obtener_lista_de_tipos(lista, key)
    dict_tipos = obtener_heroes_por_tipo(lista, set_datos, key)
    retorno = guardar_heroes_por_tipo(dict_tipos, key)

    return retorno
