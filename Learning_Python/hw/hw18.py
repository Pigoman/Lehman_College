#!/usr/bin/env python3

def getNumCharacters(firstName,lastName):
	length = len(firstName) + len(lastName)
	return length

def main():
	fname = input("Enter your first name:")
	lname = input("Enter your last name:")
	numChars = getNumCharacters(fname,lname)
	print("There are", numChars, "characters in your full name.")

if __name__ == "__main__":
	main()
