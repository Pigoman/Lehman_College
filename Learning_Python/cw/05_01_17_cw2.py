#!/usr/bin/env python3

def main():
	fileref = open("SandwichTweets.txt", 'r')
	timelst = []
	timefreq = []
	# set up list of zeros to tally frequency of hours
	for i in range(24):
		timefreq.append(0)
	
	# get a list of all of the hours from all of the tweets
	for line in fileref:
		linelst = line.split("\t")
		timelst.append(int(linelst[2][11:13]))
	
	# tally the times
	for item in timelst:
		#print(item)
		for hour in range(24):
			if item == hour:
				timefreq[hour] += 1
	
	# print time frequency
	for i in range(24):
		if(i < 10):
			print(" ", end=(""))
		print(i, " ", end=(""))
	print()
	for i in range(24):
		if(timefreq[i] < 10):
			print(" ", end=(""))
		print(timefreq[i], " ", end=(""))
	print()
			

if __name__ == "__main__":
	main()

# import the file

# make list of the times

# calculate avg hour
# calculate most frequent hour
