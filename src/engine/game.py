import pygame
from constants import *
import config
import database
from typing import List
from .common import KeysInputHandler
from .player import Player
from .tile import Tile


class Game:
    def __init__(self, window):
        self.window = window

        self.type = GAME_TYPE_OFFLINE
        self.status = GAME_STATUS_PLAY
        self.keys = KeysInputHandler()

        img = database.get_image("desert_a.png", False)
        self.background = pygame.transform.scale(img, (config.WINDOW_WIDTH, config.WINDOW_HEIGHT))

        self.sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

    def create(self):
        self.status = GAME_STATUS_PLAY

        self.sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

        k = {
            'left': pygame.K_a,
            'right': pygame.K_d,
            'shift': pygame.K_s,
            'jump': pygame.K_w,
            'punch': pygame.K_e
        }

        e = Player(self, (100, 100), k, database.get_image("sprite_vita.png", True))
        self.sprites.add(e)

        k = {
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT,
            'shift': pygame.K_DOWN,
            'jump': pygame.K_UP,
            'punch': pygame.K_RCTRL
        }
        e = Player(self, (1000, 100), k, database.get_image("sprite_mort.png", True))
        self.sprites.add(e)

        level_text = """1111111111111111111111111111
                           1000000000000000000000000001
                           1000000000000000000000000001
                           1000000000000000000000000001
                           1000000000000000000000000001
                           1000000000000000000000000001
                           1000000000000000000000000001
                           1000000000000000000000000001
                           1000000000000111100000000001
                           1000000000000000000000000001
                           1111111110000000000000000001
                           1000000000000000000011110001
                           1000000000000000000000000001
                           1000000000000000000000000001
                           1000000000000111100000000001
                           1000000000000000000000000001
                           1111111000000000000011110001
                           1000000000000000000000000001
                           1000000000000000000000000001
                           1111111111111111111111111111"""

        level = [[int(n) for n in list(line.replace(' ', ''))] for line in level_text.split('\n')]

        s_x = -50
        s_y = -250

        for j, line in enumerate(level):
            for i, t in enumerate(line):
                if t == 1:
                    self.tiles.add(Tile(pygame.Rect(s_x + 50 * i, s_y + 50 * j, 50, 50)))

        self.tiles.draw(self.background)
        self.window.blit(self.background, (0, 0))
        pygame.display.update()

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
            self.sprites.update(tiles=self.tiles)

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
