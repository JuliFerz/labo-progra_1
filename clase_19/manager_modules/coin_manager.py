
class CoinManager():
    def __init__(self, game_manager):
        self.__game_manager = game_manager

    def collide_rect(self):
        for i, coin in enumerate(self.__game_manager.coins):
            for player in self.__game_manager.list_pjs:

                if player.rect_collition.colliderect(coin.rect):
                    self.__game_manager.coins.pop(i)
