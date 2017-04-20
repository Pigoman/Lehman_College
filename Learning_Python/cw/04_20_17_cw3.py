#!/usr/bin/env python3

def main():
	# open file for writing
	outfile = open("myfile.txt", 'w')
	
	outfile.write("Hello!\n")
	outfile.write("The quick brown fox jumped over the lazy dog.\n")
	outfile.write("That was a cool sentence.\n")
	outfile.write("This is a neat file.\n")
	outfile.write("yes.\n")
	for i in range(1,11):
		outfile.write(str(i)+"\n")
	
	outfile.close()

if __name__ == "__main__":
	main()
