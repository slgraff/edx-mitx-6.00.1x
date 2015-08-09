# lec11prob3.py
#
# Lecture 11 - Classes
# Problem 3
#
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python

# Below is a transcript of a session with the Python shell. Provide the type
# and value of the expressions being evaluated. If evaluating an expression
# would cause an error, select NoneType and write error in the box. If the
# result is a function, select function and write function in the box. As
# always, try to do this problem by hand before turning to your interpreter
# for help.

# Assume the following definitions have been made:

class Wierd(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return x
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y

X = 7
Y = 8


# provide type and value of following expressions given following transcript
# in Python shell

w1 = Weird(X, Y)
print w1.getX()

print w1.getY()

w2 = Wild(X, Y)
print w2.getX()

print w2.getY()

w3 = Wild(17, 18)
print w3.getX()

print w3.getY()

w4 = Wild(X, 18)
print w4.getX()

print w4.getY()

X = w4.getX() + w3.getX() + w2.getX()
print X

print w4.getX()

Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print Y

print w2.getY()
