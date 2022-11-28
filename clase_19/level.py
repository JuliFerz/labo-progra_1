import pygame
from constantes import *
from manager_modules import *


class Level:
    def __init__(self, level_data, surface):
        ## Level config ##
        self.display_surface = surface
        self.level_data = level_data
        self.setup_level(self.level_data)
        # self.background_image = background_image
        # self.world_shift = 0

    def _subscribe_instance(self, list_ent, instance):
        for entity in list_ent:
            entity._manager = instance

    ## Crear todas las instancias ##
    def setup_level(self, layout):
        ## crea variable para grupo de sprites (0 sprites aca) ##
        self.tiles = pygame.sprite.Group()
        # self.players = pygame.sprite.GroupSingle()
        self.players = []
        self.enemies = []
        self.coins = []

        ## Platforms ##
        for platform in layout['platform']:
            self.tiles.add(platform)

        ## Players ##
        for player in layout['players']:
            player.level_tiles = self.tiles
            self.players.append(player)
        
        ## Enemies ##
        for enemy in layout['enemies']:
            enemy.level_tiles = self.tiles
            self.enemies.append(enemy)
        
        ## Coins ##
        for coin in layout['coins']:
            self.coins.append(coin)

        ## Managers ##
        self.game_manager = Game_mng.GameManager(self.players, self.enemies, self.coins, self.tiles, self.display_surface)
        self.bullet_manager = Bullet_mng.BulletManager(self.game_manager)
        self.enemy_manager = Enemy_mng.EnemyManager(self.game_manager)
        self.player_manager = Player_mng.PlayerManager(self.game_manager, self.bullet_manager)
        self.coin_manager = Coin_mng.CoinManager(self.game_manager)

        ## Manager subscription ##
        self._subscribe_instance(self.players, self.player_manager) # subscribe manager
        self._subscribe_instance(self.enemies, self.enemy_manager) # subscribe manager
        self._subscribe_instance(self.coins, self.coin_manager) # subscribe manager

        self.playing = True


    ## mover mapa ##
    """ def scroll_x(self):
        player = self.players.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < 200 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > 1000 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8 """

    def run(self, delta_ms):
        if DEBUG:
            for tile in self.tiles:
                pygame.draw.rect(self.display_surface, RED, tile.rect)
                pygame.draw.rect(self.display_surface, GREEN, tile.rect_collition)

        ## Level tiles ##
        # método draw heredado de pygame.sprite.Sprite. Dibuja lista de sprites en superficie
        self.tiles.draw(self.display_surface)
       
        
        ## Enemies ## 
        for i, enemy in enumerate(self.enemies):
            map(lambda el: el.convert_alpha(),self.enemies[i].animation)
            if self.playing:
                enemy.update(delta_ms)
            enemy.draw(self.display_surface)

        ## Drop items ##
        for coin in self.coins:
            if self.playing:
                coin.update(delta_ms)
            coin.draw(self.display_surface)

        ## Players ##
        for i, player in enumerate(self.players):
            map(lambda el: el.convert_alpha(), self.players[i].animation)
            player.update(delta_ms)
            player.draw(self.display_surface)


        ## Manager ##
        self.bullet_manager.update()
        self.enemy_manager.update()

        # if DEBUG:
        #     for tile in self.tiles:
        #         pygame.draw.rect(self.display_surface, RED, tile.rect)
        #         pygame.draw.rect(self.display_surface, GREEN, tile.rect_collition)
