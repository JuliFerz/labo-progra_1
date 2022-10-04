'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones


def starwars_app():
    lista_personajes = funciones.cargar_json(
        "../parcial_01/PP_STARWARS/data.json")

    result = False
    while(True):
        print("\n1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta == "1"):
            print("1 - Listar los personajes ordenados por altura\n")
            result = funciones.final_lista_personajes_altura(lista_personajes)
        elif(respuesta == "2"):
            print("2 - Mostrar el personaje mas alto de cada genero\n")
            result = funciones.final_mostrar_personajes_genero(
                lista_personajes)
        elif(respuesta == "3"):
            print("3 - Ordenar los personajes por peso\n")
            result = funciones.final_ordenar_personajes_peso(lista_personajes)
        elif(respuesta == "4"):
            print("4 - Armar un buscador de personajes\n")
            pattern = input('Escriba su busqueda...\n> ')
            result = funciones.final_buscador_personajes(
                lista_personajes, pattern)
        elif(respuesta == "5"):
            print("5 - Exportar lista personajes a CSV\n")
            if result:
                funciones.guardar_resultados('results.csv', result)
            else:
                print('[ERROR] Elija una opción y reintente')
                continue
        elif(respuesta == "6"):
            break


starwars_app()
