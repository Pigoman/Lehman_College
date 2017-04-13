#!/usr/bin/env python3

def main():
	CUNYs = ["Lehman", "Queens", "Hunter", "Baruch"]
	print(CUNYs)
	print(CUNYs[2])
	print(CUNYs[-1])
	print(CUNYs[1:])
	print(CUNYs[:-2])
	print(CUNYs[1:3])
	print(len(CUNYs))
	CUNYs.append("City")
	print(CUNYs)
	CUNYs[1] = "Brooklyn"
	print(CUNYs)
	for item in CUNYs:
		print(item.upper(),"COLLEGE")
	newList = []
	for i in range(len(CUNYs)):
		newList.append(CUNYs[i].upper())
	print(newList)

if __name__ == "__main__":
	main()
