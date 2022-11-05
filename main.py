#--- Imports ---#
import turtle as trtl
import random as rand
import timer 

import shop # The python file I have created which handles the shop/cosmetics.

#--- Creating objects ---# 
clickTurtle = trtl.Turtle() # This turtle will be the turtle the player needs to click to get cash.
cashTurtle = trtl.Turtle() # This turtle shows how much cash total cash the player has.
upgradeMultiplierTurtle = trtl.Turtle()
showMultiplierStats = trtl.Turtle()

turtle1 = trtl.Turtle() # These will be the turtle cosmetics.
turtle2 = trtl.Turtle()
turtle3 = trtl.Turtle()

#--- Config ---#
clickTurtle.shape("circle")
clickTurtle.shapesize(5)
clickTurtle.penup()

cashTurtle.penup()
cashTurtle.hideturtle()
cashTurtle.goto(-80, 300)
cashTurtle.pendown()

upgradeMultiplierTurtle.penup()
upgradeMultiplierTurtle.goto(150, -200)
upgradeMultiplierTurtle.shapesize(1)
upgradeMultiplierTurtle.pendown()
upgradeMultiplierTurtle.write("Click here to upgrade multiplier to earn cash faster!", font=("Ariel", 10, "bold"))

showMultiplierStats.penup()
showMultiplierStats.hideturtle()
showMultiplierStats.goto(-60, 270)
showMultiplierStats.pendown()

turtle1.shape("circle") # Cosmetics
turtle2.shape("square")
turtle3.shape("triangle")

#--
turtleColors = ["Purple", "Blue", "Red", "Green", "Yellow", "Black", "Brown", "Cyan"] # The colors the clickTurtle will appear in. (randomly)

#--- Variables ---#
cash = 0
multiplier = 1 # player can upgrade variable so player can earn more cash per click.

multiplierUpgradePrice = 10 # The price that the multiplier upgrade will cost. This will increment to a higher price when player buys upgrade.

#--- Functions ---#
def click(x, y):
    randomSpawn()
    gainCash()

def randomSpawn(): 
    randColor = rand.randint(0, 7) # 0 to 7 because the list index starts from 0.

    randX = rand.randint(-200, 200)
    randY = rand.randint(-20, 20)

    clickTurtle.hideturtle()
    clickTurtle.goto(randX, randY)
    clickTurtle.color(turtleColors[randColor])
    clickTurtle.showturtle()

def gainCash():
    global cash
    global multiplier
    cash += multiplier
    writeCash(cash) # Writing the cash after player gets it.
    writeMultiplier(multiplier)

def writeCash(cash):
    cashTurtle.clear()
    cashTurtle.write(arg=("Total cash: "+str(cash)),font=("Ariel", 20, "normal"))

def updateMultiplier(x, y):
    global multiplier
    global multiplierUpgradePrice
    global cash

    if cash >= multiplierUpgradePrice:
        print("player has requirments")
        cash -= multiplierUpgradePrice
        multiplier *= 2
        multiplierUpgradePrice *= 3
        writeCash(cash)

    writeMultiplier(multiplier)
    upgradeMultiplierTurtle.clear()
    upgradeMultiplierTurtle.write("Total multiplier: " + str(multiplier)+ "x. You need: "+ str(multiplierUpgradePrice)+" dollars To upgrade!", font=("Ariel", 10, "bold"))

def writeMultiplier(multiplier):
    showMultiplierStats.clear()
    showMultiplierStats.write(arg=("Total multiplier: "+str(multiplier)+"x"), font=("Ariel", 10, "bold"))

    print("HIEHIEAHFIOEAHOFHAOFHOAHEOUEHkfhfi##@@(#*FEHDSUF")
def buyTurtle1(x, y): # buying the turtles
    global cash
    if cash >= shop.t1Price:
        print("Bought t1")
        cash -= shop.t1Price
        turtle1.hideturtle()
        shop.t1PriceTurtle.clear() # Making the price disappear when player buys the cosmetic.

def buyTurtle2(x, y):
    global cash
    if cash >= shop.t2Price:
        print("Bought t2")
        cash -= shop.t2Price
        turtle2.hideturtle()
        shop.t2PriceTurtle.clear()


def buyTurtle3(x, y):
    global cash
    if cash >= shop.t3Price:
        print("Bought t3")
        cash -= shop.t3Price
        turtle3.hideturtle()
        shop.t3PriceTurtle.clear() 


#-- Function calls ---#
shop.initShopTurtles(turtle1, turtle2, turtle3) # Turtles appear and move to their correct positions.

#--- Events ---#
clickTurtle.onclick(click)
upgradeMultiplierTurtle.onclick(updateMultiplier)

turtle1.onclick(buyTurtle1)
turtle2.onclick(buyTurtle2)
turtle3.onclick(buyTurtle3)

wn = trtl.Screen()
wn.mainloop()