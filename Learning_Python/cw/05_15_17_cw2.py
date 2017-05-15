#!/usr/bin/env python3

def pow2(number):
	if(number <= 1):
		return 2
	else:
		return 2 * pow2(number - 1)

def main():
	number = int(input("Enter a number: "))
	print(pow2(number))

if __name__ == "__main__":
	main()
