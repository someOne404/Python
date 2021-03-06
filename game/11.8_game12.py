import pygame
import gamebox
camera = gamebox.Camera(800,600) #width, height of the window

box = gamebox.from_color(camera.x, 100, 'green', 40, 40) # center at (200,100) coordinate (left to right, top to bottom), 40 pixels wide, 80 pixels tall
sun = gamebox.from_color(camera.x, camera.y, 'yellow', 40, 40)

box.speedx = 15
#box.speedy = -20


def tick(keys):
    camera.clear('black')
    G = 200000

    # gravity
    dx = sun.x - box.x
    dy = sun.y - box.y
    d_len = (dx*dx + dy*dy)**0.5
    box.speedx += G * dx / d_len**3
    box.speedy += G * dy / d_len**3

    box.move_speed()

    if box.left < camera.left:
        box.left = camera.left
        box.speedx = abs(box.speedx)
    if box.right > camera.right:
        box.right = camera.right
        box.speedx = -abs(box.speedx)
    if box.top < camera.top:
        box.top = camera.top
        box.speedy = abs(box.speedy)
    if box.bottom > camera.bottom:
        box.bottom = camera.bottom
        box.speedy = -abs(box.speedy)

    box.speedx *= .99
    box.speedy *= .99

    camera.draw(box)
    camera.draw(sun)

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)