#!/usr/bin/env python3

def main():
	count = 0
	for i in range(10):
		word = input("Enter a word:")
		if(word == "python"):
			count += 1
	print("You entered the word python " + str(count) + " times.")

if __name__ == "__main__":
	main()
