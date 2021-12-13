import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Single alien class """ 

    def __init__(self, ai_game):
        """ Init alien and set default position """

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load alien image and sets int rect attribute
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start eache new alien near the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien horizontal position
        self.x = float(self.rect.x) 

    def check_edges(self):
        """ Return true if alien stand outside the screen """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """ Move alien to the right """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
