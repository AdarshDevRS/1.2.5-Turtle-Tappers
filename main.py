#--- Imports ---#
from audioop import mul
from functools import update_wrapper
import turtle as trtl
import random as rand

#--- Creating objects ---# 
clickTurtle = trtl.Turtle() # This turtle will be the turtle the player needs to click to get cash.
cashTurtle = trtl.Turtle() # This turtle shows how much cash total cash the player has.
upgradeMultiplierTurtle = trtl.Turtle()
showMultiplierStats = trtl.Turtle()

#--- Config ---#
clickTurtle.shape("circle")
clickTurtle.shapesize(5)
clickTurtle.penup()

cashTurtle.penup()
cashTurtle.hideturtle()
cashTurtle.goto(-80, 300)
cashTurtle.pendown()

upgradeMultiplierTurtle.penup()
upgradeMultiplierTurtle.goto(150, 0)
upgradeMultiplierTurtle.shape("circle")
upgradeMultiplierTurtle.pendown()

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

#--- Events ---#
clickTurtle.onclick(click)
upgradeMultiplierTurtle.onclick(updateMultiplier)

wn = trtl.Screen()
wn.mainloop()