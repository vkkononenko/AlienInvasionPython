import json
import os


class Settings:
    def __init__(self):
        if not os.path.exists('settings.json'):
            self.screen_width = 1200
            self.screen_height = 800
            self.bg_color = [230, 230, 230]
            self.filename = 'settings.json'
            self.bullet_speed = 1
            self.bullet_width = 3
            self.bullet_height = 15
            self.bullet_color = 60, 60, 60
            self.bullets_allowed = 3
            self.alien_speed = 0.5
            self.aliens_missed = 5
            self.aliens_killed = 0
            self.init_settings()
        else:
            json_data = self.load_settings()
            self.screen_width = json_data['screen_width']
            self.screen_height = json_data['screen_height']
            self.bg_color = json_data['bg_color']
            self.filename = json_data['filename']
            self.bullet_speed = json_data['bullet_speed']
            self.bullet_width = json_data['bullet_width']
            self.bullet_height =json_data['bullet_height']
            self.bullet_color = json_data['bullet_color']
            self.bullets_allowed = json_data['bullets_allowed']
            self.alien_speed = json_data['alien_speed']
            self.aliens_missed = json_data['aliens_missed']
            self.aliens_killed = json_data['aliens_killed']



    def init_settings(self):
            with open(self.filename, 'w') as f:
                json.dump(self.__dict__, f, indent=4)
    def load_settings(self):
        with open('settings.json', 'r') as f:
            return json.load(f)