#!/usr/bin/env python3

from turtle import *

sean = Turtle()
win = Screen()
win.setworldcoordinates(-0.5,3.5,3.5,-0.5)

def display(lineLst):
	sean.penup()
	for x in range(4):
		for y in range(4):
			line = lineLst[x].split(",")
			sean.setposition(y, x)
			sean.write(line[y], False, "right", ("Arial", 32, "normal"))

def main():
	fileref = open("testfile_hw45_1.txt", 'r')
	lineLst = []
	for line in fileref:
		lineLst.append(line.strip())
	display(lineLst)
	fileref.close()
	
	win.exitonclick()

if __name__ == "__main__":
    main()
