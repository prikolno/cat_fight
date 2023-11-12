import pygame
import thorpy
import database
import engine
from .form import Form
import forms


class Multiplayer(Form):
    def __init__(self, app):
        super(Multiplayer, self).__init__(app)

        text_input_address = thorpy.TextInput('', '123.123.123.123:5000')
        text_input_address.center_on(self.app.window)

        img = database.get_image('gui_select.png')
        img1 = pygame.transform.scale(img.subsurface((0, 0, 64, 16)), (256, 64))
        img2 = pygame.transform.scale(img.subsurface((64, 0, 64, 16)), (256, 64))
        img3 = pygame.transform.scale(img.subsurface((128, 0, 64, 16)), (256, 64))
        button_select = thorpy.ImageButton("", img1, img2, img3)
        button_select.at_unclick = self.button_select_at_unclick

        img = database.get_image('gui_back.png')
        img1 = pygame.transform.scale(img.subsurface((0, 0, 64, 16)), (256, 64))
        img2 = pygame.transform.scale(img.subsurface((64, 0, 64, 16)), (256, 64))
        img3 = pygame.transform.scale(img.subsurface((128, 0, 64, 16)), (256, 64))
        button_back = thorpy.ImageButton("", img1, img2, img3)
        button_back.at_unclick = self.button_back_at_unclick

        group_form = thorpy.Group([text_input_address, button_select, button_back])
        group_form.center_on(self.app.window)

        main_group = thorpy.Group([group_form], None, (0, 0))

        self.updater = main_group.get_updater()

    def button_select_at_unclick(self):
        game = engine.GameOnline(self.app.window)
        self.app.change_form(forms.Game(self.app, game))

    def button_back_at_unclick(self):
        self.app.change_form(forms.MainMenu(self.app))
