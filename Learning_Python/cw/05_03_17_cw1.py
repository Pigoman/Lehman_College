#!/usr/bin/env python3

def convert(numLst):
	for i in range(len(numLst)):
		numLst[i] = int(numLst[i])
	return numLst
	
def getSum(numLst):
	numLst = convert(numLst)
	sum = 0
	for item in numLst:
		sum += item
	return sum

def main():
	myNumStr = input("Please enter numbers separated by commas: ")
	print("The sum is:", getSum(myNumStr.split(",")))

if __name__ == "__main__":
	main()
