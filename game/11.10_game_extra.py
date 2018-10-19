# Splash Screen
# Timers
# Infinite Scroller
# Shoot
# Enemies
# Lives/Health
# Animate

import pygame
import gamebox
import random
camera = gamebox.Camera(400, 400)
show_splash = True
ticks = 0

platforms = [
    gamebox.from_color(0, 0, 'black', 200, 20),
    gamebox.from_color(300, 150, 'black', 200, 20),
    gamebox.from_color(100, 300, 'black', 200, 20),
    gamebox.from_color(200, 450, 'black', 200, 20),
]

#me = gamebox.from_text(200, 200, 'me', "Arial", 30, 'dark green')

shot = gamebox.from_text(200, 2200, "Bang!", "Arial", 20, "red")
shot.last_shot = 0
baddie = gamebox.from_color(0,0, "purple", 20, 20)

cats = gamebox.load_sprite_sheet("http://kwiksher.com/wp-content/uploads/2012/09/runningcat.png", 4, 2)
print(cats)
me = gamebox.from_image(200, 200, cats[0])
me.width = 100
me.lives = 3

# Splash Screen
def splash(keys):
    global show_splash
    camera.clear('black')
    camera.draw(gamebox.from_text(camera.x, camera.y,
                                  "Welcome!", "Arial", 30,
                                  "yellow"))
    camera.draw(gamebox.from_text(camera.x, camera.y+50,
                                  "(press space to continue)", "Arial", 15,
                                  "white"))
    if ticks > 60:
        show_splash = False
    if pygame.K_SPACE in keys:
        show_splash = False
    camera.display()


def tick(keys):
    global ticks
    ticks += 1

    if show_splash:
        splash(keys)
        return

    camera.clear('yellow')

# Timer
    time = gamebox.from_text(0,0, str(ticks//30), "Arial", 20, "red")
    time.top = camera.top
    time.right = camera.right
    camera.draw(time)

# infinite scroller
    for platform in platforms:
        camera.draw(platform)
        platform.y += 10
        if platform.top > camera.bottom:
            platform.y -= 600
            platform.x = random.randrange(camera.left, camera.right)
            platform.size = [random.randrange(20, 200), 20] #[width, height]

    if pygame.K_LEFT in keys:
        me.x -= 10
    if pygame.K_RIGHT in keys:
        me.x += 10
    if pygame.K_UP in keys:
        me.y -= 10
    if pygame.K_DOWN in keys:
        me.y += 10
    # me.image = random.choice(cats)
    me.image = cats[(ticks//3) % len(cats)]
    camera.draw(me)

# Shot
    if pygame.K_SPACE in keys and shot.last_shot < ticks - 30:
        shot.center = me.center
        shot.speedx = 15
        shot.speedy = -5
        shot.last_shot = ticks
    shot.move_speed()

    camera.draw(shot)

#Enemy
    # acceleration
    if baddie.x < me.x:
        baddie.speedx += 1
    if baddie.x > me.x:
        baddie.speedx -= 1
    if baddie.y < me.y:
        baddie.speedy += 1
    if baddie.y > me.y:
        baddie.speedy -= 1
    # drag
    baddie.speedx *= 0.95
    baddie.speedy *= 0.95
    # momentum
    baddie.move_speed()
    # display
    camera.draw(baddie)

    if baddie.touches(me):
        me.lives -= 1
        baddie.x = 0
        baddie.y = 0
        if me.lives < 0:
            gamebox.pause()


    camera.display()


gamebox.timer_loop(30, tick)