import pico2d
import game_framework
import play_state

pico2d.open_canvas(play_state.background_image_width*2, play_state.background_image_height*2)
game_framework.run(play_state)
pico2d.close_canvas()