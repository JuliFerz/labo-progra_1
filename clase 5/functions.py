def stark_normalizar_datos(lista: list, clave: str, tipo: str) -> list:
    '''
    Funcion que castea datos de un elemento de una lista que contiene diccionarios
    Recibe una lista de superheroes (type: list)
    Devuelve una lista con las keys de la lista original casteados en numéricos (int o float)
    '''
    if len(lista) < 1:
        return 'Error: Lista de heroes vacía'
    else:
        temp_list = []
        for elemento in lista:
            temp_dict = {}
            if (elemento and tipo == 'int' and type(elemento[clave]) != type(int())):
                temp_dict = elemento
                temp_dict[clave] = int(temp_dict[clave])
                temp_list.append(temp_dict)
            elif (elemento and tipo == 'float' and type(elemento[clave]) != type(float())):
                temp_dict = elemento
                temp_dict[clave] = float(temp_dict[clave])
                temp_list.append(temp_dict)
            else:
                temp_dict = elemento
                temp_list.append(temp_dict)
        # print('Datos normalizados')
    return temp_list


def obtener_nombre(heroe: dict) -> str:
    '''
    Funcion que devuelve el nombre de cada heroe
    Recibe un heroe (de tipo: diccionario)
    Devuelve un string formateado con el nombre del heroe (en caso de no existir, muestra un mensaje pre-seteado)
    '''
    if heroe:
        nombre_heroe = heroe['nombre']
        mensaje = 'Nombre: {0}'.format(nombre_heroe)
    return mensaje


def imprimir_dato(dato: str) -> str:
    '''
    Funcion que devuelve el un dato en un print
    Recibe un dato (de tipo: string)
    No tiene retorno. Devuelve simplemente un print con el dato
    '''
    print(dato)


def stark_imprimir_nombres_heroes(lista: list) -> str:
    '''
    Funcion que muestra por consola los nombres de los heroes
    Recibe una lista (de tipo: list) con diccionarios dentro
    Devuelve por consola el nombre de cada heroe
    '''

    if (lista):
        for elemento in lista:
            imprimir_dato(obtener_nombre(elemento))
    else:
        return -1


def obtener_nombre_y_dato(heroe: dict, key: str) -> str:
    '''
    Funcion que muestra el nombre del heroe y un dato a elección del mismo
    Recibe un heroe de tipo: dict (toma el nombre de otra funcion) y una key (de tipo str) que será el dato que queremos obtener del diccionario del heroe
    Devuelve por consola el nombre del heroe y el dato deseado a obtener
    '''
    nombre_heroe = obtener_nombre(heroe)
    dato_heroe = heroe[key]
    return '{0} | {1}: {2}'.format(nombre_heroe, key, dato_heroe)


def stark_imprimir_nombres_alturas(lista: list) -> str:
    '''
    Funcion que muestra el nombre de cada heroe y la altura de cada uno
    Recibe una lista de heroes (de tipo list)
    Devuelve por consola el nombre de cada heroe de la lista y la altura de cada uno
    '''
    if (lista):
        for elemento in lista:
            imprimir_dato(obtener_nombre_y_dato(elemento, 'altura'))
    else:
        return -1


def calcular_max(lista: list, key: str) -> dict:
    '''
    Funcion que calcula el máximo de un determinado valor de los heroes (valores numericos)
    Recibe una lista de heroes (de tipo list) y una key de tipo str para indicar el tipo de dato a evaluar para calcular el máximo
    Devuelve el heroe con la evaluación máxima del dato deseado a evaluar
    '''
    if (lista):

        max_elem = lista[0]
        for elemento in lista:
            if elemento[key] > max_elem[key]:
                max_elem = elemento
        return max_elem
    else:
        return -1


def calcular_min(lista: list, key: str) -> dict:
    '''
    Funcion que calcula el mínimo de un determinado valor de los heroes (valores numericos)
    Recibe una lista de heroes (de tipo list) y una key de tipo str para indicar el tipo de dato a evaluar para calcular el máximo
    Devuelve el heroe con la evaluación mínima del dato deseado a evaluar
    '''
    if (lista):
        min_elem = lista[0]
        for elemento in lista:
            if elemento[key] < min_elem[key]:
                min_elem = elemento
        return min_elem
    else:
        return -1


def calcular_max_min_dato(lista: list, tipo: str, key: str) -> dict:
    '''
    Funcion que calcula el máximo/mínimo de un determinado valor de los heroes (valores numericos)
    Recibe una lista de heroes (de tipo list), un "tipo" para saber si calcular min o max, y una key de tipo str para indicar el tipo de dato a evaluar para calcular el máximo
    Devuelve el heroe con la evaluación mínima o máxima del dato deseado a evaluar
    '''
    retorno = -1
    if (lista and (tipo == 'max' or tipo == 'min')):
        if(tipo == 'max'):
            retorno = calcular_max(lista, key)
        elif(tipo == 'min'):
            retorno = calcular_min(lista, key)
    return retorno


def stark_calcular_imprimir_heroe(lista: list, tipo: str, key: str) -> str:
    '''
    Funcion que calcula el máximo/mínimo de un determinado valor de los heroes (valores numericos)
    Recibe una lista de heroes (de tipo list), un "tipo" para saber si calcular min o max, y una key de tipo str para indicar el tipo de dato a evaluar para calcular el máximo
    Devuelve por consola el nombre y el dato especificado del héroe con la evaluación min/max (segun corresponda)
    '''
    retorno = -1
    if (lista and (tipo == 'max' or tipo == 'min')):
        if(tipo == 'max'):
            temp = calcular_max(lista, key)
            temp = obtener_nombre_y_dato(temp, key)
            retorno = 'Mayor {0}: {1}'.format(key, temp)
        elif(tipo == 'min'):
            temp = calcular_min(lista, key)
            temp = obtener_nombre_y_dato(temp, key)
            retorno = 'Menor {0}: {1}'.format(key, temp)
    return imprimir_dato(retorno)


def sumar_dato_heroe(lista: list, key: str) -> int:
    '''
    Funcion que suma un determinado valor de cada heroes (valores numericos)
    Recibe una lista de heroes (de tipo list) y una key de tipo string para tomar el valor de cada heroe y sumarlo
    Devuelve la suma del dato especificado por cada héroe (tipo int)
    '''
    suma = 0
    for el in lista:
        if (type(el) == type({}) and el):
            suma += el[key]

    return suma


def dividir(dividendo: int, divisor: int) -> int:
    '''
    Funcion que divide dos numeros
    Recibe una dividendo y un divisor (de tipo int)
    Devuelve la división de ambos numeros
    '''
    resultado = 0
    if divisor != 0:
        resultado = dividendo / divisor
    return resultado


def calcular_promedio(lista: list, key: str) -> int:
    '''
    Funcion que calcula promedio en base a un dato específico en los heroes
    Recibe una lista de heroes (de tipo list) y una key (de tipo str)
    Devuelve el promedio de la suma de ese valor
    '''
    dato_sumado = sumar_dato_heroe(lista, key)
    promedio = dividir(dato_sumado, len(lista))
    return promedio


def stark_calcular_imprimir_promedio_altura(lista: list) -> int:
    '''
    Funcion que calcula el promedio de alturas de los heroes
    Recibe una lista de heroes (de tipo list)
    Devuelve el promedio de altura de los mismos
    '''
    retorno = -1
    if lista:
        retorno = calcular_promedio(lista, 'altura')
    return imprimir_dato('Promedio de alturas: {0:.2f}'.format(retorno))


def imprimir_menu() -> str:
    '''
    Funcion que imprime el menu
    '''
    imprimir_dato('\n[1]: Traer el héroe más alto\n\
[2]: Traer el héroe más bajo\n\
[3]: Traer el promedio de alturas\n\
[4]: Traer el héroe más pesado\n\
[5]: Traer el héroe menos pesado\n\
[6]: Salir del programa\n')


def validar_entero(nro: str) -> bool:
    '''
    Funcion que valida si un string está conformado por numeros
    '''
    return True if nro.isnumeric() else False


def stark_menu_principal() -> int:
    '''
    Funcion que imprime el menu y valida si el input es un numérico válido.
    En caso de serlo, casteará el input en entero; caso contrario, retorna -1
    '''
    imprimir_menu()
    answer = input('> ')
    result = -1
    if (validar_entero(answer) and (int(answer) > 0 and int(answer) < 7)):
        result = int(answer)
    return result
