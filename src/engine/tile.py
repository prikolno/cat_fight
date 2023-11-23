import pygame
import config
import database


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], image: pygame.surface.Surface):
        super().__init__()

        size = 50

        self.collide = pygame.Rect(pos[0], pos[1], size, size)
        self.rect = pygame.Rect(pos[0], pos[1], size, size)

        img_size = [16, 16]
        sheet = database.get_image("tileset_forest.png", True)

        # img = sheet.subsurface(pygame.Rect(128 + img_size[0], 48, *img_size))
        # img = pygame.transform.flip(img, False, False)
        self.image = pygame.transform.scale(image, (size, size))

    def update(self):
        pass
