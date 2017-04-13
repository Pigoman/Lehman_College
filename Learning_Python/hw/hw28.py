#!/usr/bin/env python3

#Author:    Katherine St. John
#Date:      August 2014
#A program that uses command strings to control turtle drawing
#Modified by:  Sean Curran
#Date:      Wednesday March 22, 2017

import turtle


#doAction() takes a turtle and a character and has the turtle perform
#   action indicated by the character
def doAction(t,c):
    if c == 'F':            #move forward
        t.forward(50)
    elif c == 'B':          #move backward
        t.backward(50)
    elif c == 'L':          #turn left
        t.left(90)
    elif c == 'R':          #turn right
        t.right(90)
    elif c == '^':          #lift pen
        t.up()
    elif c == 'v':          #lower pen
        t.down()
    elif c == 'r':          #set color to red
        t.color("red")
    elif c == 'g':          #set color to green
        t.color("green")
    elif c == 'b':          #set color to blue
        t.color("blue")
    else:                   #for any other character, print an error message 
        print("Error: do not know the command:", c)


def main():
    silas = turtle.Turtle()
    myWin = turtle.Screen()     #The graphics window
    commands = input("Please enter a command string: ")
    for ch in commands:         # Loop once for each letter in the string commands.
                                # The letter for each time through the loop is stored in ch.
        doAction(silas,ch)

    print("See graphics window for your image")
    myWin.exitonclick()         #Close the window when clicked

main()


