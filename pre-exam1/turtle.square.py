import turtle

def polygon(sides,size,to_left):
    for i in range(sides):
        shelly.forward(size)
        if to_left == True:
            shelly.left(360/sides)
        else:
            shelly.right(360/sides)


shelly = turtle.Turtle()
shelly.shape('turtle')
shelly.speed('fastest')
shelly.shapesize(1)
shelly.color('magenta')

polygon(3, 100, True)
polygon(5, 80, False)
polygon(7, 50, False)
polygon(360, 2, True)


# square: repeat 4 times (comment)
for i in range(4):
    shelly.forward(100)
    shelly.left(90)




# pentagon:
for i in range(5):
    shelly.forward(100)
    shelly.left(360/5)



# shelly.forward(100)
# shelly.left(90)
# shelly.forward(100)
# shelly.left(90)
# shelly.forward(100)
# shelly.left(90)
# shelly.forward(100)
# shelly.left(90)


turtle.mainloop() # means "keep the window open"

.left(100)
