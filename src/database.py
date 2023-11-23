import pygame
from typing import Text, IO
import config


def get_image(name: Text, alpha: bool = False) -> pygame.surface.Surface | pygame.surface.SurfaceType:
    img = pygame.image.load(f'{config.DIR_PATH}\\images\\{name}')
    img = img.convert_alpha() if alpha else img.convert()

    return img


def get_map(name: Text) -> IO:
    return open(f'{config.DIR_PATH}\\maps\\{name}', 'r')
