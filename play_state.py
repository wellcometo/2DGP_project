import pico2d
from pico2d import *
import game_framework


class Background:
    def __init__(self):
        self.image = load_image('background_forest.png')

    def draw(self):
        self.image.clip_draw(0, 0, background_image_width, background_image_height, background_image_width*2, background_image_height*2)


class Player:
    def __init__(self):
        self.player_image = load_image('player_image.png')
        self.attack_image = load_image('attack_image.png')
        self.attack = None

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
        self.player_image.draw(x, y)


def handle_events():
    global running
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif pico2d.SDL_MOUSEMOTION:
            x, y = event.x, background_image_height*2 - 1 - event.y
        elif event.type == SDL_MouseButtonEvent:
            match event.key:
                # case pico2d.SDLK_ESCAPE:
                #     game_framework.change_state(title_state)
                case pico2d.SDL_BUTTON_LEFT:
                    player.attack = 'Attack'
                case pico2d.SDL_BUTTON_RIGHT:
                    player.attack = 'SkillAttack'


background_image_width = 384
background_image_height = 512
running = True
player = None
background = None
x, y = 0, 0


def enter():
    global running, player, background
    running = True
    player = Player()
    background = Background()


def exit():
    global player, background
    del player
    del background


def update():
    player.update()


def draw_world():
    player.draw()
    background.draw()


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