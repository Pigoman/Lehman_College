#!/usr/bin/env python3

# write a function that takes in a list of words
# and returns a list of only those words with
# 5 letters or more

def getLargeWords(li):
	nli = []
	for l in li:
		if len(l) > 4:
			nli.append(l)
	return nli

def main():
	myList = ["cat", "dog", "elephant", "squirrel"]
	newList = getLargeWords(myList)
	print("Long words are:", newList)

if __name__ == "__main__":
	main()
