from imports import *


if __name__ == '__main__':
    path = os.path.split(os.path.realpath(__file__))
    path = os.path.split(path[0])
    config.DIR_PATH = path[0]

    pygame.init()

    app = App()
    app.run()

    pygame.quit()
