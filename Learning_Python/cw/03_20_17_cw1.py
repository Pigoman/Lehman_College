#!/usr/bin/env python3

def main():
	userInput = 0
	total = 0
	while (userInput != ""):
		total += int(userInput)
		userInput = input("Please enter a number: ")
	print("Your total is:", total)

if __name__ == "__main__":
	main()
