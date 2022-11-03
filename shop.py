# This module will be used in main.py
import turtle as trtl

#--- Creating objects ---#
shopSection = trtl.Turtle()

t1PriceTurtle = trtl.Turtle() # Shows the price for the turtles.
t2PriceTurtle = trtl.Turtle()
t3PriceTurtle = trtl.Turtle()

#--- Config ---#
x = -300
y = -250

t1Price = 20
t2Price = 200
t3Price = 1000

#--- Functions ---#
def initTurtle(turtle1, turtle2, turtle3): # Initiates the turtle cosmetics
    global x 
    global y

    turtles = [turtle1, turtle2, turtle3]
    for t in turtles:
        t.penup()
        t.goto(x, y)
        t.pendown()
        x+= 50
    shopSection.penup()
    shopSection.goto(x-100, y+40)
    shopSection.pendown()
    shopSection.write("Buy cosmetics!", font=("Ariel", 20, "bold"), align="center")
    shopSection.hideturtle()