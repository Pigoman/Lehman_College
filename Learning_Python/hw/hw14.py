#!/usr/bin/env python3

# 2048 Game

from turtle import *

def drawGrid(sean):
	for i in range(5):
		sean.setposition(0, i)
		sean.pendown()
		sean.forward(4)
		sean.penup()
	sean.penup()
	sean.setposition(0, 0)
	sean.left(90)
	sean.pendown()
	for i in range(5):
		sean.setposition(i, 0)
		sean.pendown()
		sean.forward(4)
		sean.penup()
	sean.penup()
	sean.setposition(0, 0)
	return

def putNumber(sean, x, y):
	sean.setposition(x + 0.25, y + 0.125)
	sean.write("2",font=('Arial', 40, 'normal'))
	input("Please press enter")
	
	# Clear initial number
	sean.color("white")
	sean.write("2",font=('Arial', 40, 'bold'))
	sean.color("black")
	
	# Write number all the way to the left
	sean.setposition(0.25, y + 0.125)
	sean.write("2",font=('Arial', 40, 'normal'))
	return

def main():
	# Set up turtle and screen
	win = Screen()
	sean = Turtle()
	win.setworldcoordinates(-1, -1, 5, 5)
	sean.speed(0)
	drawGrid(sean)

	#while (1 < 2):
	for i in range(4):
		x = int(input("Please enter the X coordinate: "))
		y = int(input("Please enter the Y coordinate: "))
		putNumber(sean, x, y)
		
	print("GAME OVER?")

	# Window stays open until user clicks x
	win.exitonclick()
	
if __name__ == "__main__":
	main()
