class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed_factor = 4
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed_factor = 5
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = 250, 250, 250
        self.bullets_allowed = 10