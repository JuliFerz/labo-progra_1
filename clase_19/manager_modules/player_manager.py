from bullets import Bullet

class PlayerManager():
    def __init__(self, game_manager, bullet_manager):
        self.__game_manager = game_manager
        self.__bullet_manager = bullet_manager
        self.is_collide_enemy = False

    def shoot(self, entity, pos_x, flip, delta_ms=''):
        # print(entity)
        shoot = Bullet(entity, pos_x, flip)
        self.__bullet_manager.bullet_group.append(shoot)


    
    def get_damage(self, entity):
        for i, player in enumerate(self.__game_manager.list_pjs):
            if player.entity == entity:
                player.life -= 1
                pass
            if player.life <= 0:
                self.__game_manager.eliminate_player(i)
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
