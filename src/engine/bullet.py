import math
import pygame.sprite
import config
import database


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, player, pos, angle, damage):
        super(Bullet, self).__init__()

        self.game = game
        self.player = player

        self.image = database.get_image('weapon_bullet.png', True)
        self.rect = pygame.rect.Rect(pos, (16, 16))
        self.angle = angle
        self.speed_max = 10
        self.speed = (self.speed_max * math.cos(self.angle / 180 * math.pi),
                      -self.speed_max * math.sin(self.angle / 180 * math.pi))
        self.damage = damage

    def _handle_collide_tiles(self, tiles):
        for t in tiles:
            if t.rect.collidepoint(self.rect.center):
                self.kill()

    def update(self):
        self._handle_collide_tiles(self.game.tiles)

        if self.rect.centerx <= -100 or self.rect.centerx >= config.WINDOW_WIDTH + 100 or \
                self.rect.centery <= -100 or self.rect.centery >= config.WINDOW_HEIGHT + 100:
            self.kill()

        self.rect = self.rect.move(*self.speed)
