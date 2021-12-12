import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Bullet Behaviour """

    def __init__(self, ai_game):
        """ Create bullt object in current sip position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create bullet rect an set current position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # save bullet position
        self.y = float(self.rect.y)

    def update(self):
        """ Move bullet to top """
        self.y -= self.settings.bullet_speed 
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw bullet on the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)    