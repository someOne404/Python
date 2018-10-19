import pygame
import gamebox
camera = gamebox.Camera(800,600) #width, height of the window

box = gamebox.from_color(200, 100, 'red', 40, 80) # center at (200,100) coordinate (left to right, top to bottom), 40 pixels wide, 80 pixels tall

def tick(keys):
    camera.clear('cyan')

    if pygame.K_RIGHT in keys:
        box.x += 10
    camera.draw(box)

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick) # run the 'tick' function 30 times every second

# y increases going down and to the right, y decreases going up and to the left