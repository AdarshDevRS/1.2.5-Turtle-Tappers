# This module will be used in main.py
import turtle as trtl

#--- Creating objects ---#
shopSection = trtl.Turtle()

t1PriceTurtle = trtl.Turtle() # Shows the price for the turtles.
t2PriceTurtle = trtl.Turtle()
t3PriceTurtle = trtl.Turtle()

#priceTurtles = [t1PriceTurtle, t2PriceTurtle, t3PriceTurtle]

#--- Config ---#

x = -300
y = -250

t1Price = 20
t2Price = 200
t3Price = 1000

#--- Functions ---#
def initShopTurtles(turtle1, turtle2, turtle3): # Initiates the turtle cosmetics
    global x 
    global y

    turtles = [turtle1, turtle2, turtle3]
    for t in turtles:
        t.penup()
        t.goto(x, y)
        t.pendown()
        x+= 100
    showShopSection()
    showPriceTurtle()

def showShopSection():
    shopSection.penup()
    shopSection.goto(x-200, y+40)
    shopSection.pendown()
    shopSection.write("Buy cosmetics!", font=("Ariel", 20, "bold"), align="center")
    shopSection.hideturtle()

def showPriceTurtle():
    priceX = -300 # Same things as global x variable to position the price label correctly.
    priceY = (-250) - 50

    t1PriceTurtle.penup()
    t2PriceTurtle.penup()
    t3PriceTurtle.penup()

    t1PriceTurtle.goto(priceX, priceY)
    t2PriceTurtle.goto(priceX + 100, priceY)
    t3PriceTurtle.goto(priceX + 200, priceY)

    t1PriceTurtle.pendown()
    t2PriceTurtle.pendown()
    t3PriceTurtle.pendown()

    t1PriceTurtle.write(str(t1Price) + " cash", font=("Ariel", 10, "bold"), align="center")
    t2PriceTurtle.write(str(t2Price) + " cash", font=("Ariel", 10, "bold"), align="center")
    t3PriceTurtle.write(str(t3Price) + " cash", font=("Ariel", 10, "bold"), align="center")

    t1PriceTurtle.hideturtle()
    t2PriceTurtle.hideturtle()
    t3PriceTurtle.hideturtle()