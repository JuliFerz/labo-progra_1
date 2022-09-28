from functions import *
from data_stark import lista_heroes


def stark_marvel_app_3(lista_heroes: list) -> str:
    '''
    Funcion main del programa. Imprime el menu principal y acciona sobre cada uno 
    Recibe una lista de heroes (list)
    Devuelve el resultado de cada función (segun el caso)
    '''
    while True:
        answer = stark_menu_principal()

        if (answer.isnumeric() and (int(answer) > 0 and int(answer) < 6)):
            answer = int(answer)
            if (answer == 1):
                system("cls")
                stark_imprimir_nombres_con_iniciales(lista_heroes)
            elif (answer == 2):
                system("cls")
                stark_generar_codigos_heroes(lista_heroes)
            elif (answer == 3):
                system("cls")
                stark_normalizar_datos(lista_heroes)
            elif (answer == 4):
                system("cls")
                stark_imprimir_indice_nombre(lista_heroes)
            elif (answer == 5):
                system("cls")
                try:
                    stark_navegar_fichas(lista_heroes)
                except:
                    print(
                        '\n[ERROR] Primero debe:\n\
        1. Generar la lista de iniciales\n\
        2. Generar los códigos a los héroes\n\
        3. Sanitizar los datos')
                    continue

        elif(answer.isalpha() and answer.upper() == 'S'):
            break
        else:
            print('\n[ERROR] Elija nuevamente:')
            continue


stark_marvel_app_3(lista_heroes)
