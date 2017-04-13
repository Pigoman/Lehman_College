#!/usr/bin/env python3

def main():
	numNeg = 0
	for i in range(5):
		num = int(input("Please enter a number: "))
		if num < 0:
			print("That was a negative number!")
			numNeg += 1
	print("You entered", numNeg, "negative numbers.")

if __name__ == "__main__":
	main()
