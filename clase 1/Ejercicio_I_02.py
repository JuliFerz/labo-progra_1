"""
1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.
 """
continue_script = True
suma_kilos = 0
descuento = 100
suma_precio_bruto = 0
importe_con_descuento = 0
precio_max = 0
tipo_mas_caro = ''  # ?
promedio_precio = 0


while(continue_script):
    peso = input('Ingrese el peso del ingrediente: (entre 10 y 100 kilos)\n')
    while (not peso.isnumeric() or (int(peso) < 10 or int(peso) > 100)):
        peso = input('ERROR: Reingrese el peso del ingrediente:\n')
    peso = int(peso)

    precio_por_kilo = input('Ingrese el precio por kilo: (mayor a 0)\n')
    while (not precio_por_kilo.isnumeric() or (int(precio_por_kilo) < 1)):
        precio_por_kilo = input('ERROR: Reingrese el precio por kilo:\n')
    precio_por_kilo = int(precio_por_kilo)

    tipo_validad = input(
        'Ingrese el tipo de validad\n[v]: vegetal [a]: animal [m]: mezcla\n')
    while (tipo_validad.lower() != 'v' and tipo_validad.lower() != 'a' and tipo_validad.lower() != 'm'):
        tipo_validad = input('ERROR: Reingrese el tipo de validad:\n')

    suma_kilos += peso
    if (suma_kilos > 100 and suma_kilos < 300):
        descuento = 15
    elif (suma_kilos > 300):
        descuento = 25

    # A. El importe total a pagar, BRUTO sin descuento.
    suma_precio_bruto += precio_por_kilo

    # B. El importe total a pagar con descuento (Solo si corresponde).
    importe_con_descuento = suma_precio_bruto - \
        (suma_precio_bruto * descuento / 100)

    # C. Informar el tipo de alimento más caro.
    if (precio_por_kilo > precio_max):
        precio_max = precio_por_kilo
        tipo_mas_caro = tipo_validad

    # D. El promedio de precio por kilo en total.
    # promedio_precio = suma_precio_bruto / suma_kilos

    answer = input('\nDesea continuar? [n]: No | [s]: si\n')
    while(answer.lower() != 'n' and answer.lower() != 's'):
        answer = input('[ERROR] Desea continuar? [n]: No | [s]: si\n')
    continue_script = False if answer.lower() == 'n' else continue_script
# termina

if (tipo_mas_caro == 'v'):
    tipo_mas_caro = 'Vegetal'
elif(tipo_mas_caro == 'a'):
    tipo_mas_caro = 'Animal'
elif(tipo_mas_caro == 'm'):
    tipo_mas_caro = 'Mezcla'

# D. El promedio de precio por kilo en total.
promedio_precio = suma_precio_bruto / suma_kilos

print(f'Importe BRUTO a pagar: ${suma_precio_bruto}')
print(
    f'Importe a pagar con descuento ({descuento}%): ${importe_con_descuento}') if importe_con_descuento else ''
print(f'El tipo de alimento mas caro es: {tipo_mas_caro}')
print(f'Promedio de precio por kilo: ${promedio_precio}')
