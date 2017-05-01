#!/usr/bin/env python3

def main():
	fileName = input("Enter a file name:")
	fileref = open(fileName, 'r')
	for line in fileref:
		print(line.upper())
	fileref.close()

if __name__ == "__main__":
	main()
