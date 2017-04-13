#!/usr/bin/env python3

def main():
	numChars = int(input("How many letters will you enter?"))
	reverseString = ""
	for i in range(numChars):
		charEntered = input("Enter a letter:")
		reverseString = charEntered + reverseString
	print("Your string backwards is " + reverseString + ".")

if __name__ == "__main__":
	main()
