# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios' en caso de existir mostrar precio y el stock. En caso de no existir el producto mostrar el mensaje 'el articulo no se encuentra en la lista'

# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el precio total (precio * cantidad)

# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, unidad de medida y stock. Agregar la nueva fruta a la lista de precios

# Punto 4: imprimir el listado de frutas (solo su nombre)

# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir eliminarla. En caso de que el producto no exista mostrar
# el mensaje 'el articulo no se encuentra en la lista'

lista_precios = {
    "banana": {
        "precio": 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40
    },
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100
    },
    "mango": {
        "precio": 300,
        "unidad_medida": "unidad",
        "stock": 100
    }
}

# 1
""" answer = input('Buscar el producto:\n> ')
if lista_precios.get(answer):
    # 2
    answer_qty = input('\nIngrese la cantidad a comprar:\n> ')
    answer_qty = int(answer_qty)
    if answer_qty < lista_precios[answer]['stock']:
        precio_total = lista_precios[answer]['precio'] * answer_qty
        print(
            f'\nProducto: {answer}\n> Precio: ${precio_total}\n> Stock: {lista_precios[answer]["stock"]}')

    # print('Cantidad a comprar incorrecta')
else:
    print('El articulo no se encuentra en la lista') 
"""

# 3 - sin validación
""" nueva_fruta = input('\nIngrese el nombre de la nueva fruta:\n> ')
new_precio = float(input('\nIngrese el precio de la nueva fruta:\n> '))
new_unidad_med = input('\nIngrese la unidad de medida de la nueva fruta:\n> ')
new_stock = int(input('\nIngrese el stock de la nueva fruta:\n> '))

lista_precios.update({nueva_fruta: {'precio': new_precio,
                     'unidad_medida': new_unidad_med, 'stock': new_stock}})
print(lista_precios)
"""


# 4
""" for value in lista_precios.keys():
    print(f'• Nombre: {value}')
"""

# 5
answer = input('Buscar el producto para eliminar:\n> ')
if lista_precios.get(answer):
    lista_precios.pop(answer)
else:
    print('El articulo no se encuentra en la lista')
print(lista_precios)
