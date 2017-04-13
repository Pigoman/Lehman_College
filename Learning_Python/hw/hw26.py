#!/usr/bin/env python3

def main():
	userString = ""
	while (userString == ""):
		userString = input("Enter a non-empty string:")
		if (userString == ""):
			print("Your string was empty.")
	print("You entered the string:", userString)

if __name__ == "__main__":
	main()
