import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()


        # Load the image
        self.image = pygame.image.load('images/14.bmp')

        # Scale the image to the desired size (for example, half of the original size)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ship's position
        self.x = float(self.rect.x)

        #Movement Flags
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right <self.screen_rect.right:
            self.x +=self.settings.ship_speed
        if self.moving_left and self.rect.left >0:
            self.x -=self.settings.ship_speed

        #updating rect object from self .x.
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
