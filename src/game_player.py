from imports import *


class Player(Entity):
    def __init__(self, game, pos, keys, sheet):
        super(Player, self).__init__(game, pos, sheet)

        self._key_left = keys['left']
        self._key_right = keys['right']
        self._key_shift = keys['shift']
        self._key_jump = keys['jump']
        self._key_punch = keys['punch']

    def _handle_input(self):
        if self.game.get_key_status(self._key_left) == KEY_STATUS_PRESSED:
            self.direction = -1
            self.status[ENTITY_STATUS_WALK] = True
        elif self.game.get_key_status(self._key_right) == KEY_STATUS_PRESSED:
            self.direction = 1
            self.status[ENTITY_STATUS_WALK] = True
        else:
            self.status[ENTITY_STATUS_WALK] = False

        if self.game.get_key_status(self._key_jump) == KEY_STATUS_DOWN:
            if self.status[ENTITY_STATUS_ON_GROUND] or self._jump_count < self._jump_count_max:
                self._jump()

        self.status[ENTITY_STATUS_RUN] = self.status[ENTITY_STATUS_WALK] and \
                                         (self.game.get_key_status(self._key_shift) == KEY_STATUS_PRESSED)

        # if self.status[ENTITY_STATUS_RUN]:
        #     self.status[ENTITY_STATUS_WALK] = False

        if self.status[ENTITY_STATUS_RUN]:
            self._run()
        elif self.status[ENTITY_STATUS_WALK]:
            self._walk()

        self.status[ENTITY_STATUS_IDLE] = not (self.status[ENTITY_STATUS_RUN] or self.status[ENTITY_STATUS_WALK])

        if self.game.get_key_status(self._key_punch) == KEY_STATUS_DOWN:
            if self._punch_rate_i == 0 and self.stamina_points >= 10:
                self._punch()

    def update(self, tiles=None, surface=None):
        self._handle_input()

        super(Player, self).update(tiles, surface)
