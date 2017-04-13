#!/usr/bin/env python3

def getLongest(a, b):
	if (len(a) >= len(b)):
		return a
	else:
		return b

def main():
	str1 = input("Enter a string:")
	str2 = input("Enter a string:")
	print(getLongest(str1, str2), "is the longest string.")

if __name__ == "__main__":
	main()
