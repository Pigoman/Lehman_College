#!/usr/bin/env python3

def main():
	cont = ""
	while(cont != "y" and cont != "n"):
		cont = input("Would you like to continue? (y/n) ")
		if(cont != "y" and cont != "n"):
			print("Please enter a valid selection")
		else:
			print(cont)

if __name__ == "__main__":
	main()
