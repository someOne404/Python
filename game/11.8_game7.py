import pygame
import gamebox
camera = gamebox.Camera(800,600) # width, height of the window

box1 = gamebox.from_image(600, 200, "https://www.python.org/static/opengraph-icon-200x200.png")
box2 = gamebox.from_image(200, 200, "https://www.python.org/static/opengraph-icon-200x200.png")
walls = [
    gamebox.from_color(camera.x, camera.bottom, "black", 500, 50),
    gamebox.from_color(camera.x, camera.bottom, "black", 50, 500)
]

box1.timer = 0
box2.timer = 0
def tick(keys):
    camera.clear('cyan')


    if pygame.K_RIGHT in keys:
        box1.speedx = 10
    if pygame.K_LEFT in keys:
        box1.speedx = -10
    if pygame.K_UP in keys and box1.timer > 10:
        box1.speedy = -15
        box1.timer = 0
    if pygame.K_DOWN in keys:
        box1.speedy = 10

    if pygame.K_d in keys:
        box2.speedx = 10
    if pygame.K_a in keys:
        box2.speedx = -10
    if pygame.K_w in keys and box2.timer > 10:
        box2.speedy = -15
        box2.timer = 0
    if pygame.K_s in keys:
        box2.speedy = 10

    for box in [box1, box2]:
        box.timer += 1

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