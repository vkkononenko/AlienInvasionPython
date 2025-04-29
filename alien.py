import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += float(1 * self.settings.alien_speed)
        self.rect.y = self.y
        if self.rect.y >= self.screen.get_rect().bottom:
            self.kill()
            self.ai_game.settings.aliens_missed -= 1 / 36
