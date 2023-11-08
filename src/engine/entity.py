import pygame
from constants import *
import config


class Entity(pygame.sprite.Sprite):
    def __init__(self, game, pos, sheet):
        super().__init__()

        self.game = game

        self.image = pygame.Surface((100, 100))
        self.rect = pygame.Rect(pos[0], pos[1], 100, 110)
        self.collide = pygame.Rect(self.rect.left + 25, self.rect.top + 30, 50, 68)
        self.direction = 1
        self.velocity = [0.0, 0.0]
        self.max_velocity = [10000 / config.FPS, 10000 / config.FPS]
        self.acceleration = [0.0, config.G / config.FPS]

    def move(self, x, y):
        self.rect = self.rect.move(x, y)
        self.collide = self.collide.move(x, y)

    def move_ip(self, x, y):
        self.rect.move_ip(x, y)
        self.collide.move_ip(x, y)

    def push(self, dx, dy):
        self.velocity[0] += dx
        self.velocity[1] += dy

    def _handle_moving(self):
        for i in range(2):
            self.velocity[i] += self.acceleration[i]

            if abs(self.velocity[i]) > self.max_velocity[i]:
                self.velocity[i] = self.max_velocity[i] * (1 if self.velocity[i] > 0 else -1)

        self.move(*self.velocity)

    def update(self, tiles=None, surface=None):
        self._handle_moving()
