#!/usr/bin/env python3

from random import *

def game():
	num = randrange(1, 101)
	run = True
	while run:
		guess = int(input("Guess a number between 1 and 100: "))
		if(guess < num):
			print("Too low!")
		elif(guess > num):
			print("Too high!")
		else:
			print("Got it!")
			run = False

def main():
	run = True
	while run:
		game()
		choice = input("Play again? (Y/N) ")
		if(choice == "N" or choice == "n" or choice == "no" or choice == "No" or choice == "NO" or choice == "nO"):
			run = False
	print("Thanks for playing!")

if __name__ == "__main__":
	main()
