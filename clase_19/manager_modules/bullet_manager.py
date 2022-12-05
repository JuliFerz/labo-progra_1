from constantes import *

class BulletManager:
    def __init__(self, game_manager, music_manager):
        self.__game_manager = game_manager
        self.music_manager = music_manager
        self.bullet_group = []

    # todas las colisiones de las balas aca
    # cada bala tiene su "dueño" (quien dispara), ya que si yo (pj) mato a un enemigo
    # esa bala al colisionar con el enemigo lo debe hacer desaparecer y darme exp
    def horizontal_collide(self):
        for i, bullet in enumerate(self.bullet_group):
            for tile in self.__game_manager.list_platform:
                if bullet.rect.colliderect(tile.rect_collition):
                    self.music_manager.update('impact')
                    del self.bullet_group[i]
                    break
            
            for enemy in self.__game_manager.list_enemies:
                if bullet.rect.colliderect(enemy.rect_collition):
                    # Subscribe damage
                    enemy._manager.get_damage(enemy.entity, bullet.rect_pj, bullet.pj_instance)
                    self.music_manager.update('impact')
                    del self.bullet_group[i]
                    break

            for player in self.__game_manager.list_pjs:
                if bullet.rect.colliderect(player.rect_collition):
                    if bullet.entity != player.entity:
                        self.music_manager.update('impact')
                        del self.bullet_group[i]
                        break

            if bullet.rect.x >= ANCHO_VENTANA + bullet.rect.w or bullet.rect.x <= 0 - bullet.rect.w:
                self.music_manager.update('impact')
                del self.bullet_group[i]

    def update(self):
        if self.bullet_group:
            for bullet in self.bullet_group:
                bullet.update()
                bullet.draw(self.__game_manager.surface)
            self.horizontal_collide()

    def draw(self):
        pass
