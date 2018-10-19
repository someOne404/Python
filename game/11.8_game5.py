import pygame
import gamebox
camera = gamebox.Camera(800,600) # width, height of the window

box = gamebox.from_image(600, 200, "https://www.python.org/static/opengraph-icon-200x200.png")
walls = [
    gamebox.from_color(camera.x, camera.bottom, "black", 500, 50),
    gamebox.from_color(camera.x, camera.bottom, "black", 50, 500)
]
def tick(keys):
    camera.clear('cyan')

    on_ground = False
    for wall in walls:
        if box.bottom_touches(wall, -30, -30):
            box.speedx = 0
            on_ground = True


    if pygame.K_RIGHT in keys:
        box.speedx = 10
    if pygame.K_LEFT in keys:
        box.speedx = -10
    if pygame.K_UP in keys and on_ground:
        box.speedy = -10
    if pygame.K_DOWN in keys:
        box.speedy = 10

    box.speedx *= .95
    box.speedy *= .95

    box.speedy += 1 # mimics gravity



    box.move_speed()

    for wall in walls:
        box.move_to_stop_overlapping(wall, -30, -30)
        camera.draw(wall)

    camera.draw(box)
    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)