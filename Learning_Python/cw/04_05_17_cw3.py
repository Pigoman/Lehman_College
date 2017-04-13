#!/usr/bin/env python3

def getSquares(li):
	newLI = []
	for item in li:
		newLI.append(item**2)
	return newLI
	
def getSum(li):
	mySum = 0
	for i in li:
		mySum += i
	return mySum

def main():
	numLI = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	squLI = getSquares(numLI)
	print(numLI)
	print(squLI)
	print(getSum(numLI))

if __name__ == "__main__":
	main()
