class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.ship_speed = 1.5

        # Bullet Settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (253, 253, 253)
        self.bullets_allowed = 3

        #alien speed 
        self.alien_speed =1.0
        self.fleet_drop_speed =10
        #fleet direction 1 is for right and -1 for left
        self.fleet_direction=1
