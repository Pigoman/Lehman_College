#!/usr/bin/env python3

class TrainLine:

	def __init__(self, initname, initlength, initdailyRidership, initcoverageArea):
		self.name = initname
		self.length = initlength
		self.dailyRidership = initdailyRidership
		self.coverageArea = initcoverageArea
	
	def getName(self):
		return self.name
	
	def getLength(self):
		return self.length
		
	def riderDensity(self):
		return self.dailyRidership / self.coverageArea

def overallLength(subway):
	sum = 0
	for train in subway:
		sum += train.getLength()
	return sum

def main():
	# The three commuter rail lines departing from Grand Central
	# Coverage Area is estimated, Length and Ridership come from Wikipedia
	hudson = TrainLine("Hudson   ", 74,  38500,  100)
	harlem = TrainLine("Harlem   ", 82,  43076,  100)
	nhaven = TrainLine("New Haven", 133, 125000, 150)
	MNRR = [hudson, harlem, nhaven]
	print("The total length is:", str(overallLength(MNRR)))
	for train in MNRR:
		print(train.getName() + "\tLength: " + str(train.getLength()) + "\tRider Density: " + str(train.riderDensity()))

if __name__ == "__main__":
	main()
