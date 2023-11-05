from imports import *


class Form:
    def __init__(self, app):
        self.app = app
        self.updater = None

    # def update(self, events: typing.List[pygame.event.Event], mouse_rel: tuple[int, int]):
    #     if self.updater is not None:
    #         self.updater.update()

        # pygame.display.update()


class FormMainMenu(Form):
    def __init__(self, app):
        super(FormMainMenu, self).__init__(app)

        img1 = database.get_image("gui_start_1.png")
        img1 = pygame.transform.scale(img1, (256, 64))
        img2 = database.get_image("gui_start_2.png")
        img2 = pygame.transform.scale(img2, (256, 64))
        img3 = database.get_image("gui_start_3.png")
        img3 = pygame.transform.scale(img3, (256, 64))
        button_play = thorpy.ImageButton("", img1, img2, img3)
        button_play.at_unclick = self.button_play_at_unclick

        img1 = database.get_image("gui_multiplayer_1.png")
        img1 = pygame.transform.scale(img1, (256, 64))
        img2 = database.get_image("gui_multiplayer_2.png")
        img2 = pygame.transform.scale(img2, (256, 64))
        img3 = database.get_image("gui_multiplayer_3.png")
        img3 = pygame.transform.scale(img3, (256, 64))
        button_multiplayer = thorpy.ImageButton("", img1, img2, img3)
        button_multiplayer.at_unclick = self.button_multiplayer_at_unclick

        img1 = database.get_image("gui_quit_1.png")
        img1 = pygame.transform.scale(img1, (256, 64))
        img2 = database.get_image("gui_quit_2.png")
        img2 = pygame.transform.scale(img2, (256, 64))
        img3 = database.get_image("gui_quit_3.png")
        img3 = pygame.transform.scale(img3, (256, 64))
        button_quit = thorpy.ImageButton("", img1, img2, img3)
        button_quit.at_unclick = self.button_quit_at_unclick

        main_group = thorpy.Group([gif_background, button_play, button_multiplayer, button_quit])
        main_group.center_on(self.app.window)

        self.updater = main_group.get_updater()

    def button_play_at_unclick(self):
        self.app.change_form(FormGame(self.app))

    def button_multiplayer_at_unclick(self):
        self.app.change_form(FormMultiplayer(self.app))

    def button_quit_at_unclick(self):
        self.app.run = False


class FormMultiplayer(Form):
    def __init__(self, app):
        super(FormMultiplayer, self).__init__(app)

        # img = database.get_image('desert_a.png')
        # img = pygame.transform.scale(img, (config.WINDOW_WIDTH/2, config.WINDOW_HEIGHT/2))
        # image_background = thorpy.Image(img)
        # image_background.center_on(self.app.window)
        # image_background.set_topright(0, 0)

        text_input_address = thorpy.TextInput('', '123.123.123.123:5000')
        text_input_address.center_on(self.app.window)

        img1 = database.get_image("gui_back_1.png")
        img1 = pygame.transform.scale(img1, (256, 64))
        img2 = database.get_image("gui_back_2.png")
        img2 = pygame.transform.scale(img2, (256, 64))
        img3 = database.get_image("gui_back_3.png")
        img3 = pygame.transform.scale(img3, (256, 64))
        button_back = thorpy.ImageButton("", img1, img2, img3)
        button_back.at_unclick = self.button_back_at_unclick

        group_form = thorpy.Group([text_input_address, button_back])
        group_form.center_on(self.app.window)

        main_group = thorpy.Group([group_form], None, (0, 0))
        # main_group.set_topright()

        self.updater = main_group.get_updater()

    def button_back_at_unclick(self):
        self.app.change_form(FormMainMenu(self.app))


class FormGame(Form):
    def __init__(self, app):
        super(FormGame, self).__init__(app)

        self.game = Game(self.app.window)
        self.game.create()

    def update(self, events: typing.List[pygame.event.Event]):
        self.game.update(events)
        # super(FormGame, self).update(events, mouse_rel)
