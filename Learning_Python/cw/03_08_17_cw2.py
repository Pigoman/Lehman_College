#!/usr/bin/env python3

def main():
	temp = int(input("Please enter the current temperature in farenheit: "))
	if temp < 0:
		print("You should probably stay inside near a heat source.")
	elif temp < 32:
		print("It's below freezing! You need a serious coat.")
	elif temp < 50:
		print("It's pretty cold. You'd better wear a jacket!")
	elif temp < 65:
		print("You can probably get away with a sweatshirt.")
	elif temp < 70:
		print("No coat needed! Sounds like a nice day!")
	elif temp < 80:
		print("You may want to consider shorts, it's getting warm!")
	elif temp < 90:
		print("That's pretty hot, definitely shorts and a t-shirt.")
	elif temp < 100:
		print("Heat wave? Try to stay cool!")
	else:
		print("Stay inside next to the AC.")

if __name__ == "__main__":
	main()
