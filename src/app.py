import form
from imports import *


class App:
    def __init__(self):
        self.window = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), pygame.DOUBLEBUF)
        pygame.display.set_caption('Game')
        pygame.display.set_icon(database.get_image('icon.ico', True))

        self.window.set_alpha(None)

        # thorpy.init(self.window)

        self.running = True

        self.clock = pygame.time.Clock()

        self.__current_form = form.FormGame(self)

    def run(self):
        while self.running:
            self.clock.tick(config.FPS)

            pygame.display.set_caption(f'FPS: {self.clock.get_fps():.0f}')

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.__current_form.update(events)

            pygame.display.update()

