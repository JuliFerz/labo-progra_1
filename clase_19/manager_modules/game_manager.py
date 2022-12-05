from sql import Sql

class GameManager:
    def __init__(self, list_pjs, list_enemies, items, list_platform, surface):
        self.list_pjs = list_pjs
        self.list_enemies = list_enemies
        self.items = items
        self.list_platform = list_platform
        self.surface = surface

        # NUEVO
        self.ok_enemies = False
        self.ok_items = False
        self.ok_fruits = False
        self.finish = False
        self.win = False
        self.lose = False
        self.sql = Sql()
        # print('a', self.list_pjs)

    def check_win(self):
        # print(self.items[0].)
        
        if len(self.list_enemies) == 0:
            self.ok_enemies = True
        if len(self.items) == 0:
            self.ok_items = True

        if self.ok_enemies and self.ok_items:
            self.win = True
            self.finish = True
    
    def check_lose(self):
        for player in self.list_pjs:
            if player.life <= 1:
                self.lose = True
                self.finish = True

    def create_record(self, name, score, time):
        self.sql.create_record(name, score, time)
        pass




    """ def eliminate_enemy(self, entity):
        print('PRIMEROOOO', self.list_enemies)
        # value_deleted_item = self.list_enemies[entity]
        value_deleted_item = self.list_enemies[entity].values()
        key_deleted_item = self.list_enemies[entity].keys()
        number_deleted_item = re.findall('[0-9]', str(self.list_enemies[entity].keys()))[0]

        del self.list_enemies[entity] # entity -> 0 #
        
        if self.list_enemies:
            l_keys = list(self.list_enemies)

            # if len(self.list_enemies) > 1:
            for i, enemy in enumerate(self.list_enemies):

                print('AAAAAAAA', self.list_enemies)
                # for key in enemy.keys():
                #     print('CCCCCC',key)
                #     print(self.list_enemies[i])
                #     test = self.list_enemies.pop(i)
                #     enemy.update({[f'enemy_{i+1}']: test})
                #     enemy[f'enemy_{i+1}'] = self.list_enemies.pop(i)
                #     print('CCCCCC',key)

                self.list_enemies.append({f'enemy_{i+1}': enemy[f'enemy_{i+2}']}) #

                print('BBBBBBBB', self.list_enemies)
                if f'enemy_{i+2}' in enemy:
                    self.list_enemies.pop(i)

                print('BBBBBBBB', self.list_enemies) """

    def eliminate_enemy(self, index):
        del self.list_enemies[index] # entity -> 0 #

    def eliminate_player(self, index):
        del self.list_pjs[index] # entity -> 0 #

'''
# deleted_item = {'enemy_2': <characters.enemy.Enemy object at 0x0000022E3DC7C220>}

deleted_item = <characters.enemy.Enemy object at 0x0000022E3DC7C220>
key_deleted_item = 'enemy_2'
i = 0

i+1 = 1
i+2 = 2
[
    {'enemy_1': <characters.enemy.Enemy object at 0x0000022E3DC6A8B0>},
    {'enemy_3': <characters.enemy.Enemy object at 0x0000022E3DC888AG>}
]
'''

'''
[
    {'enemy_1': <characters.enemy.Enemy object at 0x0000022E3DC6A8B0>},
    {'enemy_2': <characters.enemy.Enemy object at 0x0000022E3DC888AG>},
    {'enemy_3': <characters.enemy.Enemy object at 0x0000022E3DC888AG>}
]
'''