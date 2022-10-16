import pico2d
from pico2d import *
import game_framework


class Background:
    def __init__(self):
        self.image = load_image('background_forest.png')

    def draw(self):
        self.image.clip_draw(0, 0, background_image_width, background_image_height, background_image_width, background_image_height, background_image_width*2, background_image_height*2)


class Player:
    def __init__(self):
        self.image = load_image('player_image.png')

    def update(self):
        global x, y
        # 맵 밖으로 못가게 함
        if x > background_image_width*2:
            x = background_image_width*2
        elif x < 0:
            x = 0
        if y > background_image_height*2:
            y = background_image_height*2
        elif y < 0:
            y = 0

    def draw(self):
        self.image.draw(x, y)


class NoneAttack:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

class Attack:
    def __init__(self):
        self.image = load_image('attack_image.png')
        self.attack_x = x
        self.attack_y = y + 50

    def update(self):
        self.attack_y += 2

    def draw(self):
        self.image.draw(self.attack_x, self.attack_y)


class SkillAttack:
    def __init__(self):
        self.image = load_image('skill_attack_image.png')
        self.attack_x = x
        self.attack_y = y + 50

    def update(self):
        self.attack_y += 2

    def draw(self):
        self.image.draw(self.attack_x, self.attack_y)

def handle_events():
    global running
    global x, y
    global attacks

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

        if event.type == pico2d.SDL_MOUSEMOTION:
            x, y = event.x, background_image_height*2 - 1 - event.y

        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == pico2d.SDL_BUTTON_LEFT:
                # attacks = Attack()
                attacks.append(Attack())
            elif event.button == pico2d.SDL_BUTTON_RIGHT:
                # attacks = SkillAttack()
                attacks.append(SkillAttack())

background_image_width = 384
background_image_height = 512
running = True
player = None
background = None
x, y = 0, 0
attacks = []


def enter():
    global running, player, background, x, y, attacks
    running = True
    player = Player()
    background = Background()
    x, y = 0, 0
    attacks = [NoneAttack()]


def exit():
    global player, background, x, y, attacks
    del player
    del background
    del x, y
    del attacks


def update():
    player.update()
    for attack in attacks:
        attack.update()


def draw_world():
    background.draw()
    player.draw()
    for attack in attacks:
        attack.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass


def resume():
    pass


def test_self():
    import sys
    pico2d.open_canvas()
    game_framework.run(sys.modules['__main__'])
    pico2d.close_canvas()

if __name__ == '__main__':
    test_self()