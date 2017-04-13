#!/usr/bin/env python3

# Calculates the factorial
def fact(num):
	answer = 1
	for i in range(num, 1, -1):
		answer = answer * i
	return answer
	
# Calculates the double factorial (times every second number)
def doubleFact(num):
	answer = 1
	for i in range(num, 1, -2):
		answer = answer * i
	return answer
	
# Calculates the factorial recursively
def recursiveFact(num):
	if num == 1:
		return num
	else:
		return num * recursiveFact(num - 1)

def main():
	num = int(input("Please enter a number and I will calculate the factorial of it: "))
	answer = fact(num)
	print(str(num) + "! = " + str(answer)) 
	answer = doubleFact(num)
	print(str(num) + "!! = " + str(answer))
	answer = recursiveFact(num)
	print(str(num) + "! = " + str(answer) + " calculated using recursion")

if __name__ == "__main__":
	main()
