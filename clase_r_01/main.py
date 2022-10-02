'''
1- Listar TOP N videos
2- Ordenar videos por duracion (UP/DOWN)
3- Ordenar videos por cantidad de views (UP/DOWN)
4- Buscar videos por título
5 - Exportar lista de videos a CSV
6 - Salir
'''
from functions import *


def paulina_app():
    lista_videos = cargar_json("./clase_r/ACAELJSON.json")

    while True:
        print('''
    1- Listar TOP N videos
    2- Ordenar videos por duracion (UP/DOWN)
    3- Ordenar videos por cantidad de views (UP/DOWN)
    4- Buscar videos por título
    5 - Exportar lista de videos a CSV
    6 - Salir
        ''')
        answer = input()

        if(answer == '1'):
            top = int(input('Cantidad de elementos a mostrar?\n> '))
            # VALIDAR QUE TOP SEA UN INT Y QUE NO SUPERE LA LONGITUD DE LA LISTA
            mostrar(lista_videos[:top])
        elif(answer == '2'):
            mostrar(n_sort(lista_videos, 'length', 'down'))
            mostrar(n_sort(lista_videos, 'views', 'up'))
        elif(answer == '3'):
            print('3- Ordenar videos por cantidad de views (UP/DOWN)')
        elif(answer == '4'):
            patron = input('Buscar: ')
            buscar(lista_videos, patron)
        elif(answer == '5'):
            exportar_csv(lista_videos, './DIRECCION/DIR/paulina.csv')
        elif(answer == '6'):
            break


paulina_app()
