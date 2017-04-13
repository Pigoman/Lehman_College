#!/usr/bin/env python3
import turtle

win  = turtle.Screen()
sean = turtle.Turtle()
sean.color("black")
sean.pensize(2)

for i in range(4):
	sean.forward(50)
	sean.color("red")
	sean.forward(50)
	sean.color("black")
	sean.left(90)

win.exitonclick()
