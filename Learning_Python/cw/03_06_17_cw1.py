#!/usr/bin/env python3

def function1():
	print("Hello!")

def function2(myNum):
	myNum = myNum + 5
	return myNum
	
def function3(myString):
	print(myString)

def main():
	function1()
	num = 5
	print(num)
	num = function2(num)
	print(num)
	string = "I'm going through function 3"
	function3(string)

if __name__ == "__main__":
	main()
