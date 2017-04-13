#!/usr/bin/env python3
import turtle           # loads in the turtle library (library is a set of commands)

win  = turtle.Screen()  # makes graphics window
sean = turtle.Turtle()  # make new turtle object
sean.color("blue")

# Writes an S
sean.left(180)
sean.forward(100)
sean.left(90)
sean.forward(50)
sean.left(90)
sean.forward(100)
sean.right(90)
sean.forward(50)
sean.right(90)
sean.forward(100)

# move over without drawing
sean.up()
sean.right(180)
sean.forward(200)
sean.down()

# loop to draw a square
for i in range(4):
	sean.forward(100)
	sean.left(90)

win.exitonclick()
