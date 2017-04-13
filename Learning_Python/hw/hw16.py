#!/usr/bin/env python3

# Sean Curran

from turtle import *

# I've found that functions need the turtle object 
# passed to them as well as the parameter, at least
# on my computer, so that is what I have been doing
# for the last few homeworks. I hope that is okay
def drawSquare(sean, size):
	newX = -size/2
	newY = -size/2
	sean.penup()
	sean.setposition(newX, newY)
	sean.pendown()
	for i in range(4):
		sean.forward(size)
		sean.left(90)
	sean.penup()
	sean.setposition(0,0)

def main():
	win = Screen()
	sean = Turtle()
	sean.speed(5)
	sean.shape("turtle")
	sean.resizemode("user")
	sean.turtlesize(0.75, 0.75, 1)
	
	squareSize = int(input("Please enter the length of the sides of the square: "))
	drawSquare(sean, squareSize)
	
	print("Done")
	
	win.exitonclick()

if __name__ == "__main__":
	main()
