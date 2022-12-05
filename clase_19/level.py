# more like level manager
import pygame
from constantes import *
from manager_modules import *

# level_data -> level['level_1']
# surface -> slave_surface
class Level:
    def __init__(self, level_data, running, surface, music_manager):
        ## Level config ##
        self.display_surface = surface
        self.display_rect = self.display_surface.get_rect()

        self.running = running
        self.music_manager = music_manager
        self.level_data = level_data
        self.setup_level(self.level_data)

        # self.world_shift = 0
        # self.background_image = self.get_background(self.level_data['background'])
    
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
        self.items = []

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
        
        ## Items ##
        for item in layout['items']:
            self.items.append(item)

        ## Managers ##
        self.game_manager = Game_mng.GameManager(self.players, self.enemies, self.items, self.tiles, self.display_surface)
        self.bullet_manager = Bullet_mng.BulletManager(self.game_manager, self.music_manager)
        self.enemy_manager = Enemy_mng.EnemyManager(self.game_manager, self.music_manager)
        self.player_manager = Player_mng.PlayerManager(self.game_manager, self.bullet_manager, self.music_manager)
        self.item_manager = Item_mng.ItemManager(self.game_manager, self.music_manager)

        ## Manager subscription (to instances) ##
        self._subscribe_instance(self.players, self.player_manager) # subscribe manager
        self._subscribe_instance(self.enemies, self.enemy_manager) # subscribe manager
        self._subscribe_instance(self.items, self.item_manager) # subscribe manager

        # NUEVO
        # self.game_manager.check_win()


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

        if self.running:
            self.update(delta_ms)
        self.draw(delta_ms)

    def update(self, delta_ms):
        self.game_manager.check_win()
        self.game_manager.check_lose()
        
        if not self.game_manager.finish:
            ## Enemies ## 
            for i, enemy in enumerate(self.enemies):
                enemy.update(delta_ms)
            
            ## Drop items ##
            for item in self.items:
                item.update(delta_ms)

            ## Players ##
            for i, player in enumerate(self.players):
                player.update(delta_ms)

            ## Manager ##
            self.bullet_manager.update()
            self.enemy_manager.update()

    def draw(self, delta_ms):
        ## Level tiles ##
        # método draw heredado de pygame.sprite.Sprite. Dibuja lista de sprites en superficie
        self.tiles.draw(self.display_surface)

         ## Enemies ## 
        for i, enemy in enumerate(self.enemies):
            map(lambda el: el.convert_alpha(),self.enemies[i].animation)
            enemy.draw(self.display_surface)
        
        ## Drop items ##
        for item in self.items:
            item.draw(self.display_surface)

        ## Players ##
        for i, player in enumerate(self.players):
            map(lambda el: el.convert_alpha(), self.players[i].animation)
            player.draw(self.display_surface)
