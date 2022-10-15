import pico2d

pico2d.open_canvas()
events = pico2d.get_events()
for event in events:
    if event.type == pico2d.SDL_QUIT:
        pico2d.close_canvas()