from pico2d import *
import game_world
import play_state

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
        game_world.add_collision_pairs(play_state.attacks, play_state.enemies, 'attacks:enemies')

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())


    def update(self):
        self.y += self.speed

        if self.y > 1020:
            game_world.remove_object(self)

    def get_bb(self):  # bb = Bounding Box(충돌 범위)
        return self.x-25, self.y-30, self.x+25, self.y+50

    def handle_collision(self, other, group):
        print('Bullet')
        pass
