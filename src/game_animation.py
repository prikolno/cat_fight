from imports import *


class Animation:
    def __init__(self, image: pygame.surface.Surface | pygame.surface.SurfaceType):
        self.image = image
        self.rects = []
        self.i = 0
        self.speed = 0

    def update(self):
        pass
