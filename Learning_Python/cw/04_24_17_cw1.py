#!/usr/bin/env python3

def main():
	fileref = open("MySecondFile.txt", 'r')
	for line in fileref:
		if(line[0].upper() == "A"):
			print(line.strip())
	fileref.close()

if __name__ == "__main__":
	main()
