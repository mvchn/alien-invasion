import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Single alien class """ 

    def __init__(self, ai_game):
        """ Init alien and set default position """

        super().__init__()
        self.screen = ai_game.screen

        # load alien image and sets int rect attribute
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start eache new alien near the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien horizontal position
        self.x = float(self.rect.x) 

