#!/usr/bin/env python3

def main():
	num = int(input("Enter a positive number:"))
	for i in range(1, num + 1):
		for j in range(1, num + 1):
			print(j, end = " ")
		print()

if __name__ == "__main__":
	main()
