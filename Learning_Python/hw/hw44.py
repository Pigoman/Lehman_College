#!/usr/bin/env python3

def swapString(string):
	for i in range(len(string)):
		if string[i] == "N" and string[i+1] == "Y":
			string = string[:i] + "New York" + string[i+2:]
		if string[i] == "N" and string[i+1] == "J":
			string = string[:i] + "New Jersey" + string[i+2:]
		if string[i] == "C" and string[i+1] == "T":
			string = string[:i] + "Connecticut" + string[i+2:]
	return string
		

def main():
	fileStrR = input("Enter the name of the file to read: ")
	fileStrW = input("Enter the name of the file to write: ")
	filerefR = open(fileStrR, 'r')
	filerefW = open(fileStrW, 'w')
	
	for line in filerefR:
		lineLst = line.split()
		for i in range(len(lineLst)):
			inner = lineLst[i].split("-")
			for j in range(len(inner)):
				inner[j] = swapString(inner[j])
				filerefW.write(inner[j])
				if len(inner) > 1 and j < len(inner) - 1:
					filerefW.write("-")
			filerefW.write(" ")
		filerefW.write("\n")
	
	filerefR.close()
	filerefW.close()

if __name__ == "__main__":
	main()
