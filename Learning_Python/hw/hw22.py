#!/usr/bin/env python3

from turtle import *

def main():
	win = Screen()
	sean = Turtle()
	sean.speed(1)
	sean.shape("turtle")
	sean.resizemode("user")
	sean.turtlesize(0.75, 0.75, 1)
	sean.setheading(90)
	
	num = int(input("Please enter a number: "))
	
	if ( num % 2 == 0 ):
		sean.write("  EVEN", font=('Arial', 15, 'normal'))
		sean.color("blue")
		sean.left(90)
		sean.forward(1000)
	else:
		sean.write("  ODD", font=('Arial', 15, 'normal'))
		sean.color("red")
		sean.right(90)
		sean.forward(1000)
	
	win.exitonclick()

if __name__ == "__main__":
	main()
