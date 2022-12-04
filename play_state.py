from pico2d import *
import game_framework
import game_world

from player import Player
import enemy_dragon
import meteo
from background import ForestBackground

player = None
attacks = []
enemies = []
meteors = []
background = None
background_image_width = 384  # 캔버스 가로 크기는 이것의 2배
background_image_height = 512  # 캔버스 세로 크기는 이것의 2배


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player.handle_event(event)


# 초기화
def enter():
    global background
    background = ForestBackground()
    game_world.add_object(background, 0)

    global player
    player = Player()
    game_world.add_object(player, 1)

    global attacks
    attacks = []
    game_world.add_objects(attacks, 1)

    global enemies
    enemies = []
    game_world.add_objects(enemies, 1)

    # 충돌 대상 정보를 등록
    game_world.add_collision_pairs(player, enemies, 'player:enemies')
    game_world.add_collision_pairs(attacks, enemies, 'attacks:enemies')


# 종료
def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    # 충돌 체크
    # 볼들과 소년의 충돌
    # for ball in balls.copy():
    #     if collide(boy, ball):
    #         print('COLLISION boy: ball')
    #         game_world.remove_object(ball)  # object 에서는 삭제했지만 balls 에 남아있음
    #         balls.remove(ball)  # balls 리스트에서 ball 삭제


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass


def resume():
    pass


def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    # if 조건문이 모두 거짓(충돌)이어야 return True(충돌)
    return True
