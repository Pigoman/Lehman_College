#!/usr/bin/env python3

from random import *

def main():
	numRolls = int(input("Enter the number of dice to roll:"))
	diceTotal = 0
	for i in range(numRolls):
		diceTotal += randrange(1,7)
	print("The sum of " + str(numRolls) + " dice rolls is " + str(diceTotal) + ".")

if __name__ == "__main__":
	main()
