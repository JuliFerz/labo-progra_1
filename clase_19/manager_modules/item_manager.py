
class ItemManager():
    def __init__(self, game_manager, music_manager):
        self.__game_manager = game_manager
        self.music_manager = music_manager

    def collide_rect(self):
        for i, item in enumerate(self.__game_manager.items):
            for player in self.__game_manager.list_pjs:

                if player.rect_collition.colliderect(item.rect):
                    self.music_manager.update('item')
                    player.score += item.points
                    player.life += item.health
                    player.qty_bullets += item.bullets

                    if player.life > player.max_life:
                        player.life = player.max_life
                    if player.qty_bullets >= player.max_qty_bullets:
                        print('entre aca')
                        print(player.qty_bullets, player.max_qty_bullets)
                        player.qty_bullets = player.max_qty_bullets

                    self.__game_manager.items.pop(i)
