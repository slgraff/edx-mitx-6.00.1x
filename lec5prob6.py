# lec5prob6-lenIter.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, problem 6

# Although Python provides a built-in function for computing the length
# of a string, we can write our own.
#
# Write an iterative function, lenIter, which computes the length of an input
# argument (a string), by counting up the number of characters in the string.

def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    numChars = 0
    for char in aStr:
        numChars += 1
    return numChars

# Examples of calling lenIter
print 'Calling lenIter("Hello, world!"): ' + str(lenIter("Hello, world!"))
