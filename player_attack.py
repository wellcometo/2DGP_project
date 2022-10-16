from pico2d import *
import play_state


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


# def handle_events():
#     events = get_events()
#     for event in events:
#         if event.type == SDL_MOUSEBUTTONDOWN:
#             if event.button == pico2d.SDL_BUTTON_LEFT:
#                 # attacks = Attack()
#                 play_state.attacks.append(Attack())
#             elif event.button == pico2d.SDL_BUTTON_RIGHT:
#                 # attacks = SkillAttack()
#                 play_state.attacks.append(SkillAttack())
