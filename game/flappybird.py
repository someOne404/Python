import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
ticks = 0
me = gamebox.from_image(100,camera.y,'https://vignette.wikia.nocookie.net/fantendo/images/8/85/Flappy_Bird.png/revision/latest?cb=20140208141118')
me.width = 100


top_pillars = [
    gamebox.from_color(260, 0, 'dark green', 50, 200),
    gamebox.from_color(520, 0, 'dark green', 50, 250),
    gamebox.from_color(780, 0, 'dark green', 50, 200),
]

bottom_pillars =[
    gamebox.from_color(260, 0, 'dark green', 50, 180),
    gamebox.from_color(520, 0, 'dark green', 50, 170),
    gamebox.from_color(780, 0, 'dark green', 50, 130),
]

def tick(keys):
    global ticks
    camera.clear('light blue')
    ticks += 1

    for pillar in top_pillars:
        camera.draw(pillar)
        pillar.top = camera.top
        pillar.x -= 10
        top_height = float(pillar.height)
        if pillar.left < camera.left:
            pillar.x += 800
            pillar.size = [50, random.randrange(100, 250)]

    for pillar in bottom_pillars:
        camera.draw(pillar)
        pillar.bottom = camera.bottom
        pillar.x -= 10
        if pillar.left < camera.left:
            pillar.x += 800
            pillar.size = [50, random.randrange(100, 250)]


    score = gamebox.from_text(0,0, str(ticks//30), "Arial", 50, "black")
    score.top = camera.top
    score.right = camera.right
    camera.draw(score)

    for pillar in top_pillars:
        if me.touches(pillar, -30, -5):
            final_score = gamebox.from_text(camera.x, camera.y, "You score is " + str(ticks//30), "Arial", 100, "black")
            camera.draw(final_score)
            gamebox.pause()
    for pillar in bottom_pillars:
        if me.touches(pillar, -25, -15):
            final_score = gamebox.from_text(camera.x, camera.y, "You score is " + str(ticks//30), "Arial", 100, "black")
            camera.draw(final_score)
            gamebox.pause()

    if me.y > camera.bottom:
        final_score = gamebox.from_text(camera.x, camera.y, "You score is " + str(ticks // 30), "Arial", 100, "black")
        camera.draw(final_score)
        gamebox.pause()
    if me.y < camera.top:
        final_score = gamebox.from_text(camera.x, camera.y, "You score is " + str(ticks // 30), "Arial", 100, "black")
        camera.draw(final_score)
        gamebox.pause()

    if pygame.K_SPACE in keys:
        me.speedy = -10
    me.speedy *= .95
    me.speedy += 1

    me.move_speed()
    camera.draw(me)

    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)