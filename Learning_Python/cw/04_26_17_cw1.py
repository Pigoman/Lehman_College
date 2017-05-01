#!/usr/bin/env python3

def main():
	fileref = open("nba_2013.csv", 'r')
	line1 = fileref.readline()
	highestPPG = ["John Doe", "-1"]
	for line in fileref:
		lineList = line.split(",")
		avgPts = int(lineList[28]) / int(lineList[4])
		#print(lineList[0] + ": " + str(avgPts))
		if(avgPts > int(highestPPG[1])):
			highestPPG[0] = lineList[0]
			highestPPG[1] = avgPts
	print("Highest Average Points Per Game:", highestPPG)
	'''
		if(int(lineList[2]) >= 30):
			print(line.strip())
	'''

if __name__ == "__main__":
	main()
