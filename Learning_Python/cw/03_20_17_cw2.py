#!/usr/bin/env python3

def main():
	userWord = "hi"
	wordList = []
	while (userWord != ""):
		userWord = input("Please enter a word: ")
		if (userWord != ""):
			wordList.append(userWord)
	for i in wordList:
		print(i)
	print(wordList)

if __name__ == "__main__":
	main()
