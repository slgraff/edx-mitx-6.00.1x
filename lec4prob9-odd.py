# lec4prob9-odd.py
# Lecture 4, Problem 9

##Write a Python function, odd, that takes in one number and returns True
##when the number is odd and False otherwise.
##
##You should use the % (mod) operator, not if.
##
##This function takes in one number and returns a boolean.

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''

    # Below did not work as it was returning an int
    # return (x%2)

    # Casted to a boolean, which provided the expected output
    return bool(x%2)
