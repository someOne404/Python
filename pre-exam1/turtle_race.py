import turtle
import random  # give random integers bewteen 2 numbers

# make a couple of turtles and color them
a = turtle.Turtle()
b = turtle.Turtle()
a.shape('turtle')
b.shape('turtle')
a.color('purple')
b.color('darkgreen')
a.penup()
b.penup()

# move them off of each other
b.right(90)
b.forward(30)
b.left(90)

# race 1
# for i in range(100):
    # a.forward(random.randint(0,6))
    # b.forward(random.randint(0,6))

# race 2
while a.xcor() < 300 and b.xcor() < 300: #it keeps going as long as one of them has not finished
    a.forward(random.randint(0, 6))
    b.forward(random.randint(0, 6))

# report who won
if a.xcor() > b.xcor():
    print(a.pencolor(), 'won!')
else:
    print(b.pencolor(), 'won!')




# keep the window open
turtle.mainloop()