#!/usr/bin/env python3
# Ask the user for two numbers and print the 
# numbers between the two, inclusive

a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
if a > b:
	temp = a
	a = b
	b = temp
for i in range(a, b+1):
	print(i)
