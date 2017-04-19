#!/usr/bin/env python3

def main():
	names = input("Enter a list of names:")
	print("You entered:")
	names_list = names.split("; ")
	for n in names_list:
		n_l = n.split(", ")
		print(n_l[-1], n_l[0])

if __name__ == "__main__":
	main()
