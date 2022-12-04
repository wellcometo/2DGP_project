from pico2d import *
import game_framework
import play_state

#
# class NoneMeteo:
#     def __init__(self):
#         pass
#
#     def update(self):
#         pass
#
#     def draw(self):
#         pass


class Meteo:
    def __init__(self):
        self.image = load_image('meteo01.png')
        self.x, self.y = enemy_spawn_x*5, background_mid_y * 2

    def update(self):
        self.y -= 1

    def draw(self):
        self.image.clip_draw(0, 0, 230, 233, self.x, self.y, 128, 128)


background_mid_x = 384  # = play_state.background_image_width = 384
background_mid_y = 512  # = play_state.background_image_height = 512
enemy_spawn_x = background_mid_x / 5  # 스폰 x는 1, 3, 5(중앙), 7, 9
