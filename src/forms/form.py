from typing import List
import pygame


class Form:
    def __init__(self, app):
        self.app = app
        self.updater = None

    def update(self, events: List[pygame.event.Event], mouse_rel: tuple[int, int]):
        if self.updater is not None:
            self.updater.update()

        pygame.display.update()

