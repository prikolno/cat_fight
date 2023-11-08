import os
import pygame
import thorpy
import config
import database
from app import App


if __name__ == '__main__':
    config.DIR_PATH = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

    pygame.init()

    window = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), pygame.DOUBLEBUF)
    pygame.display.set_caption('Game')
    pygame.display.set_icon(database.get_image('icon.ico', True))
    window.set_alpha(None)

    thorpy.init(window)

    app = App(window)
    app.run()

    pygame.quit()
