#!/usr/bin/env python3

from turtle import *

def draw(tur, a, xs):
	tur.right(90 * a)
	for x in xs:
		tur.forward(x)
		tur.backward(x)
		tur.right(90)
		tur.forward(10)
		tur.left(90)

def main():
	t = Turtle()
	t.speed(1)
	win = Screen()
	ls = [64, 16, 32, 16, 64, 16, 32, 16, 64]
	draw(t, 3, ls)
	
	win.exitonclick()

if __name__ == "__main__":
	main()
