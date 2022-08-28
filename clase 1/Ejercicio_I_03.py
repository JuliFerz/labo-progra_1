""" 
La división de alimentos de industrias Wayne está trabajando en un pequeño software para cargar datos de heroínas y héroes, para tener un control de las condiciones de heroes existentes, nos solicitan:
    1. Nombre de Heroína/Héroe
    2. EDAD (mayores a 18 años)
    3. Sexo ("m", "f" o "nb")
    4. Habilidad ("fuerza", "magia", "inteligencia").

A su vez, el programa deberá mostrar por consola lo siguiente:
    A. Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
    B. El sexo y nombre de Heroe | Heroína de mayor edad.
    C. La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
    D. El promedio de edad entre Heroinas.
    E. El promedio de edad entre Heroes de fuerza.
"""
continue_script = True
menor_edad_flag = True  # A
menor_edad = 0  # A
nombre_menor_edad = ''  # A
mayor_edad = 0  # B
genero_mayor_edad = ''  # B
nombre_mayor_edad = ''  # B
cant_heroinas_fuer_mag = 0  # C
cant_heroinas = 0  # D
suma_edad_heroinas = 0  # D
promedio_heroinas = 0  # D
cant_heroes_fuerza = 0  # E
suma_edad_heroes_fuerza = 0  # E
promedio_heroes_fuerza = 0  # E

while(continue_script):
    nombre = input('Ingrese el nombre de su heroína/héroe:\n')
    while(nombre.isnumeric() or nombre == ''):
        nombre = input('[ERROR]: Ingrese un nombre válido:\n')

    edad = input('Ingrese la edad de su heroína/héroe (mayor a 18 años):\n')
    while(not edad.isnumeric() or (int(edad) < 19)):
        edad = input('[ERROR]Ingrese una edad válida:\n')
    edad = int(edad)

    genero = input('Ingrese el sexo: (válido: [m] [f] [nb]\n')
    while(genero.lower() != 'm'
          and genero.lower() != 'f'
          and genero.lower() != 'nb'):
        genero = input('[ERROR] Ingrese un sexo válido: ([m] [f] [nb]\n')

    habilidad = input(
        'Ingrese la habilidad del personaje: ("fuerza", "magia", "inteligencia")\n')
    while(habilidad.lower() != 'fuerza'
          and habilidad.lower() != 'magia'
          and habilidad.lower() != 'inteligencia'):
        habilidad = input(
            '[ERROR] Ingrese una habilidad válida: ("fuerza", "magia", "inteligencia")\n')

    # A. Dar el nombre de Héroe | Heroína de 'fuerza' más joven. REVISAR
    if (habilidad == 'fuerza' and menor_edad_flag):
        menor_edad = edad
        nombre_menor_edad = nombre
        menor_edad_flag = False
    elif (habilidad == 'fuerza' and edad < menor_edad):
        menor_edad = edad
        nombre_menor_edad = nombre

    # B. El sexo y nombre de Heroe | Heroína de mayor edad.
    if (edad > mayor_edad):
        mayor_edad = edad
        genero_mayor_edad = genero
        nombre_mayor_edad = nombre

    # C. La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
    if (genero.lower() == 'f' and
            (habilidad.lower() == 'fuerza' or habilidad.lower() == 'magia')):
        cant_heroinas_fuer_mag += 1

    # E. El promedio de edad entre Heroes de fuerza.
    if (genero.lower() == 'm' and habilidad.lower() == 'fuerza'):
        cant_heroes_fuerza += 1
        suma_edad_heroes_fuerza += edad
    # D. El promedio de edad entre Heroinas.
    elif (genero.lower() == 'f'):
        cant_heroinas += 1
        suma_edad_heroinas += edad

    answer = input('\nDesea continuar? [n]: No | [s]: si\n')
    while(answer.lower() != 'n' and answer.lower() != 's'):
        answer = input('[ERROR] Desea continuar? [n]: No | [s]: si\n')
    continue_script = False if answer.lower() == 'n' else continue_script
# termina

if (genero_mayor_edad.lower() == 'm'):
    genero_mayor_edad = 'masculino'
elif (genero_mayor_edad.lower() == 'f'):
    genero_mayor_edad = 'femenino'

# D. El promedio de edad entre Heroinas.
promedio_heroinas = suma_edad_heroinas / cant_heroinas if cant_heroinas else 0
# E. El promedio de edad entre Heroes de fuerza.
promedio_heroes_fuerza = suma_edad_heroes_fuerza / \
    cant_heroes_fuerza if cant_heroes_fuerza else 0

print(
    f'El nombre de héroe | heroína más joven de "fuerza" es: {nombre_menor_edad.capitalize()} ({menor_edad} años)')
print(
    f'El nombre de héroe | heroína de mayor edad es {nombre_mayor_edad} y su sexo es {genero_mayor_edad} ({mayor_edad} años)')
print(
    f'La cantidad de Heroinas que tienen habilidades de "fuerza" o "magia" es: {cant_heroinas_fuer_mag}')
print(f'Promedio de edad de heroinas: {promedio_heroinas}')
print(f'Promedio de edad de heroes de fuerza: {promedio_heroes_fuerza}')
