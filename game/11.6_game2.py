import pygame
import gamebox
camera = gamebox.Camera(800,600) # width, height of the window

box = gamebox.from_image(600, 200, "https://img00.deviantart.net/edda/i/2015/290/1/4/umaru_chan_by_aruvian13-d9dddj6.png")
wall = gamebox.from_color(camera.x, camera.bottom, "black", 500, 50)

def tick(keys):
    camera.clear('cyan')


    if pygame.K_RIGHT in keys:
        box.x += 10
    if pygame.K_LEFT in keys:
        box.x -= 10
    if pygame.K_UP in keys:
        box.y -= 10
    if pygame.K_DOWN in keys:
        box.y += 10

    box.move_to_stop_overlapping(wall, -30, -30)

    camera.draw(box)
    camera.draw(wall)

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)