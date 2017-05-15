#!/usr/bin/env python3

class Chocolate:

	def __init__(self, n, ppp, w, coo):
		self.name = n
		self.pricePerPound = ppp
		self.weight = w
		self.countryOfOrigin = coo
		
	def cost(self):
		return self.pricePerPound * self.weight
	
	def getWeight(self):
		return self.weight
	
	def getName(self):
		return self.name

def maxCost(shoppingList):
	mostExpensive = shoppingList[0]
	for item in shoppingList:
		if(item.cost() > mostExpensive.cost()):
			mostExpensive = item
	return mostExpensive

def main():
	hersheys = Chocolate("Hersheys", 1.00, 5.00, "United States")
	lindt = Chocolate("Lindt", 2.00, 5.00, "Switzerland")
	godiva = Chocolate("Godiva", 3.00, 5.00, "Belgium")
	cadbury = Chocolate("Cadbury", 1.50, 5.00, "United Kingdom")
	ChocList = [hersheys, lindt, godiva, cadbury]
	print(maxCost(ChocList).getName())

if __name__ == "__main__":
	main()
