import pygame
from constants import *
import config
import database
from typing import List
from .common import KeysInputHandler
from .player import Player
from .tile import Tile
from .map import Map
from .bullet import Bullet
from .weapon import Weapon


class Game:
    def __init__(self, window):
        self.window = window

        self.type = GAME_TYPE_OFFLINE
        self.status = GAME_STATUS_PLAY
        self.keys = KeysInputHandler()

        self.background = None
        self.map = None

        self.sprites = pygame.sprite.Group()
        self.weapons = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

    def create(self):
        self.status = GAME_STATUS_PLAY

        self.map = Map("map_1.json")
        self.background = pygame.surface.Surface((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))

        self.sprites = pygame.sprite.Group()
        self.weapons = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        k = {
            'left': pygame.K_a,
            'right': pygame.K_d,
            'shift': pygame.K_s,
            'jump': pygame.K_w,
            'punch': pygame.K_e
        }

        e = Player(self, (100, 100), k, database.get_image("sprite_vita.png", True))
        self.sprites.add(e)

        e.weapon = Weapon(self)
        e.weapon.rect.center = (e.rect.centerx, e.rect.centery + 20)
        self.weapons.add(e.weapon)

        k = {
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT,
            'shift': pygame.K_DOWN,
            'jump': pygame.K_UP,
            'punch': pygame.K_RCTRL
        }
        e = Player(self, (1000, 100), k, database.get_image("sprite_mort.png", True))
        self.sprites.add(e)

        self.map.create()

        self.background = self.map.get_background()
        self.tiles = self.map.tiles

    def __handle_events(self, events: List[pygame.event.Event]):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.status == GAME_STATUS_PLAY:
                        self.status = GAME_STATUS_PAUSE
                    elif self.status == GAME_STATUS_PAUSE:
                        self.status = GAME_STATUS_PLAY

    def update(self, events: List[pygame.event.Event]):
        self.__handle_events(events)
        self.keys.handle_events(events)

        self.window.blit(self.background, (0, 0))

        if self.status == GAME_STATUS_PLAY:
            self.tiles.update()
            self.sprites.update()
            self.weapons.update()
            self.bullets.update()

            if len(self.sprites) <= 1:
                self.status = GAME_STATUS_OVER
        elif self.status == GAME_STATUS_OVER:
            img = pygame.transform.scale(database.get_image('gui_game_over.png', True), (64*12, 16*12))
            self.window.blit(img, (config.WINDOW_WIDTH / 2 - 64*6, config.WINDOW_HEIGHT / 2 - 16*6))

            img = pygame.transform.scale(database.get_image('gui_press_space_to_restart.png', True), (133 * 6, 7 * 6))
            self.window.blit(img, (config.WINDOW_WIDTH / 2 - 133 * 3, config.WINDOW_HEIGHT / 2 - 7 * 3 + 70))

            if self.keys[pygame.K_SPACE] == KEY_STATUS_UP:
                self.create()

        self.sprites.draw(self.window)
        self.weapons.draw(self.window)
        self.bullets.draw(self.window)
