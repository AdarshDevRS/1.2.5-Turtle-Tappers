# This module will be used in main.py

#--- Variables ---#
x = -200
y = -100

t1Price = 20
t2Price = 200
t3Price = 1000

def initTurtle(turtle1, turtle2, turtle3): # Initiates the turtle cosmetics
    global x 
    global y

    turtles = [turtle1, turtle2, turtle3]
    for t in turtles:
        t.penup()
        t.goto(x, y)
        t.pendown()
        x+= 50