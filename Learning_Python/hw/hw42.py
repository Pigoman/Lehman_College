#!/usr/bin/env python3

def main():
	fileName = input("Enter a file name:")
	print("The first letters fo the lines in your file are:")
	fileref = open(fileName, 'r')
	for line in fileref:
		if line[0] == "\n":
			print()
		else:
			print(line[0])
	fileref.close()

if __name__ == "__main__":
	main()
