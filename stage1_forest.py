from pico2d import *
import game_framework
import game_world

import enemy_dragon
import meteo
import play_state

# game_world.add_object(enemy_dragon.Lv1Dragon, 1)
play_state.enemies.append(enemy_dragon.Lv1Dragon())
