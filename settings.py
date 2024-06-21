class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.score_color = (255, 255, 255)
        
        self.ship_limit =3

        # Bullet Settings
        self.bullet_speed = 1.5
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (253, 253, 253)
        self.bullets_allowed = 3

        #alien speed 
        self.alien_speed =1.0
        self.fleet_drop_speed =10
        #fleet direction 1 is for right and -1 for left
        self.fleet_direction=1

        #How quickly the game speed up 
        self.speedup_scale = 1.1
        self.score_scale =1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed =1.0
        self.alien_points =  50
        #fleet direction 1 is for right and -1 for left
        self.fleet_direction=1
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.aliens_points  =  int(self.alien_points*self.score_scale)
        print(self.alien_points)

