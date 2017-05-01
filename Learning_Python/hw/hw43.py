#!/usr/bin/env python3

from turtle import *

sean = Turtle()
win = Screen()

def drawGrid(size):
	for i in range(size + 1):
		sean.penup()
		sean.goto(0, i)
		sean.pendown()
		sean.forward(size)
	sean.penup()
	sean.goto(0, 0)
	sean.left(90)
	for i in range(size + 1):
		sean.penup()
		sean.goto(i, 0)
		sean.pendown()
		sean.forward(size)
	sean.penup()
	sean.goto(0, 0)
	
def drawCheckers(size):
	sean.penup()
	sean.setheading(90)
	for i in range(size):
		for j in range(size):
			sean.goto(j, i)
			if (j + i) % 2 == 0:
				sean.color("black")
			else:
				sean.color("white")
			sean.begin_fill()
			for x in range(4):
				sean.forward(1)
				sean.right(90)
			sean.end_fill()
			sean.goto(j, i)

def main():
	size = int(input("Enter a size for a checkered flag: "))
	upperBound = size * 2
	win.setworldcoordinates(-0.5, -0.5, upperBound + 0.5, upperBound + 0.5)
	sean.speed(0)
	sean.color("black")
	drawGrid(upperBound)
	drawCheckers(upperBound)
	
	win.exitonclick()

if __name__ == "__main__":
	main()
