from pico2d import *
import game_framework

class Background:
    def __init__(self):
        self.image = load_image('background_forest.png')

    def draw(self):
        self.image.draw(384*2, 512*2)


class Player:
    def __init__(self):
        self.x, self.y = 384, 50
        self.player_image = load_image('player_image.png')
        self.attack_image = load_image('attack_image')

    def update(self):
        if self.x > 384*2:
            self.x = 384*2
        elif self.x < 0:
            self.x = 0
        if self.y > 512*2:
            self.y = 384*2
        elif self.y < 0:
            self.y = 0

    def draw(self):
        if 