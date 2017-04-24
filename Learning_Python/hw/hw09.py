#!/usr/bin/env python3

import math

num = int(input("Enter the max radius:"))
print("Radius Area of circle")
for i in range(1, num + 1):
	area = math.pi * math.pow(i, 2)
	print(i, area)
