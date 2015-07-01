# lec5prob3.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, problem 3

# The function recurPower(base, exp) from Problem 2 computed base**exp by
# decomposing the problem into one recursive case and one base case:
#
# base ** exp = base * base ** (exp - 1) if exp > 0
# base ** exp = 1 if exp = 0
#
# Another way to solve this problem just using multiplication
# (and remainder) is to note that:

# base**exp = (base**2)**(exp/2) if exp > 0 and exp is even
# base**exp = base * (base**(exp - 1)) if exp > 0 and exp is odd
# base**exp = 1 if exp = 0
#
# Write a procedure recurPowerNew which recursively computes exponentials
# using this idea.

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here

    if exp == 0:
        return 1
    else:
        if (exp%2 == 0):
            # exp is even
            return recurPowerNew((base * base), exp/2)

        else:
            # exp is odd
            return base * recurPowerNew(base, (exp - 1))

# Examples of calling recurPowerNew
print "Calling recurPowerNew(5, 0): " + str(recurPowerNew(5, 0))
print "Calling recurPowerNew(4, 2): " + str(recurPowerNew(4, 2))
print "Calling recurPowerNew(3, 3): " + str(recurPowerNew(3, 3))
