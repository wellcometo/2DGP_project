from pico2d import *
import game_framework
import enemy_dragon
import player_attack
import time


class Background:  # 백그라운드 이미지 클래스
    def __init__(self):
        self.image = load_image('background_forest.png')

    def draw(self):
        # 캔버스에 백그라운드 이미지 가로 세로 2배씩 늘려서 그리기
        self.image.clip_draw(0, 0,
                             background_image_width, background_image_height,
                             background_image_width, background_image_height,
                             background_image_width*2, background_image_height*2)


class Player:  # 플레이어 캐릭터 클래스
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


class Timer:  # 적 생성 시간과 플레이어의 점수에 쓰이는 타이머
    def __init__(self):
        self.start_time = time.time()
        self.current_time = None

    def update(self):
        self.current_time = time.time() - self.start_time

    # def draw(self):
    #     print(self.current_time)


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

        if event.type == pico2d.SDL_MOUSEMOTION:  # 마우스 이동으로 플레이어 캐릭터 이동
            x, y = event.x, background_image_height*2 - 1 - event.y

        if event.type == SDL_MOUSEBUTTONDOWN:  # 마우스 좌클릭으로 공격, 우클릭으로 스킬 공격
            if event.button == pico2d.SDL_BUTTON_LEFT:
                attacks.append(player_attack.Attack())
            elif event.button == pico2d.SDL_BUTTON_RIGHT:
                attacks.append(player_attack.SkillAttack())

        # if 0.5 < now_time.current_time < 0.502:  # 일정 시간에 적 생성
        #     enemies.append(enemy_dragon.Lv2Dragon())


background_image_width = 384  # 캔버스 가로 크기는 이것의 2배
background_image_height = 512  # 캔버스 세로 크기는 이것의 2배
running = True
player = None
background = None
x, y = 0, 0
attacks = []
enemies = []
now_time = None


def enter():
    global running, player, background, x, y, attacks, enemies, now_time
    running = True
    player = Player()
    background = Background()
    x, y = 0, 0
    attacks = [player_attack.NoneAttack()]
    enemies = [enemy_dragon.Lv1Dragon(),
               enemy_dragon.Lv2Dragon(),
               enemy_dragon.Lv3Dragon(),
               enemy_dragon.Lv4Dragon(),
               enemy_dragon.Lv5Dragon()]
    now_time = Timer()


def exit():
    global player, background, x, y, attacks, enemies, now_time
    del player
    del background
    del x, y
    del attacks
    del enemies
    del now_time


def update():
    player.update()
    for attack in attacks:
        attack.update()
    for enemy in enemies:
        enemy.update()
    now_time.update()


def draw_world():
    background.draw()
    for enemy in enemies:
        enemy.draw()
    player.draw()
    for attack in attacks:
        attack.draw()

    # now_time.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass


def resume():
    pass
