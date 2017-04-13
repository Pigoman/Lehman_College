#!/usr/bin/env python3

def min(num1, num2, num3):
	if ( num1 < num2 and num1 < num3):
		return num1
	elif ( num2 < num1 and num2 < num3):
		return num2
	else:
		return num3

def main():
	print("I WILL USE THE WIZARDRY OF ELECTRICITY TO TELL YOU THE SMALLEST NUMBER")
	nums = []
	for i in range(3):
		nums.append(int(input("Please enter number " + str(i + 1) + ": ")))
	print("The smallest number  : " + str(min(nums[0], nums[1], nums[2])))
		

if __name__ == "__main__":
	main()
