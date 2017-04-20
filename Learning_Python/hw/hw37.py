#!/usr/bin/env python3

def titleList(myList):
	titledList = []
	myString = ""
	for item in myList:
		itemList = item.split()
		for thing in itemList:
			myString = myString + thing[0].upper() + thing[1:] + " "
		titledList.append(myString.strip())
		myString = ""
	return titledList

def main():
	myString = input("Enter a list of strings separated by commas:")
	myList = myString.split(",")
	myTitledList = titleList(myList)
	print("Your new list is", myTitledList)

if __name__ == "__main__":
	main()
