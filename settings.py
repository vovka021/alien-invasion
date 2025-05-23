class Settings():
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Настройки пришельцев
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 1
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1