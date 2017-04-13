#!/usr/bin/env python3

from random import *

sides = int(input("How many sides do we have? "))
rolls = int(input("How many times do we roll? "))

for i in range(rolls):
	print(randrange(1, sides + 1))
