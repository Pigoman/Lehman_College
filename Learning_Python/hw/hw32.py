#!/usr/bin/env python3

def isExcited(myString):
	if(myString[-1] == "!"):
		return True
	else:
		return False

def main():
	myStr = input("Enter a string:")
	print("Your string ends with an exclamation mark:", isExcited(myStr))

if __name__ == "__main__":
	main()
