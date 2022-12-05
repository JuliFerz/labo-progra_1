from constantes import *
from plataforma import TilePlatform
from item import Item
from auxiliar import (Aux, Json)

import pygame

from characters import *


# CHEQUEOS
''' 
param_char = ('type', 'name', 'mvm_frame_rate', 'anim_frame_rate')

param_actions = ('action', 'fileName', 'rows', 'columns', 'f_from', 'f_to', 'custom_cut_w', 'step')
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

game_levels = Json.load_json_info(PATH_JSON + '/levels.json')
game_config = Json.load_json_info(PATH_JSON + '/config.json')

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
        temp_list.append(TilePlatform(
            name=name,
            type=obj['type'],
            sub_type=obj['sub_type'],
            x=obj['x'],
            y=obj['y']
        ))
    return temp_list

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
                points = enemy.get('points') or 10,
                damage = enemy['damage'],
                life = enemy['life'],
                lives = enemy['lives']
            ))
        i += 1
    return temp_list

def get_items(l_items):
    temp_list = []
    i = 1
    for item in l_items:
        temp_list.append(Item(
                manager = '',
                entity = f'item_{i}',
                c_type = item['type'],
                sub_type = item['sub_type'],
                name = item['name'],
                mvm_frame_rate = item.get('mvm_frame_rate') or 1,
                anim_frame_rate = item.get('anim_frame_rate') or 1,
                rows=item.get('rows') or 1,
                columns=item.get('columns') or 1,
                points = item.get('points') or 0,
                health = item.get('health') or 0,
                bullets= item.get('bullets') or 0,
                level_tiles = [],   
                scale=50,
                x = item['x'],
                y = item['y']
            ))
        i += 1
    return temp_list

def get_levels(levels, id):
    return [{
        'id': id,
        'background': levels['background'],
        'platform': get_platforms(levels['platforms']),
        'players': get_players(levels['players']),
        'enemies': get_enemies(levels['enemies']),
        'items': get_items(levels['items']),  
    }]

def get_music(music):
    return pygame.mixer.Sound(f'{PATH_SOUNDS}/{music}')

def get_game_config(config):
    pygame.mixer.init()
    temp_dict = {'music':{}}
    # load music
    for key, value in config['music'].items():
        temp_dict['music'][key] = get_music(value)
    return temp_dict
    # return {
    #     'music':{
    #         'background': get_music(config['music']['background']),
    #         'coin': get_music(config['music']['coin']),
    #         'helltaker': get_music(config['music']['helltaker']),
    #         'jump': get_music(config['music']['jump']),
    #         'menu': get_music(config['music']['menu']),
    #         'select': get_music(config['music']['select']),
    #         'shoot': get_music(config['music']['shoot'])
    #     }        
    # }
# asd = get_game_config(game_config)
# print('asd',asd)

# level_map = get_levels(game_levels['level_1'], 'level_1')
# print(level_map) 
# print([game_levels['level_1']])

# [
#     {
#         'id': 'level_1',
#         'background': {'set': 'set_bg_01','type': 'city','image': 'all'},
#         'platform': [ < TilePlatform Sprite(in 0 groups) > ],
#         'players': [ < characters.character.Character object at 0x00000164F298B580 > ],
#         'enemies': [ < characters.enemy.Enemy object at 0x00000164F298B640 > ],
#         'coins': [ < coin.Coin object at 0x00000164F298B730 > ]
#     }
# ]

# NEW SET LEVEL
# level_map = [
#     {
#         'platform': game_tiles,
#         'players': l_players,
#         'enemies': l_enemies,
#         'coins': l_coins,
#     }
# ]




# SET LEVEL
# level_map = {
#     'level_1': {
#         'background': [ "<  >" ],
#         'platform': [ "< NewPlatform Sprite(in 0 groups) >"],
#         'players': [ "< characters.character.Character object at 0x000001BA5DDC3E80 >" ],
#         'enemies': [ "< characters.enemy.Enemy object at 0x000001BA5DDC3F40 >" ],
#         'coins': [ "< coin.Coin object at 0x000001BA5DDCD070 >"]
#     },
#     'level_2': {
#         'platform': [ "< NewPlatform Sprite(in 0 groups) >"],
#         'players': [ "< characters.character.Character object at 0x000001BA5DDD0A90 >" ],
#         'enemies': [],
#         'coins': []
#     }
# }

# SET LEVEL
""" level_map = [
    {
        'platform': game_tiles,
        'players': l_players,
        'enemies': l_enemies,
        'coins': l_coins,
    },
    {
        'platform': game_tiles,
        'players': l_players,
        'enemies': l_enemies,
        'coins': l_coins,
    }
] """

