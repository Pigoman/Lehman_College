#!/usr/bin/env python3

def getFare(z, t):
	if ( z <= 2 and t == "adult" ):
		return 23
	elif ( z <= 2 and t == "child" ):
		return 11.5
	elif ( z == 3 and t == "adult" ):
		return 34.5
	elif ( z <= 4 and t == "child" ):
		return 23
	elif ( z == 4 and t == "adult" ):
		return 46
	else:
		return -1

def main():
	zone = int(input("What is the zone?"))
	ttpe = input("What is the ticket type (adult/child)?")
	
	fare = getFare(zone, ttpe)
	
	print("The fare is", str(fare), "krone.")

if __name__ == "__main__":
	main()
