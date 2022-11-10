from pico2d import *
import game_framework
import title_state

from player_attack import Player, NoneAttack
import enemy_dragon
import meteo

import time

import background


player = None
attacks = []  # 플레이어의 공격들
enemies = []
meteors = []
background = None
background_image_width = 384  # 캔버스 가로 크기는 이것의 2배
background_image_height = 512  # 캔버스 세로 크기는 이것의 2배


# class Background:  # 백그라운드 이미지 클래스
#     def __init__(self):
#         self.image = load_image('background_forest.png')
#
#     def draw(self):
#         # 캔버스에 백그라운드 이미지 가로 세로 2배씩 늘려서 그리기
#         self.image.clip_draw(0, 0,
#                              background_image_width, background_image_height,
#                              background_image_width, background_image_height,
#                              background_image_width*2, background_image_height*2)


# class Player:  # 플레이어 캐릭터 클래스
#     def __init__(self):
#         self.image = load_image('player_image.png')
#
#     def update(self):
#         global x, y
#         # 맵 밖으로 못가게 함
#         if x > background_image_width*2:
#             x = background_image_width*2
#         elif x < 0:
#             x = 0
#         if y > background_image_height*2:
#             y = background_image_height*2
#         elif y < 0:
#             y = 0
#
#     def draw(self):
#         self.image.draw(x, y)


class Timer:  # 적 생성 시간과 플레이어의 점수에 쓰이는 타이머
    def __init__(self):
        self.start_time = time.time()
        self.current_time = None

    def update(self):
        self.current_time = time.time() - self.start_time

    # def draw(self):  # 시간 확인할 때 씀
    #     print(self.current_time)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
        else:
            player.handle_event(event)

        # if event.type == pico2d.SDL_MOUSEMOTION:  # 마우스 이동으로 플레이어 캐릭터 이동
        #     x, y = event.x, background_image_height*2 - 1 - event.y
        #
        # if event.type == SDL_MOUSEBUTTONDOWN:  # 마우스 좌클릭으로 공격, 우클릭으로 스킬 공격
        #     if event.button == pico2d.SDL_BUTTON_LEFT:
        #         attacks.append(player_attack.Attack())
        #     elif event.button == pico2d.SDL_BUTTON_RIGHT:
        #         attacks.append(player_attack.SkillAttack())

        # if 0.5 < now_time.current_time < 0.502:  # 일정 시간에 적 생성, 정상 작동X 수정 바람
        #     enemies.append(enemy_dragon.Lv2Dragon())




now_time = None


def enter():
    global player, background, attacks, enemies, now_time, meteors
    player = Player()
    background = background.Background()
    attacks = [NoneAttack()]
    enemies = [enemy_dragon.Lv1Dragon(),  # 시험하기 위해서 모든 용을 리스트에 넣음
               enemy_dragon.Lv2Dragon(),  # 나중에 enemy_dragon.NoneDragon()으로 수정하기 바람
               enemy_dragon.Lv3Dragon(),
               enemy_dragon.Lv4Dragon(),
               enemy_dragon.Lv5Dragon()]
    now_time = Timer()
    meteors = [meteo.Meteo()]  # 시험하기 위해서 메테오 넣음, 나중에 meteo.NoneMeteo()로 수정하기 바람


def exit():
    global player, background, x, y, attacks, enemies, now_time, meteors
    del player
    del background
    del x, y
    del attacks
    del enemies
    del now_time
    del meteors


def update():
    player.update()
    for attack in attacks:
        attack.update()
    for enemy in enemies:
        enemy.update()
    for meteor in meteors:
        meteor.update()
    now_time.update()


def draw_world():
    background.draw()
    for enemy in enemies:
        enemy.draw()
    player.draw()
    for attack in attacks:
        attack.draw()
    for meteor in meteors:
        meteor.draw()
    # now_time.draw()  # 시간 확인할 때 씀


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass


def resume():
    pass
