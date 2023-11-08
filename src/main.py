from imports import *


if __name__ == '__main__':
    path = os.path.split(os.path.realpath(__file__))
    path = os.path.split(path[0])
    config.DIR_PATH = path[0]

    pygame.init()

    window = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), pygame.DOUBLEBUF)
    pygame.display.set_caption('Game')
    pygame.display.set_icon(database.get_image('icon.ico', True))
    window.set_alpha(None)

    thorpy.init(window)

    app = App(window)
    app.run()

    pygame.quit()
