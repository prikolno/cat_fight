from imports import *


class App:
    def __init__(self, window):
        self.window = window

        self.running = True

        self.clock = pygame.time.Clock()

        self.__current_form = form.MainMenu(self)

    def change_form(self, new_form):
        self.window.fill((0, 0, 0))
        self.__current_form = new_form

    def run(self):
        while self.running:
            self.clock.tick(config.FPS)

            pygame.display.set_caption(f'FPS: {self.clock.get_fps():.0f}')

            events = pygame.event.get()
            mouse_rel = pygame.mouse.get_rel()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.__current_form.update(events, mouse_rel)

            pygame.display.update()

