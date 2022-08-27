""" 
Autor: Fernandez, Julian
Divison: H
Ejercicio: Ejercicio_I_01
"""
# Del más caro de los barbijos, la cantidad de unidades y el fabricante.
precio_max = 0
qty_barbijo = 0
fabr_barbijo = 0
fabr_barbijo = ''
# Del ítem con más unidades, el fabricante.
stock_max = 0
# Cuántas unidades de jabones hay en total.
suma_total_jabon = 0

for producto in range(5):
    tipo = input(
        'Escriba el tipo de producto ("barbijo", "jabón" o "alcohol")\n')
    while (tipo != 'barbijo' and tipo != 'jabón' and tipo != 'alcohol'):
        tipo = input('ERROR: Re escriba el tipo de producto\n')

    precio = input('Escriba el precio del producto (válido entre 100 y 300)\n')
    precio = float(precio)
    while (precio < 100 or precio > 300):
        precio = float(input('ERROR: Re escriba el precio del producto\n'))

    stock = input('Ingrese el stock del artículo (entre 1 a 1000u.):\n')
    stock = int(stock)
    while(stock < 1 or stock > 1000):
        stock = int(input('ERROR: Reingrese el stock del artículo:\n'))

    marca = input('Ingrese la marca del artículo: \n')
    fabricante = input('Ingrese el fabricante del artículo: \n')

    # Del más caro de los barbijos, la cantidad de unidades y el fabricante.
    if (tipo == 'barbijo' and precio > precio_max):
        precio_max = precio
        qty_barbijo = stock
        fabr_barbijo = fabricante

    # Del ítem con más unidades, el fabricante.
    if (stock > stock_max):
        stock_max = stock
        fabr_max_stock = fabricante

    # Cuántas unidades de jabones hay en total.
    if (tipo == 'jabón'):
        suma_total_jabon += stock
# fuera

print(
    f'El mas caro de los barbijos tiene una cantidad de: {qty_barbijo} y es fabricado por: {fabr_barbijo}')
print(f'El item con mas unidades es: {fabr_max_stock}')
print(f'La suma de todos los jabones: {suma_total_jabon}')
