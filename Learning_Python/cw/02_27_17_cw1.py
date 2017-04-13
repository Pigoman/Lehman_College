#!/usr/bin/env python3

from random import *
from turtle import *

win = Screen()
sean = Turtle()
sean.color(random(), random(), random())
sean.pensize(3)

for i in range(50):
	sean.forward(randrange(1,101))
	sean.right(90)
	sean.color(random(), random(), random())

win.exitonclick()
