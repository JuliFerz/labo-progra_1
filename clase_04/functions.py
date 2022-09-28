from data_stark import lista_heroes


def imprimir_nombres_M():
    for heroe in lista_heroes:
        if(heroe['genero'] == 'M'):
            nombre = heroe['nombre']
            print('Nombre heroe: {0}'.format(nombre))


def imprimir_nombres_F():
    for heroe in lista_heroes:
        if(heroe['genero'] == 'F'):
            nombre = heroe['nombre']
            print('Nombre heroina: {0}'.format(nombre))


def encontrar_primer_masculino():
    for heroe in lista_heroes:
        if (heroe['genero'] == 'M'):
            heroe_M = heroe
            break
    return heroe_M


def encontrar_primer_femenino():
    for heroe in lista_heroes:
        if (heroe['genero'] == 'F'):
            heroe_F = heroe
            break
    return heroe_F


def calcular_heroe_mas_alto_M():
    heroe_mas_alto_M = encontrar_primer_masculino()
    for heroe in lista_heroes:
        heroe_alto = float(heroe['altura'])
        if (heroe['genero'] == 'M' and heroe_alto > float(heroe_mas_alto_M['altura'])):
            heroe_mas_alto_M = heroe
    return heroe_mas_alto_M


def calcular_heroe_mas_alto_F():
    heroe_mas_alto_F = encontrar_primer_femenino()
    for heroe in lista_heroes:
        heroe_alto = float(heroe['altura'])
        if (heroe['genero'] == 'F' and heroe_alto > float(heroe_mas_alto_F['altura'])):
            heroe_mas_alto_F = heroe
    return heroe_mas_alto_F


def calcular_heroe_mas_bajo_M():
    heroe_mas_bajo_M = encontrar_primer_masculino()
    for heroe in lista_heroes:
        heroe_alto = float(heroe['altura'])
        if (heroe['genero'] == 'M' and heroe_alto < float(heroe_mas_bajo_M['altura'])):
            heroe_mas_bajo_M = heroe
    return heroe_mas_bajo_M


def calcular_heroe_mas_bajo_F():
    heroe_mas_bajo_F = encontrar_primer_femenino()
    for heroe in lista_heroes:
        heroe_alto = float(heroe['altura'])
        if (heroe['genero'] == 'F' and heroe_alto < float(heroe_mas_bajo_F['altura'])):
            heroe_mas_bajo_F = heroe
    return heroe_mas_bajo_F


def calcular_promedio_altura_M():
    acumulador_alturas = 0
    contador_heroes_m = 0
    for heroe in lista_heroes:
        genero = heroe['genero']
        if (genero == 'M'):
            altura = float(heroe['altura'])
            acumulador_alturas += altura
            contador_heroes_m += 1
    print('Promedio de altura de heroes: {0}'.format(
        acumulador_alturas / contador_heroes_m))


def calcular_promedio_altura_F():
    acumulador_alturas = 0
    contador_heroes_f = 0
    for heroe in lista_heroes:
        genero = heroe['genero']
        if (genero == 'F'):
            altura = float(heroe['altura'])
            acumulador_alturas += altura
            contador_heroes_f += 1
    print('Promedio de altura de heroinas: {0}'.format(
        acumulador_alturas / contador_heroes_f))


def informar_nombres_alto_bajo():
    heroe_mas_alto_M = calcular_heroe_mas_alto_M()
    heroe_mas_alto_F = calcular_heroe_mas_alto_F()
    heroe_mas_bajo_M = calcular_heroe_mas_bajo_M()
    heroe_mas_bajo_F = calcular_heroe_mas_bajo_F()
    print('Nombre del heroe mas ALTO_M: {0}\nNombre del heroe mas ALTO_F: {1}\nNombre del heroe mas BAJO_M: {2}\nNombre del heroe mas BAJO_F: {3}'.format(
        heroe_mas_alto_M['nombre'], heroe_mas_alto_F['nombre'], heroe_mas_bajo_M['nombre'], heroe_mas_bajo_F['nombre']))


def calcular_heroes_tipo_ojos():
    lista_colores = set([])
    lista_color_ojos = []
    for heroe in lista_heroes:
        color_ojos = heroe['color_ojos'].capitalize()
        lista_colores.add(color_ojos)

    for color in lista_colores:
        dict_temp = {'color': color, 'cantidad': 0}
        for heroe in lista_heroes:
            color_ojos = heroe['color_ojos'].capitalize()
            if color_ojos == color:
                dict_temp['cantidad'] += 1
        lista_color_ojos.append(dict_temp)

    return lista_color_ojos


def calcular_heroes_tipo_pelo():
    lista_color_pelos = set([])
    lista_cantidad_pelos = []
    for heroe in lista_heroes:
        color_pelo = heroe['color_pelo'].capitalize() or 'No hair'
        lista_color_pelos.add(color_pelo)

    for tipo_pelo in lista_color_pelos:
        dict_temp = {'color_pelo': tipo_pelo, 'cantidad': 0}
        for heroe in lista_heroes:
            color_pelo = heroe['color_pelo'].capitalize() or 'No hair'
            if color_pelo == tipo_pelo:
                dict_temp['cantidad'] += 1
        lista_cantidad_pelos.append(dict_temp)

    return lista_cantidad_pelos


def calcular_heroes_tipo_inteligencia():
    lista_tipos_inteligencia = set([])
    lista_cantidad_tipo_inteligencia = []
    for heroe in lista_heroes:
        inteligencia_heroe = heroe['inteligencia'].capitalize() or 'No tiene'
        lista_tipos_inteligencia.add(inteligencia_heroe)

    for ci in lista_tipos_inteligencia:  # ci = inteligencia
        dict_temp = {'tipo_inteligencia': ci, 'cantidad': 0}
        for heroe in lista_heroes:
            inteligencia_heroe = heroe['inteligencia'].capitalize(
            ) or 'No tiene'
            if inteligencia_heroe == ci:
                dict_temp['cantidad'] += 1
        lista_cantidad_tipo_inteligencia.append(dict_temp)

    return lista_cantidad_tipo_inteligencia


def informar_heroes_color_ojos():
    heroes_colores = calcular_heroes_tipo_ojos()
    lista_heroes_color = []

    for heroe_color in heroes_colores:
        color_heroe = heroe_color['color']
        dict_colores = {'color': color_heroe, 'datos_heroes': []}

        for heroe in lista_heroes:
            color_ojo = heroe['color_ojos'].capitalize()
            if color_ojo == color_heroe:
                dict_colores['datos_heroes'].append(heroe)

        lista_heroes_color.append(dict_colores)

    for heroe in lista_heroes_color:
        print('\n-------------- COLOR DE OJOS: {0}'.format(heroe['color']))
        print('NOMBRES:')
        for dato_heroe in heroe['datos_heroes']:
            print('• {0}'.format(dato_heroe['nombre']))


def informar_heroes_color_pelo():
    heroes_colores = calcular_heroes_tipo_pelo()
    lista_heroes_color = []

    for heroe_color in heroes_colores:
        color_heroe = heroe_color['color_pelo']
        dict_colores = {'color_pelo': color_heroe, 'datos_heroes': []}
        for heroe in lista_heroes:
            color_pelo = heroe['color_pelo'].capitalize() or 'No hair'
            if color_pelo == color_heroe:
                dict_colores['datos_heroes'].append(heroe)
        lista_heroes_color.append(dict_colores)

    for heroe in lista_heroes_color:
        print(
            '\n-------------- COLOR DE PELO: {0}'.format(heroe['color_pelo']))
        print('NOMBRES:')
        for dato_heroe in heroe['datos_heroes']:
            print('• {0}'.format(dato_heroe['nombre']))


def informar_heroes_inteligencia():
    inteligencia_heroe = calcular_heroes_tipo_inteligencia()
    lista_heroes_inteligencia = []

    for ci in inteligencia_heroe:
        tipo_inteligencia = ci['tipo_inteligencia']
        dict_colores = {
            'tipo_inteligencia': tipo_inteligencia, 'datos_heroes': []}
        for heroe in lista_heroes:
            inteligencia = heroe['inteligencia'].capitalize() or 'No tiene'
            if inteligencia == tipo_inteligencia:
                dict_colores['datos_heroes'].append(heroe)
        lista_heroes_inteligencia.append(dict_colores)

    for heroe in lista_heroes_inteligencia:
        print(
            '\n-------------- TIPO DE INTELIGENCIA: {0}'.format(heroe['tipo_inteligencia']))
        print('NOMBRES:')
        for dato_heroe in heroe['datos_heroes']:
            print('• {0}'.format(dato_heroe['nombre']))
