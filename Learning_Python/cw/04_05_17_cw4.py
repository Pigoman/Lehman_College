#!/usr/bin/env python3

# Translates sentences, does not account for punctuation

def translateToPigLatin(word):
	latin = ""
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	punct = ""
	
	for i in range(len(alphabet)):
		if(word[-1] == alphabet[i]):
			punct = ""
			break
		else:
			punct = word[-1]
	if(punct != ""):
		word = word[0:len(word)]
	
	if(word[0].upper() == "A" or word[0].upper() == "E" or word[0].upper() == "I" or word[0].upper() == "O" or word[0].upper() == "U"):
		latin = word + "hay" + punct
	elif(word[1].upper() == "A" or word[1].upper() == "E" or word[1].upper() == "I" or word[1].upper() == "O" or word[1].upper() == "U" or word[1].upper() == "Y"):
		for i in range(len(word)):
			latin += word[(i + 1) % len(word)]
		latin += "ay" + punct
	elif(word[2].upper() == "A" or word[2].upper() == "E" or word[2].upper() == "I" or word[2].upper() == "O" or word[2].upper() == "U" or word[2].upper() == "Y"):
		for i in range(len(word)):
			latin += word[(i + 2) % len(word)]
		latin += "ay" + punct
	elif(word[3].upper() == "A" or word[3].upper() == "E" or word[3].upper() == "I" or word[3].upper() == "O" or word[3].upper() == "U" or word[3].upper() == "Y"):
		for i in range(len(word)):
			latin += word[(i + 3) % len(word)]
		latin += "ay" + punct
	else:
		latin = "INVALID WORD"
	return latin

def main():
	sentence = input("Enter a sentence:")
	sentenceLI = sentence.split()
	translatedSentence = ""
	for i in range(len(sentenceLI)):
		sentenceLI[i] = translateToPigLatin(sentenceLI[i])
		translatedSentence += sentenceLI[i] + " "
	print("Your sentence in Pig Latin is:", translatedSentence, ".")

if __name__ == "__main__":
	main()
