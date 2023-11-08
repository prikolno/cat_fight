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

        self.status = {
            ENTITY_STATUS_IDLE: False,
            ENTITY_STATUS_WALK: False,
            ENTITY_STATUS_RUN: False,
            ENTITY_STATUS_PUNCH: False,
            ENTITY_STATUS_FIRE: False,
            ENTITY_STATUS_HURT: False,
            ENTITY_STATUS_ON_GROUND: False,
            ENTITY_STATUS_DEATH: False
        }

        self.direction = 1
        self.velocity = [0.0, 0.0]
        self.acceleration = [0.0, config.G / config.FPS]
        self._jump_count = 0
        self._jump_count_max = 2

        self.heal_points_max = 100
        self.heal_points = self.heal_points_max
        self.stamina_points_max = 100
        self.stamina_points = self.stamina_points_max
        self.damage = 1000

        self._punch_rate_i = 0
        self._punch_rate = int(0.25 * config.FPS)

        self._hurt_rate_i = 0
        self._hurt_rate = int(1 * config.FPS)

        self.jump_velocity = 2000 / config.FPS
        self.max_speed_walk = 300 / config.FPS
        self.max_speed_run = 500 / config.FPS
        self.max_velocity = [10000 / config.FPS, 10000 / config.FPS]

        img_size = [24, 24]
        self._sheet = sheet
        self._anim_i = 0
        self._anim_rate = int(0.1 * config.FPS)
        self._anim_idle = [(img_size[0] * i, 0, *img_size) for i in range(0, 3)]
        self._anim_walk = [(img_size[0] * i, 0, *img_size) for i in range(4, 9)]
        self._anim_run = [(img_size[0] * i, 0, *img_size) for i in range(18, 24)]
        self._anim_punch = [(img_size[0] * i, 0, *img_size) for i in range(11, 14)]
        self._anim_hurt = [(img_size[0] * i, 0, *img_size) for i in range(14, 17)]
        self._anim_current = self._anim_idle
        self._anim_len = len(self._anim_current)

    def move(self, x, y):
        self.rect = self.rect.move(x, y)
        self.collide = self.collide.move(x, y)

    def move_ip(self, x, y):
        self.rect.move_ip(x, y)
        self.collide.move_ip(x, y)

    def push(self, dx, dy):
        self.velocity[0] += dx
        self.velocity[1] += dy

    def get_punch(self, other):
        self.change_heal_points(-other.damage)

        self.status[ENTITY_STATUS_HURT] = True

    def death(self):
        self.kill()

    def _walk(self):
        self.velocity[0] = self.max_speed_walk * self.direction

    def _run(self):
        if self.stamina_points < 0.3:
            self.status[ENTITY_STATUS_RUN] = False
            return

        self.velocity[0] = self.max_speed_run * self.direction
        self.change_stamina_points(-0.3)

    def _jump(self):
        if self.stamina_points < 10:
            return

        self.velocity[1] = -self.jump_velocity
        self._jump_count += 1
        self.change_stamina_points(-10)

    def _punch(self):
        if self.stamina_points < 10:
            return

        self.status[ENTITY_STATUS_PUNCH] = True
        self.change_stamina_points(-10)

        for e in self.game.sprites:
            if self is not e:
                dx = (self.rect.left - e.rect.right, self.rect.right - e.rect.left)
                dy = (self.rect.bottom - e.rect.top, self.rect.top - e.rect.bottom)

                if dx[0] < 0 < dx[1] and dy[0] > 0 > dy[1]:
                    dxm = dx[0] if -dx[0] < dx[1] else dx[1]
                    if (dxm < 0) == (self.direction < 0):
                        e.get_punch(self)
                        e.push(5 * self.direction, -10)

    def change_stamina_points(self, value):
        self.stamina_points = max(0, self.stamina_points + value)

    def change_heal_points(self, value):
        self.heal_points = max(0, self.heal_points + value)

        if self.heal_points == 0:
            self.kill()

    def _handle_regeneration(self):
        if self.status[ENTITY_STATUS_IDLE]:
            self.heal_points += 0.1

        self.stamina_points += 0.1

        self.stamina_points = min(self.stamina_points, self.stamina_points_max)
        self.heal_points = min(self.heal_points, self.heal_points_max)

    def _handle_punch_rate(self):
        self._punch_rate_i += 1

        if self._punch_rate_i >= self._punch_rate:
            self.status[ENTITY_STATUS_PUNCH] = False
            self._punch_rate_i = 0

    def _change_anim(self, anim):
        if self._anim_current != anim:
            self._anim_current = anim
            self._anim_len = len(anim)
            self._anim_i = 0

    def _handle_anim(self):
        a = self._anim_idle

        if self.status[ENTITY_STATUS_HURT]:
            a = self._anim_hurt
        elif self.status[ENTITY_STATUS_PUNCH]:
            a = self._anim_punch
        elif self.status[ENTITY_STATUS_RUN]:
            a = self._anim_run
        elif self.status[ENTITY_STATUS_WALK]:
            a = self._anim_walk

        self._anim_i += 1

        if self._anim_i > self._anim_len * self._anim_rate - 1:
            self._anim_i = 0

            if self.status[ENTITY_STATUS_HURT]:
                a = self._anim_idle
                self.status[ENTITY_STATUS_HURT] = False

        self._change_anim(a)

    def _handle_moving(self):
        for i in range(2):
            self.velocity[i] += self.acceleration[i]

            if abs(self.velocity[i]) > self.max_velocity[i]:
                self.velocity[i] = self.max_velocity[i] * (1 if self.velocity[i] > 0 else -1)

        self.move(*self.velocity)

    def _handle_collide_tiles(self, tiles):
        if tiles is None:
            tiles = []

        self.status[ENTITY_STATUS_ON_GROUND] = False

        for t in tiles:
            dx = (self.collide.left - t.collide.right, self.collide.right - t.collide.left)
            dy = (self.collide.bottom - t.collide.top, self.collide.top - t.collide.bottom)

            if dx[0] < 0 < dx[1] and dy[0] > 0 > dy[1]:
                dxm = dx[0] if -dx[0] < dx[1] else dx[1]
                dym = dy[0] if -dy[0] > dy[1] else dy[1]

                if abs(dxm) < abs(dym):
                    cx = -dxm
                    cy = 0
                    self.velocity[0] = 0.0
                else:
                    cx = 0
                    cy = -dym
                    self.velocity[1] = 0.0

                if cy < 0:
                    self._jump_count = 0
                    self.status[ENTITY_STATUS_ON_GROUND] = True

                self.move(cx, cy)

        if self.status[ENTITY_STATUS_ON_GROUND]:
            self._jump_count = 0

    def _render(self):
        surface = pygame.Surface((100, 110), pygame.SRCALPHA)
        img = self._sheet.subsurface(self._anim_current[self._anim_i // self._anim_rate])
        img = pygame.transform.flip(img, self.direction == -1, False)
        img = pygame.transform.scale(img, (100, 100))
        surface.blit(img, (0, 10))

        pygame.draw.rect(surface, (200, 200, 200), (20, 0, 60, 20))

        pygame.draw.rect(surface, (0, 200, 0), (20, 0, 60 * (self.heal_points / self.heal_points_max), 10))
        pygame.draw.rect(surface, (0, 0, 0), (20, 0, 60, 10), 2)

        pygame.draw.rect(surface, (100, 100, 200), (20, 10, 60 * (self.stamina_points / self.stamina_points_max), 10))
        pygame.draw.rect(surface, (0, 0, 0), (20, 10, 60, 10), 2)

        # pygame.draw.rect(surface, (0, 0, 200), pygame.Rect(0, 0, 100, 110), 1)
        # pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(25, 30, 50, 68), 1)

        self.image = surface

    def update(self, tiles=None, surface=None):
        self._handle_moving()
        self._handle_collide_tiles(tiles)
        self._handle_regeneration()

        if self.status[ENTITY_STATUS_ON_GROUND]:
            self.velocity[0] = 0.0

        if self.status[ENTITY_STATUS_PUNCH]:
            self._handle_punch_rate()

        self._handle_anim()
        self._render()
