#!/usr/bin/env python3

def main():
	# open file (load into working memory of computer)
	# initialize fileref as variable for accessing file
	fileref = open("Enrollment.txt", 'r')
	total = 0
	for line in fileref:
		item = line.split()
		total += int(item[1])
	print("Total undergrad:", str(total))
	# ideally, we do want to close files 
	# when we're done using them
	# especially when we're writing to files
	fileref.close()

if __name__ == "__main__":
	main()
