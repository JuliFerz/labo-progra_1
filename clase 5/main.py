from functions import *
from data_stark import lista_heroes


def stark_marvel_app(lista: list) -> str:
    '''
    Funcion main del programa. Imprime el menu principal y acciona sobre cada uno
    Recibe un input por consola (str) del llamado de otra función
    Devuelve un string con el resultado, segun el caso que se elija por input
    '''
    while True:
        answer = stark_menu_principal()
        while(answer == -1):
            print('[ERROR]: Seleccione una opcion correcta')
            answer = stark_menu_principal()

        if(answer == 1):
            stark_normalizar_datos(lista, 'altura', 'float')
            stark_calcular_imprimir_heroe(lista, 'max', 'altura')
        elif(answer == 2):
            stark_normalizar_datos(lista, 'altura', 'float')
            stark_calcular_imprimir_heroe(lista, 'min', 'altura')
        elif(answer == 3):
            stark_normalizar_datos(lista, 'altura', 'float')
            stark_calcular_imprimir_promedio_altura(lista)
        elif(answer == 4):
            stark_normalizar_datos(lista, 'peso', 'float')
            stark_calcular_imprimir_heroe(lista, 'max', 'peso')
        elif(answer == 5):
            stark_normalizar_datos(lista, 'peso', 'float')
            stark_calcular_imprimir_heroe(lista, 'min', 'peso')
        elif(answer == 6):
            break


stark_marvel_app(lista_heroes)
