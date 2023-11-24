import math
import pygame
import config
import database
import engine.bullet


class Weapon(pygame.sprite.Sprite):
    def __init__(self, game):
        super(Weapon, self).__init__()

        self.game = game

        self.rect = pygame.rect.Rect(0, 0, 200, 200)
        self.rect_original = pygame.rect.Rect(0, 0, 200, 200)
        self.angle = 0
        self.image = pygame.surface.Surface((200, 200))
        self.image_original = pygame.transform.scale(database.get_image('weapon_colt.png', True), (200, 200))

        self.damage = 10

        self.shoot_i = 0
        self.shoot_rate = 0.3 * config.FPS

        self.bullet_spawn = (100, 0)

    def shoot(self, player):
        if self.shoot_i == 0:
            self.shoot_i = self.shoot_rate

            spawn = (
                self.rect.centerx + 20 * math.cos(self.angle / 180 * math.pi),
                self.rect.centery - 20 * math.sin(self.angle / 180 * math.pi)
            )

            self.game.bullets.add(engine.bullet.Bullet(self.game, player, spawn, self.angle, self.damage))

    def _render(self):
        img = self.image_original
        img = pygame.transform.rotate(img, self.angle)
        center = self.rect.center
        self.rect = img.get_rect()
        self.rect.center = center
        self.image = img

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        self.angle = -math.atan2(mouse_pos[1] - self.rect.centery, mouse_pos[0] - self.rect.centerx) * 180 / math.pi

        self._render()

        if self.shoot_i > 0:
            self.shoot_i -= 1
