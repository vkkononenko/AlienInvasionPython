import pygame

class Ship():
    def __init__(self, ai_game):
        self.moving_right = 0
        self.moving_up = 0
        self.sheep_speed = 1
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.moving_right * self.sheep_speed
        self.y += self.moving_up * self.sheep_speed
        if self.moving_right > 0 and self.rect.right > self.screen_rect.right:
            self.moving_right = 0
        elif self.moving_right < 0 and self.rect.left < 0:
            self.moving_right = 0
        elif self.moving_up < 0 and self.rect.top - 10 < self.screen_rect.top:
            self.moving_up = 0
        elif self.moving_up > 0 and self.rect.bottom + 10 > self.screen_rect.bottom:
            self.moving_up = 0
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)