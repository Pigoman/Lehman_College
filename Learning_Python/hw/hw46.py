#!/usr/bin/env python3

def main():
	filenameR = input("Enter the name of a file: ")
	namelist = filenameR.split(".")
	filenameW = namelist[0] + "_out.txt"
	filerefR = open(filenameR, 'r')
	filerefW = open(filenameW, 'w')
	
	i = 1
	for line in filerefR:
		filerefW.write(str(i)+"\t"+line)
		i += 1
	
	filerefR.close()
	filerefW.close()

if __name__ == "__main__":
	main()
