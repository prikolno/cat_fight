import database
import pygame
import thorpy
from .form import Form
import forms


class MainMenu(Form):
    def __init__(self, app):
        super(MainMenu, self).__init__(app)

        img = database.get_image('gui_start.png')
        img1 = pygame.transform.scale(img.subsurface((0, 0, 64, 16)), (256, 64))
        img2 = pygame.transform.scale(img.subsurface((64, 0, 64, 16)), (256, 64))
        img3 = pygame.transform.scale(img.subsurface((128, 0, 64, 16)), (256, 64))
        button_play = thorpy.ImageButton("", img1, img2, img3)
        button_play.at_unclick = self.button_play_at_unclick

        img = database.get_image('gui_multiplayer.png')
        img1 = pygame.transform.scale(img.subsurface((0, 0, 64, 16)), (256, 64))
        img2 = pygame.transform.scale(img.subsurface((64, 0, 64, 16)), (256, 64))
        img3 = pygame.transform.scale(img.subsurface((128, 0, 64, 16)), (256, 64))
        button_multiplayer = thorpy.ImageButton("", img1, img2, img3)
        button_multiplayer.at_unclick = self.button_multiplayer_at_unclick

        img = database.get_image('gui_quit.png')
        img1 = pygame.transform.scale(img.subsurface((0, 0, 64, 16)), (256, 64))
        img2 = pygame.transform.scale(img.subsurface((64, 0, 64, 16)), (256, 64))
        img3 = pygame.transform.scale(img.subsurface((128, 0, 64, 16)), (256, 64))
        button_quit = thorpy.ImageButton("", img1, img2, img3)
        button_quit.at_unclick = self.button_quit_at_unclick

        main_group = thorpy.Group([button_play, button_multiplayer, button_quit])
        main_group.center_on(self.app.window)

        self.updater = main_group.get_updater()

    def button_play_at_unclick(self):
        self.app.change_form(forms.Game(self.app))

    def button_multiplayer_at_unclick(self):
        self.app.change_form(forms.Multiplayer(self.app))

    def button_quit_at_unclick(self):
        self.app.running = False
