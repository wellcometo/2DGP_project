from pico2d import *
import game_framework
import play_state


class ForestBackground:  # 백그라운드 이미지 클래스
    def __init__(self):
        self.image = load_image('background_forest.png')

    def update(self):
        pass

    def draw(self):
        # 캔버스에 백그라운드 이미지 가로 세로 2배씩 늘려서 그리기
        self.image.clip_draw(0, 0,
                             play_state.background_image_width, play_state.background_image_height,
                             play_state.background_image_width, play_state.background_image_height,  # 이미지 그릴 x, y 좌표
                             play_state.background_image_width * 2, play_state.background_image_height * 2)  # 이미지 늘리기
