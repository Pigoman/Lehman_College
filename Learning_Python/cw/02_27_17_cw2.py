#!/usr/bin/env python3

from math import *

def welcomeMessage():
	print("Welcome to my program!")
	print("It computes the area of a circle")
	print("Then it computes the area of a rectangle")

def areaOfCircle(radius):
	area = radius * radius * pi
	return area
	
def areaOfRect(length, width):
	area = length * width
	return area
	
r = float(input("Enter a radius: "))
a = areaOfCircle(r)
print("The area of the circle is", a)
l = float(input("Enter a length: "))
w = float(input("Enter a width: "))
a = areaOfRect(l, w)
print("The area of the rectangle is", a)
