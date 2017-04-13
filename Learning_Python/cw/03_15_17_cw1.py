#!/usr/bin/env python3

from random import *

def main():
	num = -1
	while num <= 0:
		num = int(input("Please enter a number: "))
	
	for i in range(num):
		print(str(i+1) + ". " + str(randrange(1, 101)))

if __name__ == "__main__":
	main()
