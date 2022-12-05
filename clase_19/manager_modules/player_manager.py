from bullets import Bullet
from constantes import *

class PlayerManager():
    def __init__(self, game_manager, bullet_manager, music_manager):
        self.__game_manager = game_manager
        self.__bullet_manager = bullet_manager
        self.music_manager = music_manager
        self.is_collide_enemy = False


    def sound_effect(self, id):
        self.music_manager.update(id)

    def shoot(self, entity, instance, pos_x, flip, delta_ms=''):
        shoot = Bullet(entity, instance, pos_x, flip)
        self.__bullet_manager.bullet_group.append(shoot)


    def check_outside_map(self, entity):
        for player in self.__game_manager.list_pjs:
            if player.rect_collition.top > ANCHO_VENTANA and player.entity == entity:
                player.life = 0

    
    def get_damage(self, entity, enemy_entity):
        for i, player in enumerate(self.__game_manager.list_pjs):
            for enemy in self.__game_manager.list_enemies:
                if player.entity == entity and enemy.entity == enemy_entity:
                    player.life -= 1
                    pass
                if player.life <= 0:
                    self.music_manager.update('explosion')
                    self.__game_manager.eliminate_player(i)
                    break
    
    def get_exp(self, entity, points): # REVISAR - no lo estoy usando
        for i, player in enumerate(self.__game_manager.list_pjs):
            if player.entity == entity:
                player.score += points
                break

    """ def horizontal_collide_enemy(self):
        self.is_collide_enemy = False
        for i, player in enumerate(self.__game_manager.list_pjs):
            for x, enemy in enumerate(self.__game_manager.list_enemies):
                # Chocar con enemigo
                if player.rect.colliderect(enemy.rect_collition):
 
                    player.rect_collition.centerx = player.rect.centerx
                    self.is_collide_enemy = True
                # self.is_collide_x = True

    def vertical_collide_enemy(self):
        # self.is_collide_enemy = False
        for i, player in enumerate(self.__game_manager.list_pjs):
            for x, enemy in enumerate(self.__game_manager.list_enemies):
                # Chocar con enemigo
                if player.rect.colliderect(enemy.rect_collition):

                    # player.rect_collition.centery = player.rect.centery
                    player.direction.y = 0

                    # self.is_collide_enemy = True
                # self.is_collide_x = True """


    def update(self):
        # print(self.in_vision)
        # self.detect_vision()
        # self.move_rect_x()
        pass
        

    def draw(self):

        pass
