from typing import List
import pygame
import constants
import config
import database
import engine.player
import engine.game
import multiplayer.net
from engine.map import Map


class GameOnline(engine.Game):
    def __init__(self, window):
        super(GameOnline, self).__init__(window)

        self.connection = multiplayer.net.Connection()

    def _connect_to_server(self):
        pass
    
    def create(self):
        self.status = constants.GAME_STATUS_PLAY

        self.map = Map("map_1.json")
        self.background = pygame.surface.Surface((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))

        self.sprites = pygame.sprite.Group()

        k = {
            'left': pygame.K_a,
            'right': pygame.K_d,
            'shift': pygame.K_s,
            'jump': pygame.K_w,
            'punch': pygame.K_e
        }

        e = engine.player.Player(self, (100, 100), k, database.get_image("sprite_vita.png", True))
        self.sprites.add(e)

        _map = engine.map.Map("map_2.json")
        self.tiles = _map.tiles
        self.window.blit(_map.get_background(), (0, 0))

    def update(self, events: List[pygame.event.Event]):
        super(GameOnline, self).update(events)

        ...
