#!/usr/bin/env python3

from turtle import *

def drawSquare():
	sean.pendown()
	for i in range(4):
		sean.forward(50)
		sean.left(90)

win = Screen()
sean = Turtle()

sean.color("blue")
sean.pensize(3)

sean.penup()
sean.left(180)
sean.forward(100)
sean.right(180)
sean.pendown()

for i in range(4):
	sean.forward(100)
	drawSquare()
	sean.right(90)

win.exitonclick()
