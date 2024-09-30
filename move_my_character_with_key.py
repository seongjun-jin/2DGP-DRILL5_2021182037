from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')

def handle_events():
    global running
    global x
    global y
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                if x < 800:
                    x += 10
                    dir += 1
                if x >= 800:
                    x += 0
                    dir += 1
            elif event.key == SDLK_LEFT:
                if x > 0:
                    x -= 10
                    dir -= 1
                if x <= 0:
                    x -= 0
                    dir -= 1
            elif event.key == SDLK_UP:
                if y < 600:
                    y += 10
                    dir += 2
                if y >= 600:
                    y += 0
                    dir += 2
            elif event.key == SDLK_DOWN:
                if y > 0:
                    y -= 10
                    dir -= 2
                if y <= 0:
                    y += 0
                    dir -= 2
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_UP:
                dir -= 2
            elif event.key == SDLK_DOWN:
                dir += 2

running = True
x = 800 // 2
y = 600 // 2
frame = 0
dir = 0

while running:
    clear_canvas()
    background.draw(400,100)
    if dir == 1:
        character.clip_draw(frame * 60, 60, 60, 60, x, y)
    elif dir == -1:
        character.clip_draw(frame * 60, 120, 60, 60, x, y)
    elif dir == -2:
        character.clip_draw(frame * 60, 180, 60, 60, x, y)
    elif dir == 2:
        character.clip_draw(frame * 60, 0, 60, 60, x, y)
    elif dir == 0:
        character.clip_draw(frame * 60, 180, 60, 60, x, y)

    update_canvas()
    handle_events()
    frame = (frame+1) % 8

    if dir == 1:
        if x < 800:
            x += dir * 5
        else:
            x += 0

    elif dir == -1:
        if x > 0:
            x += dir * 5
        else:
            x -= 0

    elif dir == 2:
        if y < 600:
            y += dir * 5
        else:
            y += 0

    elif dir == -2:
        if y > 0:
            y += dir * 5
        else:
            y -= 0

close_canvas()