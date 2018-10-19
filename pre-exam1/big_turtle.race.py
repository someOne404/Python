import turtle
import random  # give random integers between 2 numbers

# make a list of turtles
turtles = [
    turtle.Turtle(),
    turtle.Turtle(),
    turtle.Turtle(),
    turtle.Turtle(),
    turtle.Turtle(),
]


# reshape all of the turtles
for a in turtles:
    a.shape('turtle')  # "a" means each of the turtles one at a time, it is arbitrarily defined
    a.penup()
    a.speed('fast')

for i in range(len(turtles)):  # len(turtles) means length of the list
    a = turtles[i]
    a.left(90)
    a.forward(30*i)
    a.right(90)

for i in range(100):
    for hello in turtles:
        hello.forward(random.randint(0,6))








# keep the window open
turtle.mainloop()