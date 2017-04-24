#!/usr/bin/env python3

def main():
	infile = open("MySecondFile.txt", 'r')
	s = infile.read() # read entire file as a string
	print(s)
	
	infile.close()
	
	print("-"*10)
	
	infile = open("MySecondFile.txt", 'r')
	s = infile.readline() # reads in one line of file
	print(s)
	t = infile.readline()
	print(t)
	infile.close()
	
	infile = open("MySecondFile.txt", 'r')
	s = infile.readlines()
	print(s)
	infile.close()

if __name__ == "__main__":
	main()
