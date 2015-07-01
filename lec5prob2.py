# lec5prob2.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, problem 2

# Write a function recurPower(base, exp) which computes base**exp by
# recursively calling itself to solve a smaller version of the same
# problem, and then multiplying the result by base to solve the initial problem.

# This function should take in two values - base can be a float or an integer;
# exp will be an integer >= 0. It should return one numerical value. Your code
# must be recursive - use of the ** operator or looping constructs is not allowed.


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    return base * recurPower(base, exp - 1)

# Examples of calling recurPower(), remove before submitting
print "Result calling recurPower(5, 0): " + str(recurPower(5, 0))
print "Result calling recurPower(5, 2): " + str(recurPower(5, 2))
print "Result calling recurPower(4, 5): " + str(recurPower(4, 5))
