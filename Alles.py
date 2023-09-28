#Der Erste Code

#print("Hallo World")

from turtle import *
from turtle import Turtle
import random

c = ["black", "white", "yellow", "green", "red", "blue", "purple"] #Liste mit Farben

while True: #damit jedes mal andere Farben benutzt werden dammit nich auffällt dass jeder das selbe hat 
    color1 = c[random.randint(0, len(c)-1)]
    color2 = c[random.randint(0, len(c)-1)]
    if color1 == color2: # Dass nich die Selbe Farbe für den Roboter und den Hintergrund benutzt wird
        color1 = c[random.randint(0, len(c)-1)]
        color2 = c[random.randint(0, len(c)-1)]
    else:
        break

win = Screen() #Erstellt den Hintergrund
win.bgcolor(color1)

rob = Turtle() #Erstellt den Roboter der alles Zeichnet
rob.pensize(4)
rob.color(color2)
rob.speed(20)

rob.penup() #Bringt den Robter in Position und Rotiert ihn so dass nur eine Zacke oben ist
rob.goto(150, 0)
rob.pendown()
rob.right(15)

for i in range(12): #Zeichnet den Stern 
    rob.right(150)
    rob.forward(300)

rob.penup() #Bringt den Roboter wieder zu seinem Zuhause
rob.home()

rob.screen.mainloop() #Macht dass der Bildschirm Offen bleibt auch nach dem Zeichen des Sterns