#!/usr/bin/env python3

import turtle

win = turtle.Screen()
sean = turtle.Turtle()
sean.speed(10)

win.setworldcoordinates(-0.5, -0.5, 10, 10)

sean.setposition(0, 0)

# draw horizontal lines
for i in range(10):
	sean.setposition(0, i)
	sean.pendown()
	sean.forward(9)
	sean.penup()

# reset position and turn facing north
sean.setposition(0, 0)
sean.left(90)

#draw vertical lines
for i in range(10):
	sean.setposition(i, 0)
	sean.pendown()
	sean.forward(9)
	sean.penup()

win.exitonclick()
