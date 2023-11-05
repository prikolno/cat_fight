from imports import *


def get_image(name: typing.Text, alpha: bool = False) -> pygame.surface.Surface | pygame.surface.SurfaceType:
    img = pygame.image.load(f'{config.DIR_PATH}\\images\\{name}')
    img = img.convert_alpha() if alpha else img.convert()

    return img
