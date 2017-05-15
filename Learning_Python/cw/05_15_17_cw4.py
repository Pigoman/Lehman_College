#!/usr/bin/env python3

def fib(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, sum(a, b)
	return a

def sum(a, b):
	return a + b

def main():
	print(str(fib(0)))
	print(str(fib(3)))
	print(str(fib(5)))

if __name__ == "__main__":
	main()
