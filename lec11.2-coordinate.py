# lec11-coordinate.py
#
# Lecture 11 - Classes
# Video 2 - A Class Example
#
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python


import math

def sq(x):
    return x*x

# create an object, Coordinate, that extends Object
class Coordinate(object):
    # define initialization method
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    def distance(self,other):
        return math.sqrt(sq(self.x - other.x)
                         + sq(self.y - other.y))

# create an instance of Coordinate named 'c'
c = Coordinate(3,4)

# create a second instance of Coordinate named Origin
origin = Coordinate(0,0)

print(c.x, origin.x)
