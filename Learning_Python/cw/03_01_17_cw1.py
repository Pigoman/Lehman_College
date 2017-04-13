#!/usr/bin/env python3

def conversion(c):
	f = float(c * (9.0 / 5.0) + 32)
	return f
	
def main():
	degC = float(input("Please enter degrees in celsius: "))
	degF = conversion(degC)
	print(degC, "degrees celsius is", degF, "degrees farenheit")

if __name__ == "__main__":
	main()
