import turtle


shelly = turtle.Turtle()
shelly.shape('turtle')

for i in range(20,40,3): # in 20-40 range, one step equals to 3
    shelly.forward(10) #in forward, 10 means 10 pixels; in turn, 10 means degrees
    shelly.right(i**2)
    print(i)

turtle.mainloop()