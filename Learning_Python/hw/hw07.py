# Write your name on the screen, surrounded by a box or a polygon
import turtle

win  = turtle.Screen()
sean = turtle.Turtle()
sean.color("blue")
sean.pensize(2)

# Move over to a nicer starting position
sean.penup()
sean.setposition(-100, 100)
sean.left(180)
sean.pendown()

# S
sean.forward(50)
sean.left(90)
sean.forward(50)
sean.left(90)
sean.forward(50)
sean.right(90)
sean.forward(50)
sean.right(90)
sean.forward(50)

# move
sean.penup()
sean.right(90)
sean.forward(25)
sean.right(90)
sean.forward(75)
sean.pendown()

# e
sean.forward(50)
sean.left(90)
sean.forward(25)
sean.left(90)
sean.forward(50)
sean.left(90)
sean.forward(50)
sean.left(90)
sean.forward(50)

# move
sean.penup()
sean.forward(25)
sean.left(90)
sean.forward(50)
sean.pendown()

# a
sean.right(90)
sean.forward(45)
sean.right(90)
sean.forward(50)
sean.right(90)
sean.forward(45)
sean.right(90)
sean.forward(25)
sean.right(90)
sean.forward(45)
sean.penup()
sean.right(90)
sean.forward(25)
sean.left(90)
sean.pendown()
sean.forward(5)

# move
sean.penup()
sean.forward(25)
sean.pendown()

# n
sean.left(90)
sean.forward(50)
sean.right(180)
sean.penup()
sean.forward(5)
sean.pendown()
sean.left(90)
sean.forward(50)
sean.right(90)
sean.forward(45)

# move to make box
sean.penup()
sean.setposition(-175, 125)
sean.pendown()
sean.color("purple")

# box
for i in range(2):
	sean.forward(150)
	sean.left(90)
	sean.forward(325)
	sean.left(90)

sean.penup()
sean.setposition(0, 100)
sean.color("red")
for i in range(10):
	sean.left(180)

input("Press enter to quit")
