#!/usr/bin/env python3

# add numbers using an accumulator
def addNums():
	times = int(input("How many numbers do you want to add up? "))
	total = 0
	for i in range(times):
		num = int(input("Please enter a number: "))
		total = total + num	
	print("The sum of your numbers is:", total)
	
# concatinate words using an accumulator
def addWords():
	times = int(input("How many words do you want to put together? "))
	total = ""
	for i in range(times):
		theirWord = input("Please enter a word: ")
		total = total + theirWord + " "
	print("Your sentence is:", total)
	
# count characters in words using an accumulator
def lengthWords():
	times = int(input("How many words do you want to count? "))
	total = 0
	for i in range(times):
		theirWord = input("Please enter a word: ")
		total = total + len(theirWord)	
	print("The total number of characters entered is:", total)

def main():
	lengthWords()	

if __name__ == "__main__":
	main()
