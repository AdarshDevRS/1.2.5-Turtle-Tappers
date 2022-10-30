#--- Imports ---#
from socket import getfqdn
import turtle as trtl
import random as rand

#--- Creating objects ---# 
clickTurtle = trtl.Turtle() # This turtle will be the turtle the player needs to click to get cash.
cashTurtle = trtl.Turtle() # This turtle shows how much cash total cash the player has.

#--- Config ---#
clickTurtle.shape("circle")
clickTurtle.pensize(5)

turtleColors = ["Purple", "Blue", "Red", "Green", "Yellow", "Black", "Brown", "Cyan"] # The colors the clickTurtle will appear in. (randomly)


#--- Variables ---#
cash = 0
multiplier = 1 # player can upgrade variable so player can earn more cash per click.


#--- Functions ---#
def randomSpawn():
    pass

def gainCash():
    pass

def writeCash():
    pass

def multiplier():
    return # Multiplier


#--- Events ---#


wn = trtl.Screen()
wn.mainloop()