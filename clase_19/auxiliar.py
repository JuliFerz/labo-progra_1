import pygame, json
import re
from constantes import *


class Aux:
    @staticmethod
    def get_surface_from_sprite(path, filas, columnas, custom_w=0, step=1, custom_btm=0):
        lista = []
        try:
            surface = pygame.image.load(path)  # ancho 129 alto 100
        except:
            print('FALLO EN IMAGEN', path)
            print('FALLO EN IMAGEN', filas)
            print('FALLO EN IMAGEN', columnas)
        rect = surface.get_rect()
        ancho_f = int(rect.width / columnas)
        alto_f = int(rect.height / filas)
        # if re.search('aligator', path):
        # if re.search('aligator', path) and re.search('jump', path):
            # print('AAAAA',path)
            # print('ancho', ancho_f)
            # print('alto', alto_f)
        x = 0
        for f in range(0, filas, step):
            for c in range(0, columnas, step):
                x = c * ancho_f
                y = f * alto_f
                # print(x,y)
                new_surface = surface.subsurface(x, y, ancho_f - custom_w, alto_f)
                lista.append(new_surface)
            x = 0
        return lista

    @staticmethod
    # def get_surface_from_files(path_format,quantity,scale=1,w=0,h=0,repeat_frame=1):
    def get_surface_from_files(path, file_name, quantity=0, w=0, h=1, custom_btm=0):
        lista = []
        for i in range(quantity):
            surface = pygame.image.load(path+f'{file_name}_00{i}.png')

            rect = surface.get_rect()
            ancho_f = rect.width
            alto_f = rect.height
            x = 0
            # for f in range(0, filas, step):
                # for c in range(0, columnas, step):
            # x = c * ancho_f
            # y = f * alto_f
                    # print(x,y)
            # new_surface = surface.subsurface(x, y, ancho_f - custom_w, alto_f)
            # lista.append(new_surface)

            surface = pygame.transform.scale(surface,(w, h))
            
            lista.append(surface)
        return lista

        """ path = path_format.format(i)
        surface_fotograma = pygame.image.load(path)
        fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
        fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
        if(scale == 1 and w != 0 and h != 0):
            surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
        if(scale != 1):
            print("ENTREEE")
            surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
        
        for i in range(repeat_frame):
            lista.append(surface_fotograma) """


    # BORRAR
    @staticmethod
    def get_surface_form_file(path, filas, columnas, custom_w=0, step=1, custom_btm=0):
        lista = []
        try:
            surface = pygame.image.load(path)  # ancho 129 alto 100
        except:
            print('FALLO EN IMAGEN', path)
            print('FALLO EN IMAGEN', filas)
            print('FALLO EN IMAGEN', columnas)
        rect = surface.get_rect()
        ancho_f = int(rect.width / columnas)
        alto_f = int(rect.height / filas)

        # if re.search('aligator', path):
        # if re.search('aligator', path) and re.search('jump', path):
            # print('AAAAA',path)
            # print('ancho', ancho_f)
            # print('alto', alto_f)
        x = 0
        for f in range(0, filas, step):
            for c in range(0, columnas, step):
                x = c * ancho_f
                y = f * alto_f
                # print(x,y)
                new_surface = surface.subsurface(x, y, ancho_f - custom_w, alto_f)
                lista.append(new_surface)
            x = 0
        return lista


class Json:
    l_characters = []
    l_enemies = []
    l_npc = []
    l_coins = []

    @staticmethod
    def load_character_json(path):
        temp_list = []
        with open(path, 'r') as file:
            temp_list = json.load(file)
        return temp_list['players'], temp_list['enemies'], temp_list['npc'], temp_list['coins']

    
    @staticmethod
    def load_json_platforms(path):
        temp_list = []
        with open(path, 'r') as file:
            temp_list = json.load(file)
        # return temp_list['desert'], temp_list['forest'], temp_list['graveyard'], temp_list['space_ship'], temp_list['winter']
        return temp_list

    @staticmethod
    def load_json_map(path):
        temp_list = []
        with open(path, 'r') as file:
            temp_list = json.load(file)
        return temp_list['platforms']
    
    @staticmethod
    def load_json_level(path):
        temp_list = []
        with open(path, 'r') as file:
            temp_list = json.load(file)
        return temp_list['platforms'], temp_list['players'], temp_list['enemies'], temp_list['coins']
