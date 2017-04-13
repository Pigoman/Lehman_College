#!/usr/bin/env python3

def getFine(speedLimit,actualSpeed):
	speedingBy = int(actualSpeed - speedLimit)
	if ( speedingBy <= 0 ):
		return 0
	elif ( speedingBy <= 15):
		return 100
	else:
		return 100 + 5 * speedingBy

def main():
	spdlim = float(input("Enter the speed limit in miles:"))
	spdact = float(input("Enter the actual speed in miles:"))
	
	fine = getFine(spdlim, spdact)
	
	print("The fine is $" + str(fine) + ".")

if __name__ == "__main__":
	main()
