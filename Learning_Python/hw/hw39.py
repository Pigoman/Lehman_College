#!/usr/bin/env python3

def getLengths(myLst):
	LenLst = []
	for item in myLst:
		LenLst.append(len(item))
	return LenLst

def main():
	myStr = input("Enter a list strings separated by commas:")
	StrLst = myStr.split(",")
	print("Your new list is", getLengths(StrLst))

if __name__ == "__main__":
	main()
