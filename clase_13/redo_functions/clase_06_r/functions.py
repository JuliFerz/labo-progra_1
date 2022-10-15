import re
from os import system


def extraer_iniciales(nombre: str) -> str:
    '''
    Función que extrae las iniciales de los nombres de los héroes
    Recibe el nombre de cada heroe (type str)
    Retorna str con las iniciales separadas por un punto ("N/A" en caso de no tener nombre)
    '''
    retorno = 'N/A'
    if nombre.count('-'):
        nombre = nombre.replace('-', ' ')

    nombre_heroe = nombre.split(' ')
    temp_list = list(
        map(lambda el: el[0] if not el.lower().count('the') else '', nombre_heroe))
    temp_list.remove('') if '' in temp_list else ''
    retorno = '{0}.'.format('.'.join(temp_list))
    return retorno


def definir_iniciales_nombre(heroe: dict) -> bool:
    '''
    Función que agrega por cada héroe una clave con las iniciales
    Recibe un héroe (de tipo dictionary)
    Retorna un bool True en caso de caso positivo o un False en caso de no poder lograrlo
    '''
    retorno = False
    if (type(heroe) == type({}) and heroe.get('nombre')):
        heroe['iniciales'] = extraer_iniciales(heroe['nombre'])
        retorno = True
    return retorno


def agregar_iniciales_nombre(lista: list) -> bool:
    '''
    Función que recibe una lista de héroes, donde a cada uno será pasado a la función definir_iniciales_nombre
    Recibe una lista de héroes (de tipo list)
    Retorna un bool True en caso de caso positivo o un False en caso de no poder lograrlo (y detendrá la iteración)
    '''
    retorno = False
    if (type(lista) == type([]) and len(lista) > 0):
        for heroe in lista:
            retorno = definir_iniciales_nombre(heroe)
            if retorno == False:
                print('El origen de datos no contiene el formato correcto')
                break
        return retorno


def stark_imprimir_nombres_con_iniciales(lista: list) -> str:
    '''
    Función que recibe una lista de héroes, donde cada uno será enviado a agregar_iniciales_nombre
    Recibe una lista de héroes (de tipo list)
    Devuelve un string por cada línea mostrando el nombre y las iniciales entre paréntesis (no retorna nada)
    '''
    system('cls')
    heroe_iniciales = agregar_iniciales_nombre(lista)
    if (type(lista) == type([]) and len(lista) > 0 and heroe_iniciales):
        list(map(lambda el: print(
            f'* {el["nombre"]} ({el["iniciales"]})'), lista))


def generar_codigo_heroe(id_heroe: int, genero_heroe: str) -> str:
    '''
    Función que genera un codigo por cada héroe en base al id y al genero del heroe 
    Recibe el id (int) y género de cada heroe (str)
    Devuelve un string con el codigo generado o un 'N/A' en caso de no lograr realizarlo
    '''
    retorno = 'N/A'
    if (type(id_heroe) == type(0) and (genero_heroe == 'M' or genero_heroe == 'F' or genero_heroe == 'NB')):
        retorno = genero_heroe
        retorno += '-{0}'.format(id_heroe).zfill(9)
    return retorno


def agregar_codigo_heroe(heroe: dict, id_heroe: int) -> bool:
    '''
    Función que agrega por cada héroe una clave con el codigo 
    Recibe un heroe de tipo dictionary y un ID de heroe
    Devuelve True en caso de haber logrado agregar la clave o un False en caso contrario
    '''
    genero_heroe = heroe.get('genero')
    codigo_heroe = generar_codigo_heroe(id_heroe, genero_heroe)
    retorno = False
    if (heroe and len(codigo_heroe) == 10):
        heroe['codigo_heroe'] = codigo_heroe
        retorno = True
    return retorno


def stark_generar_codigos_heroes(lista: list) -> str:
    '''
    Función que agrega por cada héroe una clave con el código 
    Recibe la lista de los heroes
    Devuelve un string con el primer y el último heroe con sus codigos respectivos
    '''
    system('cls')
    if len(lista) > 0:
        i = 1
        for heroe in lista:
            if type(heroe) == type({}) and heroe.get('genero'):
                heroe = agregar_codigo_heroe(heroe, i)
                i += 1
            else:
                print('El origen de datos no contiene el formato correcto')
                return

        primer_heroe = lista[0]['codigo_heroe']
        ultimo_heroe = lista[len(lista) - 1]['codigo_heroe']
        print(f'Se asignaron {i - 1} códigos')
        print(f'El código del primer héroe es: {primer_heroe.rjust(19)}')
        print(f'El código del del último héroe es: {ultimo_heroe.rjust(15)}')


def sanitizar_entero(numero_str: str) -> int:
    '''
    Función que recibe un string y evalua si puede ser o no un int 
    Recibe un string para evaluar
    En caso positivo, devuelve el string convertido en int. Caso contrario, devuelve distintos códigos negativos en base al error
    '''
    # Si contiene carácteres no numéricos retornar -1
    # Si el número es negativo se deberá retornar un -2
    # Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3
    retorno = -3
    numero_str = numero_str.strip()

    if not re.search('[a-zA-Z,.]+', numero_str):
        retorno = int(numero_str)
        if retorno < 0:
            retorno = -2
    else:
        retorno = -1
    return retorno


def sanitizar_flotante(numero_str: str) -> float:
    '''
    Función que recibe un string y evalua si puede ser o no un float 
    Recibe un string para evaluar
    En caso positivo, devuelve el string convertido en float. Caso contrario, devuelve distintos códigos negativos en base al error
    '''
    # Consignas:
    # Si contiene carácteres no numéricos retornar -1
    # Si el número es negativo se deberá retornar un -2
    # Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3
    retorno = -3
    numero_str = numero_str.strip()

    if not re.search('[a-zA-Z,]+', numero_str):
        retorno = float(numero_str)
        if retorno < 0:
            retorno = -2
    else:
        retorno = -1
    return retorno


def sanitizar_string(valor_str: str, valor_por_defecto: str = '-') -> str:
    """
    Funcion que transforma un string en minusculas
    Recibe un string y un string por defecto (siendo este último opcional)
    Devuelve el string convertido en minusculas (en caso de no haber string, devuelve el por defecto)
    """
    retorno = 'N/A'

    valor_str = re.sub('/+', ' ', valor_str)
    if valor_str == '' and valor_por_defecto:
        retorno = valor_por_defecto.strip().lower()
    elif re.sub(' +', '', valor_str).isalpha():
        retorno = valor_str.strip().lower()

    return retorno


def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str) -> bool:
    """
    Funcion que castea los datos de un heroe (dictionary)
    Recibe un heroe (dict), una clave para saber a qué dato apuntar del heroe y un tipo_dato para saber a qué tipo de dato castear (str, int, float)
    Devuelve un True en caso de poder haberlo realizado, o un False en caso de error
    """
    lista_tipo_datos = ['string', 'entero', 'flotante']
    tipo_dato = tipo_dato.lower()
    if (not tipo_dato in lista_tipo_datos):
        print('Tipo de dato no reconcido')
        retorno = False
    elif(not clave in heroe):
        print('La clave especificada no existe en el héroe')
        retorno = False
    else:
        if tipo_dato == 'string':
            heroe[clave] = sanitizar_string(heroe[clave])
            retorno = True
        elif tipo_dato == 'entero':
            heroe[clave] = sanitizar_entero(heroe[clave])
            retorno = True
        elif tipo_dato == 'flotante':
            heroe[clave] = sanitizar_flotante(heroe[clave])
            retorno = True
    return retorno


def stark_normalizar_datos(lista: list):
    """
    Funcion que castea los datos de los heroes ('altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza' e 'inteligencia')
    Recibe una lista de heroes
    No devuelve, solo castea datos
    """
    system('cls')
    if not lista:
        print('Error: Lista de héroes vacía')
    else:
        for heroe in lista:
            sanitizar_dato(heroe, 'altura', 'flotante')
            sanitizar_dato(heroe, 'peso', 'flotante')
            sanitizar_dato(heroe, 'color_ojos', 'string')
            sanitizar_dato(heroe, 'color_pelo', 'string')
            sanitizar_dato(heroe, 'fuerza', 'entero')
            sanitizar_dato(heroe, 'inteligencia', 'string')
        print('Datos normalizados')


def generar_indice_nombres(lista_heroes: list) -> list:
    """
    Funcion genera una lista donde cada elemento es cada palabra del nombre de cada heroe
    Recibe una lista de heroes
    Devuelve una lista con cada palabra de los heroes
    """
    if len(lista_heroes) > 0:
        lista_nombres = []

        for heroe in lista_heroes:
            if (type(heroe) == type({}) and heroe.get('nombre')):
                nombre_heroe = heroe['nombre'].split(' ')
                for nombre in nombre_heroe:
                    lista_nombres.append(nombre)
            else:
                print('El origen de datos no contiene el formato correcto')
                break
    return lista_nombres


def stark_imprimir_indice_nombre(lista_heroes: list) -> str:
    """
    Funcion muestra los nombres de los héroes concatenados con un guion medio
    Recibe una lista de heroes
    Devuelve un string con los nombres concatenados
    """
    system('cls')
    lista_nombre_heroes = generar_indice_nombres(lista_heroes)
    return print('-'.join(lista_nombre_heroes))


def convertir_cm_a_mtrs(valor_cm: float) -> float:
    """
    Funcion que transforma un valor en cm en mtrs
    Recibe un valor flotante en cm
    Devuelve un float con el resultado en mtrs
    """
    retorno = -1
    if ((type(valor_cm) == type(0.0) or type(valor_cm) == type(0)) and valor_cm > 0):
        retorno = round(valor_cm / 100, 4)
    return retorno


def generar_separador(patron: str, largo: int, imprimir: bool = True) -> str:
    '''
    Funcion que genera un separador en base a los parámetros recibidos
    Recibe un "patron" (str) que se usará como patrón para el separador, un "largo" (int) para definir la longitud del separador y un "imprimir" (bool) opcional que definirá si imprime por consola o no el separador (por defecto en True)
    Retorna el separador
    '''
    retorno = 'N/A'
    if (len(patron) > 0 and len(patron) < 3) \
            and (type(largo) == type(0) and (largo >= 1 and largo <= 235)):
        retorno = patron * largo

    print(retorno) if imprimir else ''
    return retorno


def generar_encabezado(titulo: str) -> str:
    '''
    Funcion que genera un encabezado separado por la función previa
    Recibe un "titulo" (str) que será transformado en mayuscula
    La función devuelve el titulo con los separadores antes y luego del mismo
    '''
    separador = generar_separador('*', 80, False)
    return '{0}\n{1}\n{0}'.format(separador, titulo.upper())


def imprimir_ficha_heroe(heroe: dict) -> str:
    '''
    Funcion genera una ficha con datos de cada heroe
    Recibe un heroe (dict)
    La función devuelve los datos del heroe con cada encabezado
    '''
    encabezado_principal = generar_encabezado('principal')
    encabezado_fisico = generar_encabezado('fisico')
    encabezado_senias = generar_encabezado('señas particulares')
    system("cls")

    print(
        '{0}\n\
    \tNOMBRE DEL HÉROE: \t\t{1} ({2})\n\
    \tIDENTIDAD SECRETA: \t\t{3}\n\
    \tCONSULTORA: \t\t\t{4}\n\
    \tCÓDIGO DE HÉROE: \t\t{5}'.format(
            encabezado_principal,
            heroe['nombre'],
            heroe['iniciales'],
            heroe['identidad'],
            heroe['empresa'],
            heroe['codigo_heroe'])
    )
    print(
        '{0}\n\
    \tALTURA: \t\t\t{1:.2f} Mtrs.\n\
    \tPESO: \t\t\t\t{2} Kg.\n\
    \tFUERZA: \t\t\t{3} N'.format(
            encabezado_fisico,
            convertir_cm_a_mtrs(heroe['altura']),
            heroe['peso'],
            heroe['fuerza'])
    )
    print(
        '{0}\n\
    \tCOLOR DE OJOS: \t\t\t{1}\n\
    \tCOLOR DE PELO: \t\t\t{2}'.format(
            encabezado_senias,
            heroe['color_ojos'],
            heroe['color_pelo'])
    )


def stark_navegar_fichas(lista_heroes: list) -> str:
    '''
    Funcion recorre cada heroe de una lista
    Recibe una lista de heroes
    La función retorna el heroe en base a la elección del usuario
    '''
    system('cls')
    i = 0
    mensaje = '[1] Ir a la izquierda\t[2] Ir a la derecha\t[S] Salir\n'
    imprimir_ficha_heroe(lista_heroes[i])
    while True:
        print(mensaje)
        answer = input(' > ')

        if (answer.isnumeric() and (int(answer) > 0 and int(answer) < 3)):
            answer = int(answer)
            if (answer == 1):
                i -= 1
                if (i == -len(lista_heroes) - 1):
                    i = -1
                imprimir_ficha_heroe(lista_heroes[i])
            elif (answer == 2):
                i += 1
                if (i == len(lista_heroes)):
                    i = 0
                imprimir_ficha_heroe(lista_heroes[i])
        elif(answer.isalpha() and answer.upper() == 'S'):
            system("cls")
            break
        else:
            print('\n[ERROR] Elija nuevamente:')
            continue


def imprimir_menu() -> str:
    '''
    Funcion que imprime el menu. No tiene parametros.
    '''
    print(
        '\n1 - Generar e imprimir la lista de nombres junto con sus iniciales\n\
2 - Generar códigos de héroes\n\
3 - Normalizar datos\n\
4 - Imprimir índice de nombres\n\
5 - Navegar fichas\n\
S - Salir\n\
{0}'.format(generar_separador('-', 80, False))
    )


def stark_menu_principal() -> str:
    '''
    Funcion solicita al usuario elegir una opción.
    Devuelve el valor elegido (str)
    '''
    imprimir_menu()
    print('\nIngrese una opción:')
    answer = input(' > ')
    return answer
