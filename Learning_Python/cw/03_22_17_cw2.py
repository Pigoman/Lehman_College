#!/usr/bin/env python3

def main():
	for i in range(1,101):
		print(i, end=" ")
		if i % 10 == 0:
			print()
	print("Now with two loops")
	for i in range(0,100,10):
		for j in range(1,11):
			print(str(i+j), end=" ")
		print()

if __name__ == "__main__":
	main()
