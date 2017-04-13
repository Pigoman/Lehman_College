#!/usr/bin/env python3

def getNumTrips(balance):
	numTrips = int(balance / 2.75)
	return numTrips

def main():
	bal = float(input("Enter your Metrocard balance:"))
	trips = getNumTrips(bal)
	print("You can take", trips, "more trips on the subway.")

if __name__ == "__main__":
	main()
