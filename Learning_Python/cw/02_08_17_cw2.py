#!/usr/bin/env python3
import turtle

win  = turtle.Screen()
sean = turtle.Turtle()
sean.color("black")
sean.pensize(2)
sean.penup()
sean.setposition(-200, 200)
sean.pendown()

for i in range(10):
	sean.forward(25)
	sean.right(90)
	sean.write(i + 1)
	sean.forward(25)
	sean.left(90)

win.exitonclick()
