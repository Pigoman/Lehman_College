#!/usr/bin/env python3

def main():
	fileref = open("infile.txt", 'r')
	outfile = open("outfile.txt", 'w')
	for line in fileref:
		if len(line) >= 15:
			outfile.write(line.upper())
	fileref.close()
	outfile.close()

if __name__ == "__main__":
	main()
