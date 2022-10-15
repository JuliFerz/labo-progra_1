# MIT License
#
# Copyright (c) 2022 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from funciones_sw import (
    buscar_personaje_en_lista, cargar_json, continuar_consola,
    exportar_a_csv, imprimir_menu, listar_por_genero, listar_max_por_genero,
    mostrar, ordenar_lista, validar_respuesta, desordenar_lista
)


FILE_IN = '../Clase_14.PP_Modificado/starwars.json'
FILE_OUT = '../Clase_14.PP_Modificado/starwars.csv'


def starwars_app_v2():
    lista_personajes = cargar_json(FILE_IN)
    while(True):
        imprimir_menu()
        respuesta = validar_respuesta(input('>> '), '^[0-9]{1,2}$')
        if(respuesta == "1"):
            key = 'height'
            results = ordenar_lista(lista_personajes, key)
            mostrar(results, key)
        elif(respuesta == "2"):
            results = listar_max_por_genero(lista_personajes, 'male')
            results += listar_max_por_genero(lista_personajes, 'female')
            results += listar_max_por_genero(lista_personajes, 'n/a')
            mostrar(results)
        elif(respuesta == "3"):
            key = 'mass'
            results = ordenar_lista(lista_personajes, key)
            mostrar(results, key)
        elif(respuesta == "4"):
            pattern = validar_respuesta(
                input("Ingrese un nombre a buscar: "), r'^[a-zA-Z]+')
            buscar_personaje_en_lista(lista_personajes, pattern)
        elif(respuesta == "5"):
            gender = 'female'
            results = listar_por_genero(lista_personajes, gender)
            mostrar(results, gender)
        elif(respuesta == "6"):
            gender = 'male'
            results = listar_por_genero(lista_personajes, gender)
            mostrar(results, gender)
        elif(respuesta == "7"):
            gender = 'n/a'
            results = listar_por_genero(lista_personajes, gender)
            mostrar(results, gender)
        elif(respuesta == "8"):
            results = [desordenar_lista(lista_personajes)]
            mostrar(results, 'random')
        elif(respuesta == "9"):
            exportar_a_csv(results, FILE_OUT)
        elif(respuesta == "10"):
            break
        else:
            print('Opcion incorrecta.')
        continuar_consola()


starwars_app_v2()
