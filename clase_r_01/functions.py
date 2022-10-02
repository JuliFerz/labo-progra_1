import json
import re


def cargar_json(path: str) -> list:
    with open(path, 'r') as file:
        dict_json = json.load(file)
    return dict_json['paulina']


def mostrar(lista: list):
    print('\n')
    for el in lista:
        print('{0} - {1} - {2}'
              .format(el['views'], el['length'], el['title']))
    print('\n')


def buscar_min_max(lista: list, key: str, order: str) -> int:
    '''
    Busca un minimo de un determinado elemento (key) de una lista de diccionarios
    Recibe una lista de diccionarios y una key para buscar el minimo
    Devuelve el índice de el minimo elemento de la lista o -1 en caso de error
    '''
    retorno = -1
    if len(lista) > 0:
        i_min_max = 0
        """ i = 0
        for el in lista:
            if (el[key] < lista[i_min_max]):
                i_min_max = i
            i += 1 """
        for i in range(len(lista)):
            if((order == 'down' and lista[i][key] < lista[i_min_max][key]) or
               (order == 'up' and lista[i][key] > lista[i_min_max][key])):
                i_min_max = i
        retorno = i_min_max
    return retorno


def n_sort(lista: list, key: str, order: str = 'up') -> list:
    lista_ordenada = lista.copy()
    """ while(len(lista_a_ordenar > 0)):
        index_min_max = buscar_min_max(lista_a_ordenar, key, order)
        lista_ordenada.append(lista_a_ordenar.pop(index_min_max)) """
    for i in range(len(lista_ordenada)):
        index_min_max = buscar_min_max(lista_ordenada[i:], key, order) + i
        # ☝️ OJO! Es necesario sumarle i porque sino esta variable va a devolver un indice
        # que pertenece a la "sub lista" de lista_ordenada[i:], y este indice NO va a coincidir
        # con el indice de la lista original (sin el slice)
        lista_ordenada[i], lista_ordenada[index_min_max] = lista_ordenada[index_min_max], lista_ordenada[i]
    return lista_ordenada


def buscar(lista: list, patron: str):
    print('\n')
    for el in lista:
        match = re.search(patron, el['title'], re.IGNORECASE)
        if (match):
            # resaltar en color la palabra que matcheó (g0d)
            titulo = el['title']
            palabra = '\033[0;31m' + match.group(0) + '\033[0;m'
            titulo = titulo.replace(match.group(0), palabra)
            print('{0} - {1} - {2}'
                  .format(el['views'], el['length'], titulo))
    print('\n')


def exportar_csv(lista: str, path: str):
    with open(path, 'w') as file:
        for el in lista:
            file.write('{0},{1},{2}\n'.format(
                el['views'], el['length'], el['title']))
