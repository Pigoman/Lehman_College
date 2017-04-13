#!/usr/bin/env python3

def convertCurrency(c, d):
	convert = 0.0
	billType = ""
	if ( c == "Japan" ):
		convert = d * 83.85
		billType = "Yen"
	elif ( c == "Indonesia" ):
		convert = d * 9639.99
		billType = "Rupiahs"
	elif ( c == "Hungary" ):
		convert = d * 0.00456
		billType = "Forints"
	else:
		convert = -1
	return convert, billType

def main():
	print("This program converts US Dollars to the currency of Japan, Indonesia, or Hungary.")
	country = input("Please enter the country: ")
	dollars = float(input("Please enter the US dollar amount: "))
	amount, bill = convertCurrency(country, dollars)
	if ( amount == -1 ):
		print("Sorry, I could not understand you")
	else:
		print("$" + str(dollars) + " is " + str(amount) + " " + bill)

if __name__ == "__main__":
	main()
