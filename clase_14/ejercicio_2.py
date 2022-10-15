# Punto 1: Modificar la calle y altura de 'persona_1' por Ramón Franco 5050.

# Punto 2: Verificar si existe un numero de telefono con la etiqueta 'trabajo'. Si no existe, entonces crearlo con el valor +54 11 4201-4133. Caso contrario actualizarlo

# Punto 3: imprimir los datos completos de persona_1 recorriendo todas sus claves y valores

# Punto 4:
#   Obtener el id de 'persona_1' y de 'persona_2'.
#   Comprarlos, si son iguales imprirmir:
#       "'ID de persona_1 es: id_persona_1 y el ID de persona_2 es: id_persona_2 entonces son el mismo diccionario' caso contrario imprimir "No son el mismo diccionario"
#   Modificar el nombre y apellido de persona_1 por Emilio Ravenna
#   Imprimir persona_1 y persona_2 y analizar los resultados
## persona_2 = persona_1

# Punto 5:
#   Crear persona_3 a partir de una copia superficial de persona_1
#   Modificar nombre y apellido a persona_3 por Gabriel Medina
#   Modificar el nro de documento por 28.307.401
#   Imprimir persana_1 y persona_3 y analizar los resultados

# Punto 6:
#   Crear persona_4 a partir de una copia profunda de persona_1
#   Modificar el nombre y apellido por Mario Santos
#   Modificar el nro de documento por: 29.407.901
#   Imprimir persana_1 y persona_3 y analizar los resultados
from copy import deepcopy
persona_1 = {
    "nombre": "Maximo",
    "apellido": "Cozzetti",
    "domicilio": {
        "calle": "Av. Mitre",
        "altura": 750,
        "localidad": "Avellaneda",
        "barrio": "Avellaneda Centro",
        "cod_postal": "C1870"
    },
    "telefonos": [
        {
            "etiqueta": "fijo",
            # "etiqueta": "trabajo",
            "cod_pais": "+54",
            "cod_area": "11",
            "numero": "4201-4133"
        },
        {
            "etiqueta": "movil",
            "cod_pais": "+54",
            "cod_area": "11",
            "nro": "4353-0220"
        }
    ],
    "identificacion": {
        "tipo": "dni",
        "nro": "30.505.003"
    }
}


# 1 - REVISAR
# Método 1:
""" address = persona_1.get('domicilio')
address['calle'] = 'Ramón Franco'
address['altura'] = 5050 """

# Método 2:
# persona_1['domicilio'].update({'calle': 'Ramón Franco', 'altura': 5050})

# Método 3: (no usar)
""" persona_1['domicilio']['calle'] = 'Ramón Franco'
persona_1['domicilio']['altura'] = 5050 """


# 2
""" busqueda = 'trabajo'
nuevo_numero = {"etiqueta": "trabajo", "cod_pais": "+54",
                "cod_area": "11", "numero": "4201-4133"}
for tel in persona_1['telefonos']:
    if busqueda in tel['etiqueta']:
        tel.update(nuevo_numero)
        break
    else:
        persona_1['telefonos'].extend([nuevo_numero])
        break """
# print(persona_1['telefonos'])


# 3
""" def imprimir_diccionario(diccionario: dict) -> str:
    return list(map(lambda val: print(f'\t{val[0]} -> {val[1]}'), diccionario.items()))


for key, value in persona_1.items():
    if type(value) == type({}):
        print(f'• {key.capitalize()}:')
        for el in value:
            print(f'\t{el} -> {value[el]}')
    elif type(value) == type([]):
        print(f'• {key.capitalize()}:')
        for el in value:
            imprimir_diccionario(el)
    else:
        print(f'• {key.capitalize()} -> {value}') """


# 4
""" persona_2 = persona_1  # Copia del enunciado
if id(persona_2) == id(persona_1):
    print(
        f'ID de persona_1 es: {id(persona_1)} y el ID de persona_2 es: {id(persona_2)} entonces son el mismo diccionario')
else:
    print('No son el mismo diccionario')

persona_2.update({'nombre': 'Emilio', 'apellido': 'Ravenna'})
# Se modifica en ambos porque no se copió el objeto persona_1 en persona_2
# sino que se pasó la referencia en memoria, por ende, se modificaron ambos que apuntan a la misma dirección
# print(persona_1)
# print(persona_2)
 """


# 5
""" persona_3 = persona_1.copy()
persona_3.update({'nombre': 'Gabriel', 'apellido': 'Medina'})
persona_3['identificacion'].update({'nro': '28.307.401'})
# Se modificó en ambos el mismo nro de dni ya que se hizo una copia superficial y no profunda
# Es decir, los objetos que estén dentro del objeto que se copió superficialmente, no se creará un nuevo espacio en memoria
# Sino que se pasará la misma referencia, por ende, se modifican ambos por igual
# print(persona_1)
# print(persona_3)
 """


# 6
persona_4 = deepcopy(persona_1)
persona_4.update({'nombre': 'Mario', 'apellido': 'Santos'})
persona_4['identificacion'].update({'nro': '29.407.901'})
# En este caso no se modificó el DNI en ambos dos dado que se hizo una copia profunda de persona_1
# Es decir, se creó un nuevo espacio en memoria por cada objeto que tenga dentro persona_1
# Por ende, las modificaciones de persona_4 no alterarán a persona_1
print(persona_1)
print(persona_4)
