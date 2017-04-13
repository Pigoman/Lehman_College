#!/usr/bin/env python3

def removeAone(word):
	word = word.replace("a", "")
	word = word.replace("A", "")
	return word

def removeAtwo(word):
	newWord1 = ""
	newWord2 = ""
	wordList = word.split("a")
	for i in wordList:
		newWord1 += i
	wordList = newWord1.split("A")
	for i in wordList:
		newWord2 += i
	return newWord2
	
def removeAthree(word):
	word = word.replace("A", "a")
	firstA = word.find("a")
	if(firstA == -1):
		return word
	else:
		return removeAthree(word[0:firstA] + word[firstA+1:len(word)])
		

def main():
	word = input("Please enter a word: ")
	print(removeAone(word))
	print(removeAtwo(word))
	print(removeAthree(word))

if __name__ == "__main__":
	main()
