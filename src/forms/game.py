import engine
import pygame
from typing import List
from .form import Form


class Game(Form):
    def __init__(self, app):
        super(Game, self).__init__(app)

        self.game = engine.Game(self.app.window)
        self.game.create()

    def update(self, events: List[pygame.event.Event], mouse_rel: tuple[int, int]):
        self.game.update(events)
        # super(FormGame, self).update(events, mouse_rel)
