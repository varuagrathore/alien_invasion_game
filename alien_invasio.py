import sys
import pygame
from settings import Settings
from ship import Ship
from stars import Stars
from button import Button
from game_stats import GameStats
from scoreboard import  Scoreboard
from game_functions import event_handler, bullet_handler, alien_handler, screen_updater, fleet_handler

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Fullscreen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = Stars(self)
        fleet_handler.create_fleet(self)
        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            event_handler.check_events(self)
            if self.stats.game_active:
                self.ship.update()
                bullet_handler.update_bullets(self)
                alien_handler.update_aliens(self)
            screen_updater.update_screen(self)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
