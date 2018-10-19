import pygame
import gamebox
camera = gamebox.Camera(800,600) # width, height of the window

box = gamebox.from_image(600, 200, "https://www.python.org/static/opengraph-icon-200x200.png")
walls = [
    gamebox.from_color(camera.x, camera.bottom, "black", 500, 50),
    gamebox.from_color(400, 200, "black", 50, 500),
    gamebox.from_color(80, 120, "black", 50, 50)
]
goal = gamebox.from_text(100, 400, 'goal', 'Arial', 20, 'blue')
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

    for wall in walls:
        box.move_to_stop_overlapping(wall, -30, -30)


    camera.draw(box)
    for wall in walls:
        camera.draw(wall)
    camera.draw(goal)

    if box.touches(goal):
        won = gamebox.from_text(camera.x, camera.y, "You won!", "Arial", 150, 'white', bold=True)
        camera.draw(won)
        for wall in walls:
            wall.color = 'purple'
            camera.draw(wall)
        gamebox.pause()

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)