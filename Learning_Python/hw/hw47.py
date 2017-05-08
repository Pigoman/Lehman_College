#!/usr/bin/env python3

def main():
	filenameR = input("Enter the file name:")
	filerefR = open(filenameR, 'r')
	
	sum = 0
	for line in filerefR:
		linelist = line.split(",")
		for item in linelist:
			sum += float(item)
	print("The sum of your numbers is", str(sum) + ".")
	
	filerefR.close()

if __name__ == "__main__":
	main()
