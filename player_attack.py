from pico2d import *
import play_state

# 이벤트 정의 RD = RIGHT_DOWN, RU = RIGHT_UP, LD = LEFT_DOWN, LU = LEFT_UP
RD, LD, RU, LU = range(4)  # RD, LD, RU, LU = 0, 1, 2, 3

key_event_table = {
    (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_RIGHT): RD,
    (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT): LD,
    (SDL_MOUSEBUTTONUP, SDL_BUTTON_RIGHT): RU,
    (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT): LU,
}




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
        self.attack_x = play_state.x
        self.attack_y = play_state.y + 50

    def update(self):
        self.attack_y += 2

    def draw(self):
        self.image.draw(self.attack_x, self.attack_y)


class SkillAttack:
    def __init__(self):
        self.image = load_image('skill_attack_image.png')
        self.attack_x = play_state.x
        self.attack_y = play_state.y + 50

    def update(self):
        self.attack_y += 2

    def draw(self):
        self.image.draw(self.attack_x, self.attack_y)


class Player:  # 플레이어 캐릭터 클래스
    def add_event(self, key_event):
        self.q.insert(0, key_event)

    def handle_event(self, event):  # event: 키 입력 이벤트
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        if self.q:  # 만약에 리스트 q에 뭔가 들어있다면...
            event = self.q.pop()
            self.cur_state.exit()
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter()

    def __init__(self):
        self.image = load_image('player_image.png')

    def update(self):
        global x, y
        # 맵 밖으로 못가게 함
        if x > play_state.background_image_width*2:
            x = play_state.background_image_width*2
        elif x < 0:
            x = 0
        if y > play_state.background_image_height*2:
            y = play_state.background_image_height*2
        elif y < 0:
            y = 0

    def draw(self):
        self.image.draw(x, y)
