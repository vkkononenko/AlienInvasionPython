import sys
import pygame
import settings as settings
from alien import Alien
from bullet import Bullet
from ship import Ship as ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.create_fleet()  # Создаем флот сразу при запуске

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()

            # Если флот уничтожен, создаём новый
            if len(self.aliens) == 0:
                self.create_fleet()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)
        self.ship.update()

    def check_keydown(self, event):
        if event.key == pygame.K_w:
            self.ship.moving_up = -1
        elif event.key == pygame.K_s:
            self.ship.moving_up = 1
        elif event.key == pygame.K_a:
            self.ship.moving_right = -1
        elif event.key == pygame.K_d:
            self.ship.moving_right = 1
        elif event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullets_allowed:
                self.fire_bullet()

    def check_keyup(self, event):
        if event.key in (pygame.K_w, pygame.K_s):
            self.ship.moving_up = 0
        elif event.key in (pygame.K_a, pygame.K_d):
            self.ship.moving_right = 0

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        self.bullets.update()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.update()
        self.aliens.draw(self.screen)

        font = pygame.font.SysFont(None, 36)
        text_lives = font.render(f"Aliens missed left: {int(self.settings.aliens_missed)}", True, (255, 0, 0))
        self.screen.blit(text_lives, (10, 10))
        text = font.render(f"Aliens killed: {int(self.settings.aliens_killed)}", True, (255, 0, 0))
        self.screen.blit(text, (10, 40))

        # Проверка столкновений
        collisions_bullets = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if self.settings.aliens_missed <= 0:
            self.draw_game_over()
            pygame.display.flip()
            pygame.time.delay(2000)  # Пауза 2 секунды
            pygame.quit()
            sys.exit()

        if collisions_bullets:
            for bullet, aliens_killed in collisions_bullets.items():
                self.settings.aliens_killed += len(aliens_killed) / 4

        pygame.display.flip()

    def fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def create_fleet(self):
        ship_height = self.ship.rect.height

        alien = Alien(self)
        self.settings.alien_speed += 0.05
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_aliens_y = available_space_y // (2 * alien_height)

        for row_number in range(number_aliens_y):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_width, alien_height, alien_number, row_number)

    def create_alien(self, alien_width, alien_height, alien_number, row_number):
        alien = Alien(self)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def draw_game_over(self):
        font = pygame.font.SysFont(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 2))
        self.screen.blit(text, text_rect)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
