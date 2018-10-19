import pygame
import gamebox
camera = gamebox.Camera(800, 600)

box = gamebox.from_image(600, 200, "https://www.python.org/static/opengraph-icon-200x200.png")
wall = gamebox.from_color(camera.x, camera.bottom, "black", 500, 50)


def tick(keys):
    camera.clear('cyan')

    if pygame.K_RIGHT in keys:
        box.speedx = +10
    if pygame.K_LEFT in keys:
        box.speedx = -10
    if pygame.K_UP in keys:
        box.speedy = -10
    if pygame.K_DOWN in keys:
        box.speedy = +10

    box.speedx *= .9
    box.speedy *= .9

    box.speedy += 1

    box.move_speed()
    box.move_to_stop_overlapping(wall, -30, -30)
    #box.move_both_to_stop_overlapping(wall)
    print(box.overlap(wall))
    print(box.pad(wall))

    camera.draw(box)
    camera.draw(wall)

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)