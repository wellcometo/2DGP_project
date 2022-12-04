from pico2d import *
import game_framework
import play_state


image = None


def enter():
    global image
    image = load_image('title.png')


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:  # esc 누르면 종료
                game_framework.quit()
            elif event.key == SDLK_SPACE:  # 스페이스바 누르면 게임 시작
                game_framework.change_state(play_state)
        elif event.type == SDL_MOUSEBUTTONDOWN:  # 마우스 좌클릭 시 게임 시작
            if event.button == pico2d.SDL_BUTTON_LEFT:
                game_framework.change_state(play_state)


def draw():
    clear_canvas()
    image.draw(play_state.background_image_width, play_state.background_image_height)  # 캔버스 중앙에 그리기
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
