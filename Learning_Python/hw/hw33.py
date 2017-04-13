#!/usr/bin/env python3

#Introductory Program, Spring 2017
#Lehman College, City University of New York
#Second Version of Tic-Tac-Toe
#   This version checks the number of winning 
#	 positions at the end of the game.

from turtle import *

def setUp():
    #Set up the screen and turtle
    win = Screen()
    tic = Turtle()
    tic.speed(10)
    #Change the coordinates to make it easier to tranlate moves to screen coordinates:
    win.setworldcoordinates(-0.5,-0.5,3.5, 3.5)

    #Draw the vertical bars of the game board:
    for i in range(1,3):
        tic.up()
        tic.goto(0,i)
        tic.down()
        tic.forward(3)

    #Draw the horizontal bars of the game board:
    tic.left(90)    #Point the turtle in the right direction before drawing
    for i in range(1,3):
        tic.up()
        tic.goto(i,0)
        tic.down()
        tic.forward(3)

    tic.up()        #Don't need to draw any more lines, so, keep pen up

    #Set up board:
    board = [["","",""],["","",""],["","",""]]
    
    return(win,tic,board)

def checkInput(checkX, checkY, board):
	if(checkX <= -1 or checkX >= 3 or checkY <= -1 or checkY >= 3 or str(board[checkX][checkY]) != ""):
		print("Please make a valid selection")
		return False
	else:
		return True
	

def playGame(tic,board):
    #Ask the user for the first 8 moves, alternating between the players X and O:
    for i in range(4):
        if checkWinner(board) != "No winner":
            return()
        while True:
            x = int(input("Enter x coordinates for X's move: "))
            y = int(input("Enter y coordinates for X's move: "))
            if(checkInput(x, y, board)):
                break
        tic.goto(x+.25,y+.25)
        tic.write("X",font=('Arial', 90, 'normal'))
        board[x][y] = "X"
        
        if checkWinner(board) != "No winner":
            return()
        
        while True:
            x = int(input("Enter x coordinates for O's move: "))
            y = int(input("Enter y coordinates for O's move: "))
            if(checkInput(x, y, board)):
                break                
        tic.goto(x+.25,y+.25)
        tic.write("O",font=('Arial', 90, 'normal'))
        board[x][y] = "O"
        
    # The ninth move:
    while True:
        x = int(input("Enter x coordinates for X's move: "))
        y = int(input("Enter y coordinates for X's move: "))
        if(checkInput(x, y, board)):
            break
    tic.goto(x+.25,y+.25)
    tic.write("X",font=('Arial', 90, 'normal'))
    board[x][y] = "X"

def checkWinner(board):
    for x in range(3):
        if board[x][0] != "" and (board[x][0] == board[x][1] == board[x][2]):
            return(board[x][0])  #we have a non-empty row that's identical
    for y in range(3):
        if board[0][y] != "" and (board[0][y] == board[1][y] == board[2][y]):
            return(board[0][y])  #we have a non-empty column that's identical
    if board[0][0] != "" and (board[0][0] == board[1][1] == board[2][2]):
        return(board[0][0])
    if board[2][0] != "" and (board[2][0] == board[1][1] == board[2][0]):
        return(board[2][0])   
    return("No winner")

def cleanUp(tic,win):
    #Display an ending message: 
    tic.goto(-0.25,-0.25)
    tic.write("Thank you for playing!",font=('Arial', 20, 'normal'))


def main():
    #playAgain = "yes"
    #while playAgain == "yes" or playAgain == "YES" or playAgain == "Yes" or playAgain == "yEs" or playAgain == "yeS" or playAgain == "YEs" or playAgain == "YeS" or playAgain == "yES" or playAgain == "y" or playAgain == "Y":
	win,tic,board = setUp()   #Set up the window and game board
	playGame(tic,board)       #Ask the user for the moves and display
	print("\nThe winner is", checkWinner(board))  #Check for winner
	cleanUp(tic,win)    #Display end message
        #playAgain = input("Play again?")
        #win.clear()
    
	win.exitonclick()#Closes the graphics window when mouse is clicked


main()
