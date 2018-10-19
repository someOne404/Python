# Piano Tiles by jl4nq & ads2fp

'''We'll make a game that allows two players to compete with each other.
The one who finishes tapping all the black tiles at the bottom of the screen will win the game.
We will implement at least 4 requirements, which include:
    # Two players simultaneously
    # Scrolling level
    # Timer
    # Music/Sound effects


# Two players simultaneously:
    We will have two players playing at the time.
    Player 1 will use 'A','S','D','F' to tap the tiles.
    Player 2 will use 'H','J','K','L' to tap the tiles.

# Scrolling level:
    We will have 50 tiles for the players to complete.
    The tiles will come from the top of the screen.
    As the player finishes tapping the tile at the bottom, the tiles from the top will move down to create the scrolling effect.

# Timer:
    We will have a timer to record how long the competition takes.
    When one player finishes tapping 50 tiles, the game will end.
    The time taken by that player will be displayed on the screen

# Music/Sound effects:
    We will add a piece of piano music as the background music when the game starts
    It will play forever if the window is not closed.



'''
import random

import pygame

from pre_exam3 import gamebox

camera = gamebox.Camera(800, 600)
show_splash = True
ticks = 0
left_number = 0
right_number = 0
start = False
left_last_press = 0
right_last_press = 0


border = gamebox.from_color(camera.x, camera.y, 'black', 4, 600)
left_playground = gamebox.from_image(200, camera.y, 'background.jpg')
right_playground = gamebox.from_image(600, camera.y, 'background.jpg')

left_tiles = [
    gamebox.from_color(50 + 1 * 100, 50, "black", 100, 100),
    gamebox.from_color(50 + 3 * 100, 50 + 100, "black", 100, 100),
    gamebox.from_color(50 + 0 * 100, 50 + 200, "black", 100, 100),
    gamebox.from_color(50 + 2 * 100, 50 + 300, "black", 100, 100),
    gamebox.from_color(50 + 1 * 100, 50 + 400, "black", 100, 100),
    gamebox.from_color(50 + 0 * 100, 50 + 500, "black", 100, 100),
]
right_tiles = [
    gamebox.from_color(50 + 4 * 100, 50, "black", 100, 100),
    gamebox.from_color(50 + 7 * 100, 50 + 100, "black", 100, 100),
    gamebox.from_color(50 + 5 * 100, 50 + 200, "black", 100, 100),
    gamebox.from_color(50 + 4 * 100, 50 + 300, "black", 100, 100),
    gamebox.from_color(50 + 6 * 100, 50 + 400, "black", 100, 100),
    gamebox.from_color(50 + 4 * 100, 50 + 500, "black", 100, 100),

]


# Splash Screen
def splash(keys):
    global show_splash
    camera.clear('black')
    camera.draw(gamebox.from_text(camera.x, camera.y - 130,
                                  "Piano Tiles", "Arial", 70,
                                  "white"))
    camera.draw(gamebox.from_text(camera.x, camera.y - 60, "Burgard Lu (jl4nq) & Aidan Sinclair (ads2fp)", "Arial", 20, 'white'))
    keyboard = gamebox.from_image(camera.x, camera.y - 10, 'keyboard.gif')
    keyboard.width = 150
    camera.draw(keyboard)
    camera.draw(gamebox.from_text(camera.x, camera.y + 50,
                                  "PLAYER 1: Press 'A','S','D','F'", "Arial", 25,
                                  "white"))
    camera.draw(gamebox.from_text(camera.x, camera.y + 100,
                                  "PLAYER 2: Press 'H','J','K','L'", "Arial", 25,
                                  "white"))
    camera.draw(gamebox.from_text(camera.x, camera.y + 160,
                                  "Instruction: Tap the lowest black tiles and get 50 ones as soon as possible",
                                  "Arial", 20,
                                  "red"))
    camera.draw(gamebox.from_text(camera.x, camera.y + 200,
                                  "(Press Space To Continue)", "Arial", 20,
                                  "white"))


    if pygame.K_SPACE in keys:
        show_splash = False
    camera.display()


def tick(keys):
    global start
    global ticks
    global left_number
    global right_number
    global left_last_press
    global right_last_press
    if show_splash:
        splash(keys)
        return

    camera.clear('white')
    camera.draw(left_playground)
    camera.draw(right_playground)
    camera.draw(border)

    start_sign = gamebox.from_text(camera.x, camera.y, "Press Enter to Start", "Arial", 50, "yellow")
    left_timer = gamebox.from_text(0, 0, str(ticks // 30), "Arial", 30, "red")
    right_timer = gamebox.from_text(0, 0, str(ticks // 30), "Arial", 30, "red")
    left_timer.top = camera.top
    right_timer.top = camera.top
    left_timer.left = camera.left
    right_timer.right = camera.right

    camera.draw(left_timer)
    camera.draw(right_timer)

    if pygame.K_RETURN in keys:
        start = True
    if start:
        ticks += 1

    left_win = gamebox.from_text(200, 200, 'You win!', "Arial", 50, "yellow")
    right_win = gamebox.from_text(600, 200, 'You win!', "Arial", 50, "yellow")
    left_score = gamebox.from_text(200, 300, 'You record is ' + str(ticks // 30) + '"', "Arial", 50, "yellow")
    right_score = gamebox.from_text(600, 300, 'You record is ' + str(ticks // 30) + '"', "Arial", 50, "yellow")


    bgm = gamebox.load_sound(
            'bumble_bee.wav')
    if start:
        bgm.play(-1)


    for tile in left_tiles:
        camera.draw(tile)
        if start:
            if tile.y == 550:
                if tile.x == 50 and pygame.K_a in keys and left_last_press < ticks - 2:
                    left_last_press = ticks
                    for tile in left_tiles:
                        tile.y += 100
                    left_number += 1
                if tile.x == 150 and pygame.K_s in keys and left_last_press < ticks - 2:
                    left_last_press = ticks
                    for tile in left_tiles:
                        tile.y += 100
                    left_number += 1
                if tile.x == 250 and pygame.K_d in keys and left_last_press < ticks - 2:
                    left_last_press = ticks
                    for tile in left_tiles:
                        tile.y += 100
                    left_number += 1
                if tile.x == 350 and pygame.K_f in keys and left_last_press < ticks - 2:
                    left_last_press = ticks
                    for tile in left_tiles:
                        tile.y += 100
                    left_number += 1
            if tile.y > camera.bottom:
                tile.y -= 600
                tile.x = 50 + random.randint(0, 3) * 100


    for tile in right_tiles:
        camera.draw(tile)
        if start:
            if tile.y == 550:
                if tile.x == 450 and pygame.K_h in keys and right_last_press < ticks - 2:
                    right_last_press = ticks
                    for tile in right_tiles:
                        tile.y += 100
                    right_number += 1
                if tile.x == 550 and pygame.K_j in keys and right_last_press < ticks - 2:
                    right_last_press = ticks
                    for tile in right_tiles:
                        tile.y += 100
                    right_number += 1
                if tile.x == 650 and pygame.K_k in keys and right_last_press < ticks - 2:
                    right_last_press = ticks
                    for tile in right_tiles:
                        tile.y += 100
                    right_number += 1
                if tile.x == 750 and pygame.K_l in keys and right_last_press < ticks - 2:
                    right_last_press = ticks
                    for tile in right_tiles:
                        tile.y += 100
                    right_number += 1
            if tile.y > camera.bottom:
                tile.y -= 600
                tile.x = 50 + random.randint(4, 7) * 100
    if left_number == 50:
        camera.draw(left_win)
        camera.draw(left_score)
        gamebox.pause()

    if right_number == 50:
        camera.draw(right_win)
        camera.draw(right_score)
        gamebox.pause()

    if start == False:
        camera.draw(start_sign)

    camera.draw(gamebox.from_text(50, 550, "A", "Arial", 20, "red"))
    camera.draw(gamebox.from_text(150, 550, "S", "Arial", 20, "red"))
    camera.draw(gamebox.from_text(250, 550, "D", "Arial", 20, "red"))
    camera.draw(gamebox.from_text(350, 550, "F", "Arial", 20, "red"))
    camera.draw(gamebox.from_text(450, 550, "H", "Arial", 20, "red"))
    camera.draw(gamebox.from_text(550, 550, "J", "Arial", 20, "red"))
    camera.draw(gamebox.from_text(650, 550, "K", "Arial", 20, "red"))
    camera.draw(gamebox.from_text(750, 550, "L", "Arial", 20, "red"))

    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)