import pygame
from typing import Text
import config


def get_image(name: Text, alpha: bool = False) -> pygame.surface.Surface | pygame.surface.SurfaceType:
    img = pygame.image.load(f'{config.DIR_PATH}\\images\\{name}')
    img = img.convert_alpha() if alpha else img.convert()

    return img
