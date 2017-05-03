#!/usr/bin/env python3

# to make a class:

class City:
	
	# make a constructor
	
	def __init__(self, initName, initPop, initArea):
		self.name = initName
		self.population = initPop
		self.area = initArea
	
	def getName(self):
		return self.name
	
	def getPopulation(self):
		return self.population
		
	def getArea(self):
		return self.area
		
	def setName(self, newName):
		self.name = newName
	
	def setPopulation(self, newPop):
		self.population = newPop
	
	def setArea(self, newArea):
		self.Area = newArea
		
	def calcDensity(self):
		return self.population / self.area
		
newYork = City("New York", 85000000, 470)
print(newYork)
print(newYork.getName())
print(newYork.getPopulation())
print(newYork.getArea())
print(newYork.calcDensity())
