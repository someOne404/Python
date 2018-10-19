import pygame
import gamebox
import random
camera = gamebox.Camera(800,600) # width, height of the window

box = gamebox.from_image(600, 200, "https://www.python.org/static/opengraph-icon-200x200.png")
walls = [
    gamebox.from_color(camera.x, camera.bottom, "black", 500, 50),
    gamebox.from_color(400, 200, "black", 50, 500),
    gamebox.from_color(80, 120, "black", 50, 50)
]
goal = gamebox.from_text(100, 400, 'goal', 'Arial', 20, 'blue')
coins = []
for i in range(50):
    coins.append(gamebox.from_color(
        random.randrange(camera.left, camera.right),
        random.randrange(camera.top, camera.bottom),
        "yellow", 20, 20
    ))

for coin in coins:
    for wall in walls:
        if coin.touches(wall):
            coins.remove(coin)

box.score = 0


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
        won = gamebox.from_text(camera.x, camera.y, "You got "+ str(box.score)+"!", "Arial", 100, 'white', bold=True)
        camera.draw(won)
        for wall in walls:
            wall.color = 'purple'
            camera.draw(wall)
        gamebox.pause()

    for coin in coins:
        camera.draw(coin)
    for coin in coins:
        if box.touches(coin, -60, -60):
            coins.remove(coin)
            box.score += 1

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)