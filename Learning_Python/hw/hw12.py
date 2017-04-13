#!/usr/bin/env python3

import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

sean = turtle.Turtle()     # 3.  Create two turtles
amy = turtle.Turtle()
sean.color('red')
amy.color('blue')
sean.shape('turtle')
amy.shape('turtle')

sean.up()                  # 4.  Move the turtles to their starting point
amy.up()
sean.goto(-300,20)
amy.goto(-300,-20)

# your code goes here
for i in range(100):
	sean.forward(random.randrange(1,11))
	amy.forward(random.randrange(1,11))

wn.exitonclick()
