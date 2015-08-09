# lec11.4-coordinate.py
#
# Lecture 11 - Classes
# Video 4 - Adding Methods to a Class
#
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python

import math

def sq(x):
    return x*x

class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define a method which Python will use when needs a string to print
    # Without this 'print c' will display line like this:
    #   <__main__.Coordinate object at 0x1006df4d0>
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    def distance(self,other):
        return math.sqrt(sq(self.x - other.x)
                         + sq(self.y - other.y))

c = Coordinate(3,4)
Origin = Coordinate(0,0)

# added print c to show what is printed using new def __str__(self) method
print c
