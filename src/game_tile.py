from imports import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, collide: pygame.Rect):
        super().__init__()

        self.collide = collide
        self.rect = collide

        img_size = [16, 16]
        sheet = database.get_image("tileset_forest.png", True)

        img = sheet.subsurface(pygame.Rect(128 + img_size[0], 48, *img_size))
        # img = pygame.transform.flip(img, False, False)
        self.image = pygame.transform.scale(img, (50, 50))

    def update(self):
        pass
