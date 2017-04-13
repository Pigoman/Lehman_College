#!/usr/bin/env python3
# ask user for a, b, c
# find x using quadratic equation

import math

a = eval(input("Please enter a value for a: "))
b = eval(input("Please enter a value for b: "))
c = eval(input("Please enter a value for c: "))

disc = math.pow(b,2) - 4 * a * c

xPlus  = (-b + math.sqrt(disc)) / (2 * a)
xMinus = (-b - math.sqrt(disc)) / (2 * a)

print("x is", xPlus, "and", xMinus)
