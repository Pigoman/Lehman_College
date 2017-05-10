#!/usr/bin/env python3
#Introductory Programming, Lehman College, CUNY
#Spring 2015
#A template file for drawing earthquake data to the screen
#Already written: functions that
#         setup the screen, and
#         draw ocean boundaries.
#To write: functions that
#         get data from file,
#         parse lines to location to stamp


import turtle

tracy = turtle.Turtle()

def setUpScreen():
     w = turtle.Screen()
     w.setworldcoordinates(-181,-91,181,91)
     return(w)

def drawOceans():
     infile = open("oceansSimplified.json","r")#A file with coordinates field only
     lines = infile.readlines()         #Read in the lines of the file
     tracy.speed(0)

     for line in lines:                
          start = line.find("[[[")+1    #Find where the coordinates start
          end = line.find("]]]}")+2     #    and ends
          coordString = line[start:end] #Grab the coordinates, ignoring last 5 characters in line
                                        #    (not needed in our format)
          coordinates = eval(coordString)    #Turn the string into list of numbers
          #print(coordinates[-1])
          tracy.up()                   #Move to starting point without drawing
          tracy.goto(coordinates[0][0], coordinates[0][1])
          tracy.down()
          #print coordinates
          for point in coordinates:     #For each point in the list of coordinates
               #print(point)
               x = point[0]             #Find the x and y of point
               y = point[1]
               tracy.goto(x,y)          #Move the turtle to the (x,y)


def getQuakeData():
     #Fill in this function definition!#
     filename = input("Enter the Quake file: ")
     print("Reading " + filename + "...")
     fileref = open(filename, 'r')
     filelist = []
     for line in fileref:
         filelist.append(line.split(","))
     fileref.close()
     print("Done")
     return filelist

def drawQuakes(lines):
     #Fill in this function definition!#
     print("Mapping Quakes...")
     tracy.penup()
     for i in range(len(lines)):
         if i > 0:
             tracy.goto(float(lines[i][2]), float(lines[i][1]))
             tracy.dot(5, "red")
     print("Done")
     
def main():
     w = setUpScreen()   #Set up the screen with lower left (-90,-180) and upper right (90,180)
     drawOceans()        #Draws oceans using the oceansSimplified.json file
     lines = getQuakeData()   #Asks user for quake file and returns list of lines
     drawQuakes(lines)   #Stamps at each point in each line
     w.exitonclick()     #Close the window when clicked

if __name__ == "__main__":
	main()
