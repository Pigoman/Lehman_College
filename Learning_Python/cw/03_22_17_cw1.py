#!/usr/bin/env python3

from turtle import *

win = Screen()
sean = Turtle()
sean.speed(5)
sean.shape("turtle")
sean.color("green")
sean.resizemode("user")
sean.turtlesize(0.5, 0.5, 1)

def drawSquare(c, size):
	newX = -size/2
	newY = -size/2
	sean.color(c)
	sean.penup()
	sean.setposition(newX, newY)
	sean.pendown()
	for i in range(4):
		sean.forward(size)
		sean.left(90)
	sean.penup()
	sean.setposition(0,0)
	sean.color("green")

def main():
	colorList = []
	color = "black"
	print("Press enter to draw squares")
	while color != "":
		color = input("Please enter a color: ")
		if color != "":
			colorList.append(color)
	for i in range(len(colorList)):
		print(colorList[i])
		drawSquare(colorList[i], (i + 1) * 20)
	print("Close turtle window to quit")
	
	win.exitonclick()

if __name__ == "__main__":
	main()
