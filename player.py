import time

from pico2d import *
import game_world
import play_state

import player_attack


# 이벤트 정의
LD, LU = range(2)
event_name = ['LD', 'LU']

button_event_table = {
    (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT): LD,
    (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT): LU
}


# 상태 정의
class IDLE:
    @staticmethod
    def enter(self):
        print('ENTER IDLE')
        pass

    @staticmethod
    def exit(self):
        print('EXIT IDLE')
        pass

    @staticmethod
    def do(self):
        pass

    @staticmethod
    def draw(self):
        pass


class ATTACK:
    def enter(self):
        print('ENTER ATTACK')
        pass

    def exit(self):
        print('EXIT ATTACK')
        pass

    def do(self):
        game_world.add_object(player_attack.Attack(self.x, self.y), 1)
        pass

    def draw(self):
        pass


# 상태 변환 테이블
next_state = {
    IDLE:  {LU: IDLE, LD: ATTACK},
    ATTACK:   {LU: IDLE, LD: ATTACK},
}


class Player:

    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('images/player_image.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self)


    def draw(self):
        self.cur_state.draw(self)
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.button) in button_event_table:
            button_event = button_event_table[(event.type, event.button)]
            self.add_event(button_event)
        # 마우스 이동으로 플레이어 캐릭터 이동
        elif event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, play_state.background_image_height * 2 - 1 - event.y

    def fire_ball(self):
        print('FIRE BALL')
        # game_world.add_object(ball, 1)

    def get_bb(self):  # bb = Bounding Box(충돌 범위)
        return self.x-50, self.y-50, self.x+50, self.y+50

    def handle_collision(self, other, group):
        pass
