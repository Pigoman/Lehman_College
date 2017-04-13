#!/usr/bin/env python3

from random import *

rollTotal = 0

for i in range(2):
	roll = randrange(1,7)
	print("Roll " + str(i + 1) + ": " + str(roll))
	rollTotal += roll

print("Sum: " + str(rollTotal))
