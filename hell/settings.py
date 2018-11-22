class Settings():
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_default_speed = 7
        self.ship_speed_factor = 7
        self.ship_slow_speed = 2.7
        self.ship_limit = 3

        # boss1 settings
        self.boss_speed_factor = 2.5
        self.boss_direction = 1
        self.boss_health = 25000
        
        #bullet settings
        self.bullet_speed_factor = 15
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = 250, 0, 0
        self.bullets_allowed = 200
        self.bullet_dmg = 10

        #boss bullet settings
        self.boss_bullet_speed_factor = 5
        self.boss_bullet_width = 5
        self.boss_bullet_height = 25
        self.boss_bullet_color = 250, 250, 250