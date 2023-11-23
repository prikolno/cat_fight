import pygame
import config


class Entity(pygame.sprite.Sprite):
    def __init__(self, game, image, rect, collide):
        super().__init__()

        self.game = game

        self.image = image
        self.rect = rect
        self.collide = collide
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

    def update(self, surface=None):
        self._handle_moving()
