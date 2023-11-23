from typing import Text
import json
import pygame
import config
import database
from engine.tile import Tile


class Map:
    def __init__(self, name: Text):
        file = database.get_map(name)
        data = json.load(file)

        self.size = data['size']
        self.matrix = data['map']
        self.background = database.get_image(data['background'])
        self.sheet = database.get_image(data['tile_set'], True)
        self.rects = data['rects']

        self.tiles = pygame.sprite.Group()

    def create(self):
        self.tiles = pygame.sprite.Group()

        s_x = -50
        s_y = -250

        images = {
            k: self.sheet.subsurface(pygame.Rect(self.rects[k])) for k, v in self.rects.items()
        }

        for j, line in enumerate(self.matrix):
            for i, t in enumerate(line.split()):
                if t != '00':
                    self.tiles.add(Tile((s_x + 50 * i, s_y + 50 * j), images[t]))

    def get_background(self):
        surface = self.background
        surface = pygame.transform.scale(surface, (config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        self.tiles.draw(surface)
        return surface
