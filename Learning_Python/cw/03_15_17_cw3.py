#!/usr/bin/env python3

def main():
	answer = ""
	while answer != "who's there?":
		print("Knock knock!")
		answer = input()
	while answer != "cows go who?":
		print("Cows go")
		answer = input()
	print("No silly, cows go MOO")

if __name__ == "__main__":
	main()
