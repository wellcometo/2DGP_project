from pico2d import *
import game_world


class Attack:
    image = None

    def __init__(self, x = 800, y = 300, velocity = 1):
        if Attack.image == None:
            Attack.image = load_image('attack_image.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.y > 1020:
            game_world.remove_object(self)
