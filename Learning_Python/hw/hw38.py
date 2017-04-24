#!/usr/bin/env python3

from turtle import *

def sumRow(nums):
	sum = 0;
	for i in nums:
		sum += i
	return sum

def display(cha, col, row):
	sean = Turtle()
	sean.hideturtle()
	sean.penup()
	sean.goto(col, row)
	sean.write(cha, False, align="center", font=("Arial", 16, "normal"))
	return 0

def main():
	wn = Screen()           #The graphics window
	nums = [[4,3,2,1],[8,7,6,5],[12,11,10,9],[16,15,14,13],[20,19,18,17]] #The numbers to be displayed to the screen
	n = len(nums)           #The number of rows
	m = len(nums[0])        #The number of columns (assumes all same length)
	wn.setworldcoordinates(-0.5,n-0.5,m+2,-1.0)      # Sets screen coordinates so that
                                                    # the origin is in the upper left corner                                                    
	for row in range(n):
		rowTotal = sumRow(nums[row])   #Returns the sum of inputted list
		for col in range(m):
			display(nums[row][col], col, row)  #Displays entry at (col,row)
		display("=", col+1, row)              #Displays "=" at (col+1,row)
		display(rowTotal, col+2, row)         #Displays row total at (col+2,row)

	wn.exitonclick()  #Closes the graphics window when mouse is clicked

if __name__ == "__main__":
    main()
