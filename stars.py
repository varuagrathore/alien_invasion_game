# stars.py
import pygame
from random import randint
import os

class Stars:

    def __init__(self, ai_game):
        """Initialize the stars and set their starting positions."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        
        self.star_image = pygame.image.load(os.path.join('images', 'star.bmp')).convert_alpha()
        self.star_image = pygame.transform.scale(self.star_image, (10, 10))  # Scale down to 10x10 pixels
        self.star_rect = self.star_image.get_rect()

        self.stars = self._create_stars()

    def _create_stars(self):
        """Create a grid of stars with random positions."""
        star_spacing = 40
        num_stars_x = self.settings.screen_width // star_spacing
        num_stars_y = self.settings.screen_height // star_spacing

        stars = []
        for row in range(num_stars_y):
            for col in range(num_stars_x):
                x = col * star_spacing + randint(-10, 10)
                y = row * star_spacing + randint(-10, 10)
                stars.append((x, y))

        return stars

    def draw_stars(self):
        """Draw the stars on the screen."""
        for star in self.stars:
            self.screen.blit(self.star_image, star)
