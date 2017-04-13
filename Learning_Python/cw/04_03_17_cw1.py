#!/usr/bin/env python3

def getDash(lname):
	for i in range(len(lname)):
		if(lname[i] == "-"):
			return i
	return -1

def getInitials(fname, lname):
	dashPos = getDash(lname)
	if(dashPos == -1):
		return fname[0].upper() + "." + lname[0].upper() + "."
	else:
		return fname[0].upper() + "." + lname[0].upper() + "-" + lname[dashPos + 1].upper() + "."

def main():
	fname = input("Please enter your first name: ")
	lname = input("Please enter your last name: ")
	print("Your initials are", getInitials(fname, lname))

if __name__ == "__main__":
	main()
