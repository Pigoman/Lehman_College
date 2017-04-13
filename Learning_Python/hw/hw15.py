#!/usr/bin/env python3

# Flower Function
# by Sean Curran

from turtle import *

def drawFlower(sean, x, y):
	# Stem
	sean.setheading(90)
	sean.color("green")
	sean.pendown()
	sean.forward(50)
	# Move to make petals
	sean.penup()
	sean.forward(5)
	sean.pendown()
	# Petals
	sean.color("red")
	for i in range(1, 11):
		for j in range(5):
			sean.setheading(72*j)
			sean.circle(i)
	sean.penup()
	# Center
	sean.setposition(x, y+50)
	sean.pendown()
	sean.setheading(0)
	sean.color("yellow")
	for i in range(5):
		sean.circle(i)
	# AT THE END return turtle to original spot
	sean.penup()
	sean.setheading(0)
	sean.setposition(x, y)
	sean.color("black")

def main():
	win = Screen()
	sean = Turtle()
	sean.speed(0)
	sean.shape("turtle")
	sean.resizemode("user")
	sean.turtlesize(0.75, 0.75, 1)
	
	drawFlower(sean, sean.xcor(), sean.ycor())
	
	sean.forward(50)
	
	drawFlower(sean, sean.xcor(), sean.ycor())
	
	sean.left(180)
	sean.forward(100)
	
	drawFlower(sean, sean.xcor(), sean.ycor())
	
	sean.forward(50)
	sean.right(90)
	sean.forward(50)
	sean.right(180)
	
	sean.write("  What pretty flowers!", font=('Arial', 15, 'normal'))
	
	win.exitonclick()

if __name__ == "__main__":
	main()
