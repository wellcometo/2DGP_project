from pico2d import *
import game_framework

class Background:
    def __init__(self):
        self.image = load_image('background_wheat_field.png')

    def draw(self):
        self.image.draw(1280, 1706)


class Player:
    def __init__(self):
        self.x, self.y = 1280/2, 50
        self.frame = 0