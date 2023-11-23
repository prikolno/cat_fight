import pygame
import constants
import database
import engine.player
import engine.game
import engine.map


class GameOnline(engine.Game):
    def create(self):
        self.status = constants.GAME_STATUS_PLAY

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
