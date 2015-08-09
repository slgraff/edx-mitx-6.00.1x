# lec11prob4.py
#
# Lecture 11 - Classes
# Problem 4
#
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python

'''
Consider the following code from the last lecture video:

Your task is to define the following two methods for the Coordinate class:

    1. Add an __eq__ method that returns True if coordinates refer to same point
    in the plane (i.e., have the same x and y coordinate)

    2. Define __repr__, a special method that returns a string that looks like
    a valid Python expression that could be used to recreate an object with the
    same value. In other words, eval(repr(c)) == c given the definition of
    __eq__ from part 1.

    For more on __repr__ see this SO post:

    http://stackoverflow.com/questions/452300/python-object-repr-self-should-be-an-expression
'''

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's x coordinate.
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ', ' + str(self.getY()) + '>'

    # returns True if coordinates refer to same point in the plan
    def __eq__(self, other):
        # check to see if 'other' is same type
        assert type(other) == type(self)
        if self.getX() == other.getX():
            if self.getY() == other.getY():
                return True
        return False

    # returns a string that looks like a valid Python expression that could be
    # used to recreate an object with the same value.
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'


# create new object test_coord
test_coord = Coordinate(10, 20)

# call new methods to determine output
print(test_coord.__eq__(10, 20))
print(test_coord.__eq__(5, 10))

print(test_coord.__repr__())
