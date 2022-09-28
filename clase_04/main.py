from functions import *

while True:
    answer = input('\n[1]: Traer nombres de heroes\n\
[2]: Traer nombres de heroinas\n\
[3]: Traer la altura promedio de los heroes\n\
[4]: Traer la altura promedio de las heroinas\n\
[5]: Traer el nombre de los superheroes mas bajo/alto de ambos generos\n\
[6]: Traer cantidad de heroes por color de ojos\n\
[7]: Traer cantidad de heroes por color de pelo\n\
[8]: Traer cantidad de heroes por inteligencia\n\
[9]: Traer lista de superheroes por color de ojos\n\
[10]: Traer lista de superheroes por color de pelo\n\
[11]: Traer lista de superheroes por inteligencia\n\
[12]: Salir del programa\n\n > ')

    while(not answer.isnumeric() or (int(answer) < 1 or int(answer) > 12)):
        answer = input('[ERROR]: Seleccione una opcion correcta\n>')

    if(answer == '1'):
        imprimir_nombres_M()
    elif(answer == '2'):
        imprimir_nombres_F()
    elif(answer == '3'):
        calcular_promedio_altura_M()
    elif(answer == '4'):
        calcular_promedio_altura_F()
    elif(answer == '5'):
        informar_nombres_alto_bajo()
    elif(answer == '6'):
        lista_color_ojos = calcular_heroes_tipo_ojos()
        for color_ojo in lista_color_ojos:
            print('• Color de ojos: {0}\n• Cantidad: {1}\n'.format(
                color_ojo['color'], color_ojo['cantidad']))
    elif(answer == '7'):
        lista_color_pelos = calcular_heroes_tipo_pelo()
        for color_pelo in lista_color_pelos:
            print('• Color de pelo: {0}\n• Cantidad: {1}\n'.format(
                color_pelo['color_pelo'], color_pelo['cantidad']))
    elif(answer == '8'):
        lista_tipos_inteligencia = calcular_heroes_tipo_inteligencia()
        for tipo_inteligencia in lista_tipos_inteligencia:
            print('• Tipo inteligencia: {0}\n• Cantidad: {1}\n'.format(
                tipo_inteligencia['tipo_inteligencia'], tipo_inteligencia['cantidad']))
    elif(answer == '9'):
        informar_heroes_color_ojos()
    elif(answer == '10'):
        informar_heroes_color_pelo()
    elif(answer == '11'):
        informar_heroes_inteligencia()
    elif(answer == '12'):
        break
