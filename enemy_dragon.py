from pico2d import *
import game_framework
import play_state

class Lv1Dragon:
    def __init__(self):
        self.image = load_image('white_dragon.png')
        self.x, self.y = play_state.background_image_width, play_state.background_image_height*2
    def update(self):
        self.y -= 1

    def draw(self):
        self.image.draw(self.x, self.y)