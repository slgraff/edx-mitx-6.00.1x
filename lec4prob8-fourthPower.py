# lec4prob8
# Lecture 4, Problem 8

##Write a Python function, fourthPower, that takes in one number and
##returns that value raised to the fourth power.
##
##You should use the square procedure that you defined in Problem 3 of
##these lecture exercises (you don't need to redefine square in this box;
##when you call square, the tutor will use our definition).
##
##This function takes in one number and returns one number.

# This is the square function from Lecture 4.3
def square(x):
    '''
    x: int or float.
    '''
    return (x**2)

# This is my code for thie exercise.
# Online code checker is always returning following error:
# TypeError: float argument required, not NoneType
# Determined error was that I was not returning a value from function

def fourthPower(x):
    '''
    x: int or float.
    '''
    # square(square(x)) 
    return square(square(x))

# Test cases
# All run fine in IDLE IDE
print "Fourth Power of -1.47 is " + str(fourthPower(-1.47))
print "Fourth Power of -8.78 is " + str(fourthPower(-8.78))
print "Fourth Power of 3.32 is " + str(fourthPower(3.32))
print "Fourth Power of 2.06 is " + str(fourthPower(2.06))
print "Fourth Power of -8.71 is " + str(fourthPower(-8.71))
