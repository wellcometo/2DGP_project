from pico2d import *
import game_world


# Attack Speed
PIXEL_PER_METER = (50.0 / 3.0)  # 50 pixel = 3 m
ATTACK_SPEED_KMPH = 0.3  # km Per Hour
ATTACK_SPEED_MPM = (ATTACK_SPEED_KMPH * 1000.0 / 60.0)
ATTACK_SPEED_MPS = (ATTACK_SPEED_MPM / 60.0)
ATTACK_SPEED_PPS = (ATTACK_SPEED_MPS * PIXEL_PER_METER)


class Attack:
    image = None

    def __init__(self, x, y):
        if Attack.image == None:
            Attack.image = load_image('images/attack_image.png')
        self.x, self.y, self.speed = x, y + 50, ATTACK_SPEED_PPS

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y += self.speed

        if self.y > 1020:
            game_world.remove_object(self)
