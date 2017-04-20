#!/usr/bin/env python3

def main():
	toDo = input("Enter a list of things to do (separated by commas):")
	print("To do list")
	toDoList = toDo.split(",")
	num = 1
	for item in toDoList:
		print(str(num) + ". " + item)
		num += 1

if __name__ == "__main__":
	main()
