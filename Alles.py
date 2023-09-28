#Der Erste Code

#print("Hallo World")

from turtle import *
from turtle import Turtle
import random

c = ["black", "white", "yellow", "green", "red", "blue", "purple"]

while True:
    color1 = c[random.randint(0, len(c)-1)]
    color2 = c[random.randint(0, len(c)-1)]
    if color1 == color2:
        color1 = c[random.randint(0, len(c)-1)]
        color2 = c[random.randint(0, len(c)-1)]
    else:
        break

win = Screen()
win.bgcolor(color1)
rob = Turtle()
rob.pensize(4)
rob.color(color2)
rob.speed(20)

rob.penup()
rob.goto(150, 0)
rob.pendown()
rob.right(15)
for i in range(12):
    rob.right(150)
    rob.forward(300)
rob.penup()
rob.home()
rob.screen.mainloop()