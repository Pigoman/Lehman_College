#!/usr/bin/env python3

def main():
	number = 1001
	while (number <= 0 or number >= 1000):
		number = int(input("Enter a number between 0 and 1000:"))
		if (number <= 0 or number >= 1000):
			print("Your number is out of range!")
	print("Your number is " + str(number) + ".")

if __name__ == "__main__":
	main()
