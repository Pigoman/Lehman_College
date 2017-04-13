#!/usr/bin/env python3

from math import *

def EuclideanDistance(x1, y1, x2, y2):
	distance = float(sqrt( (x2 - x1)**2 + (y2 - y1)**2 ))
	return distance

def main():
	x1 = int(input("Please enter a value for x1: "))
	y1 = int(input("Please enter a value for y1: "))
	x2 = int(input("Please enter a value for x2: "))
	y2 = int(input("Please enter a value for y2: "))
	ED = EuclideanDistance(x1, y1, x2, y2)
	print("The distance between the points is:", ED)

if __name__ == "__main__":
	main()
