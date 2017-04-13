#!/usr/bin/env python3

def countA(s):
	return(s.count("A") + s.count("a"))

def main():
	myStr = input("Please enter a string: ")
	print("Number of 'a':",countA(myStr))

if __name__ == "__main__":
	main()
