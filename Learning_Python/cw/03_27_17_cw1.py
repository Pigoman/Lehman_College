#!/usr/bin/env python3

def main():
	num = int(input("Please enter a number: "))
	for i in range(1, num + 1):
		for j in range(i):
			print(i, end = " ")
		print()

if __name__ == "__main__":
	main()
