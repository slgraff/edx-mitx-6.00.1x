# lec8.2-exceptionsCode.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 8, video 2

# Handling exceptions in code
# In Python, raise an exception
# raise Exception("descriptive string")
# Python provides handlers, 'try' and 'except'
# 'else' is executed when clause is executed without problems
# 'finally' clause always executed after try, except, else

def divide(x, y):
    try:
        result = x / y
    # If get a zero division error, handle the error
    except ZeroDivisionError, e:
        print "division by zero! " + str(e)
    #
    else:
        print "result is", result
    #
    finally:
        print "executing finally clause"

def divideNew(x, y):
    try:
        result = x / y
    except ZeroDivisionError, e:
        print "division by zero! " + str(e)
    # In case of a TypeError, recall divideNew casting x and y to ints
    except TypeError:
        divideNew(int(x), int(y))
    else:
        print "result is", result
    finally:
        print "executing finally clause"

# Examples of calling divide to demonstrate exceptions
# divide(3,4)
# divide(3,0)
# divide('3','4')

# Examples of calling divideNew
# divideNew(3,4)
# divideNew(3,0)
# divideNew('3','4')
