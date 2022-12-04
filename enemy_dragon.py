from pico2d import *
import game_framework
import play_state


# 적 드래곤 레벨 비교 white(Lv1) < green(Lv2) < blue(Lv3) < purple(Lv4) < black(Lv5)
class NoneDragon:
    def __init__(self):
        self.image = load_image('images/green_dragon.png')
        self.x, self.y = enemy_spawn_x * 3, background_mid_y * 2
        pass

    def update(self):
        self.y -= 0.7
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):  # bb = Bounding Box(충돌 범위)
        return self.x-50, self.y-50, self.x+50, self.y+50

    def handle_collision(self, other, group):
        print('Dragon')
        pass

class Dragon:
    def __init__(self):
        self.x, self.y = enemy_spawn_x, background_mid_y*2
        pass

    def update(self):
        self.y -= 0.7
        pass

    def draw(self):
        pass


class Lv1Dragon(Dragon):
    def __init__(self):
        self.image = load_image('images/white_dragon.png')
        self.x = self.x * 1

    def update(self):
        self.y -= 0.7

    def draw(self):
        self.image.draw(self.x, self.y)


class Lv2Dragon:
    def __init__(self):
        self.image = load_image('images/green_dragon.png')
        self.x, self.y = enemy_spawn_x*3, background_mid_y*2

    def update(self):
        self.y -= 0.7

    def draw(self):
        self.image.draw(self.x, self.y)


class Lv3Dragon:
    def __init__(self):
        self.image = load_image('images/blue_dragon.png')
        self.x, self.y = enemy_spawn_x*5, background_mid_y*2

    def update(self):
        self.y -= 0.7

    def draw(self):
        self.image.draw(self.x, self.y)


class Lv4Dragon:
    def __init__(self):
        self.image = load_image('images/purple_dragon.png')
        self.x, self.y = enemy_spawn_x*7, background_mid_y*2

    def update(self):
        self.y -= 0.7

    def draw(self):
        self.image.draw(self.x, self.y)


class Lv5Dragon:
    def __init__(self):
        self.image = load_image('images/black_dragon.png')
        self.x, self.y = enemy_spawn_x*9, background_mid_y*2

    def update(self):
        self.y -= 0.7

    def draw(self):
        self.image.draw(self.x, self.y)


background_mid_x = 384  # = play_state.background_image_width = 384
background_mid_y = 512  # = play_state.background_image_height = 512
enemy_spawn_x = background_mid_x / 5  # 스폰 x는 1, 3, 5(중앙), 7, 9
