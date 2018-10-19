import pygame
import gamebox

camera = gamebox.Camera(800,600) # width, height of the window

box = gamebox.from_color(200, 100, 'red', 40, 80) # center at (200,100) coordinate (left to right, top to bottom), 40 pixels wide, 80 pixels tall
box2 = gamebox.from_text(400, 300, 'Box!', 'Arial', 100, 'yellow')
#box3 = gamebox.from_image(600, 200, "https://www.python.org/static/opengraph-icon-200x200.png")

def tick(keys):
    camera.clear('cyan')

    camera.draw(box2)
    camera.draw(box)
    #camera.draw(box3)

    if pygame.K_RIGHT in keys:
        box.x += 10
    if pygame.K_LEFT in keys:
        box.x -= 10
    if pygame.K_UP in keys:
        box.y -= 10
    if pygame.K_DOWN in keys:
        box.y += 10

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)