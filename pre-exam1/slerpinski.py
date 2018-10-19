import turtle

w = turtle.Turtle()
w.speed('fastest')


def tri(size):
    if size < 10:
        for i in range(3):
            w.forward(size)
            w.left(360/3)

    else:
        for i in range(3):
            tri(size/2)
            w.forward(size)
            w.left(360/3)



tri(300)

turtle.mainloop()