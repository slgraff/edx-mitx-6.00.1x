# Quiz1Problem4.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Quiz 1, Problem 4

# Write a simple procedure, myLog(x, b), that computes the logarithm of a
# number x relative to a base b. For example, if x = 16 and b = 2, then the
# result is 4 - because 2**4 = 16. If x = 15 and b = 3, then the result is 2
# - because 3**2 is the largest power of 3 less than 15.
#
# In other words, myLog should return the largest power of b such that b
# to that power is still less than or equal to x.
#
# x and b are both positive integers; b is an integer greater than or equal
# to 2. Your function should return an integer answer.

# logarithm, def.: a quantity representing the power to which a fixed number
# (the base) must be raised to produce a given number.

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Tests if x is less than the base, b. If true, then we have found
    # the logarithm of x relative to b
    if x < b:
        # Debug string to see progression, values of x, b
        print("x < b. " + "x: " + str(x) + " b: " + str(b))
        return 0
    else:
        # Debug string to see progression, values of x, b
        print("In else. " + "x: " + str(x) + " b: " + str(b))
        return 1 + myLog(x/b, b)

# Examples of calling myLog()
print(myLog(16, 2))
print(myLog(15, 3))
