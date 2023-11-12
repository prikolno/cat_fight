import pygame
from constants import *


class KeysInputHandler:
    def __init__(self):
        self.keys = dict()

    def __getitem__(self, item):
        if item in self.keys:
            return self.keys[item]
        else:
            return KEY_STATUS_RELEASED

    def __iter__(self):
        return self.keys.items()

    def handle_events(self, events):
        for k, v in self.keys.items():
            if v == KEY_STATUS_DOWN:
                self.keys[k] = KEY_STATUS_PRESSED
            elif v == KEY_STATUS_UP:
                self.keys[k] = KEY_STATUS_RELEASED

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.keys[event.key] = KEY_STATUS_DOWN
            elif event.type == pygame.KEYUP:
                self.keys[event.key] = KEY_STATUS_UP
