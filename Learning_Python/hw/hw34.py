#!/usr/bin/env python3

def translateToPigLatin(word):
	latin = ""
	if(word[0].upper() == "A" or word[0].upper() == "E" or word[0].upper() == "I" or word[0].upper() == "O" or word[0].upper() == "U"):
		latin = word + "hay"
	elif(word[1].upper() == "A" or word[1].upper() == "E" or word[1].upper() == "I" or word[1].upper() == "O" or word[1].upper() == "U" or word[1].upper() == "Y"):
		for i in range(len(word)):
			latin += word[(i + 1) % len(word)]
		latin += "ay"
	elif(word[2].upper() == "A" or word[2].upper() == "E" or word[2].upper() == "I" or word[2].upper() == "O" or word[2].upper() == "U" or word[2].upper() == "Y"):
		for i in range(len(word)):
			latin += word[(i + 2) % len(word)]
		latin += "ay"
	elif(word[3].upper() == "A" or word[3].upper() == "E" or word[3].upper() == "I" or word[3].upper() == "O" or word[3].upper() == "U" or word[3].upper() == "Y"):
		for i in range(len(word)):
			latin += word[(i + 3) % len(word)]
		latin += "ay"
	else:
		latin = "INVALID WORD"
	return latin

def main():
	word = input("Enter a word:")
	print("Your word in Pig Latin is", translateToPigLatin(word) + ".")

if __name__ == "__main__":
	main()
