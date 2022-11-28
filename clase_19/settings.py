from constantes import *
from plataforma import Platform, NewPlatform
from coin import Coin
from auxiliar import (Aux, Json)
from gui import *

# NUEVO
from characters import *


# l_players, l_enemies, l_npc, l_coins = Json.load_character_json(PATH_JSON+'/characters.json')
# tiles = Json.load_json_platforms(PATH_JSON+'/data_map.json') # para edición de mapa (solo para que puedan figurar todos los items en un menu para colocarlos despues en el mapa (en el json map.json))
# game_tiles = Json.load_json_map(PATH_JSON+'/map.json') # niveles pre-definidos


# obligatorios
param_char = ('type', 'name', 'mvm_frame_rate', 'anim_frame_rate')

param_actions = ('action', 'fileName', 'rows', 'columns',
                 'f_from', 'f_to', 'custom_cut_w', 'step')


# CHEQUEOS
''' 
# 1
def check_char_params(char_list: list):
    retorno = False
    i = 0
    for player in char_list:
        for key in player:
            if key in param_char:
                i += 1
    if i == len(param_char):
        retorno = True
    return retorno

# print(check_char_params(l_players))

# 2 REVISAR
def check_action_params(char_list: list):
    retorno = False
    i = 0
    if check_char_params(char_list):
        for player in char_list:
            for actions in player['actions']:
                print(actions)
    return retorno 

# print(check_action_params(l_players))
# '''

game_tiles, l_players, l_enemies, l_coins = Json.load_json_level(PATH_JSON + '/level_1.json')

def check_name(obj):
    name = None
    if obj['sub_type'] == 'Tiles':
        name = '{}'.format(obj['image'])
    else:
        if obj['image'] > 1:
            name = '{} ({})'.format(obj['name'], obj['image'])
        else:
            name = '{}'.format(obj['name'])
    return name

def get_platforms(platforms):
    temp_list = []
    for obj in platforms:
        name = check_name(obj)
        temp_list.append(NewPlatform(
            name=name,
            type=obj['type'],
            sub_type=obj['sub_type'],
            x=obj['x'],
            y=obj['y']
        ))
    return temp_list
game_tiles = get_platforms(game_tiles)

# Instanciar PJ's
# primer modelo: [{player_1: Instancia}, {player_2: Instancia}]
# segundo modelo: [Instancia, Instancia]
def get_players(l_players):
    temp_list = []
    i = 1
    for player in l_players:
        temp_list.append(Character.Character(
                manager = '',
                entity = f'player_{i}',
                c_type = player['type'],
                name = player['name'],
                animations = player['actions'],
                mvm_frame_rate = player['mvm_frame_rate'],
                anim_frame_rate = player['anim_frame_rate'],
                control_type=player['control']['type'],
                level_tiles='',
                x = player['x'],
                y = player['y'],
                speed_walk = player['speed_walk'],
                jump_height = player['jump_height'],
                damage = player['damage'],
                life = player['life'],
                lives = player['lives']
            ))
        i += 1
    return temp_list
l_players = get_players(l_players)

def get_enemies(l_enemies):
    temp_list = []
    i = 1
    for enemy in l_enemies:
        temp_list.append(Enemy.Enemy(
                manager='',
                entity=f'enemy_{i}',
                c_type = enemy['type'],
                name = enemy['name'],
                animations = enemy['actions'],
                separate_files=enemy['separate_files'],
                mvm_frame_rate = enemy['mvm_frame_rate'],
                anim_frame_rate = enemy['anim_frame_rate'],
                level_tiles = [],
                x = enemy['x'],
                y = enemy['y'],
                speed_walk = enemy['speed_walk'],
                damage = enemy['damage'],
                life = enemy['life'],
                lives = enemy['lives']
            ))
        # print(temp_list)
        i += 1
    return temp_list
l_enemies = get_enemies(l_enemies)

def get_coins(l_coins):
    temp_list = []
    i = 1
    for coin in l_coins:
        temp_list.append(Coin(
                manager = '',
                entity = f'coin_{i}',
                c_type = coin['type'],
                sub_type = coin['sub_type'],
                name = coin['name'],
                mvm_frame_rate = coin['mvm_frame_rate'],
                anim_frame_rate = coin['anim_frame_rate'],
                level_tiles = [],
                scale=50,
                x = coin['x'],
                y = coin['y']
            ))
        i += 1
    return temp_list
l_coins = get_coins(l_coins)


# SET LEVEL

level_map = {
    'platform': game_tiles,
    'players': l_players,
    'enemies': l_enemies,
    'coins': l_coins,
}
