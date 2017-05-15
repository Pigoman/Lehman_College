#!/usr/bin/env python3

def main():
	fileref = open("infile2.txt", 'r')
	i = 1
	printed = False
	for line in fileref:
		linelist = line.split()
		for item in linelist:
			if item == "Python":
				print(i, end=" ")
				printed = True
		if(printed):
			print()
			printed = False
		i += 1
	fileref.close()

if __name__ == "__main__":
	main()
