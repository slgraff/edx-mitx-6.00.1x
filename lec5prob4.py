# lec5prob4.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, problem 4

# The greatest common divisor of two positive integers is the largest integer
# that divides each of them without remainder. For example:
#
# gcd(2, 12) = 2
# gcd(6, 12) = 6
# gcd(9, 12) = 3
# gcd(17, 12) = 1
#
# Write an iterative function, gcdIter(a, b), that implements this idea.
# One easy way to do this is to begin with a test value equal to the smaller
# of the two input arguments, and iteratively reduce this test value by 1
# until you either reach a case where the test divides both a and b
# without remainder, or you reach 1.

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    divisor = 0

    # Test to see which variable is smaller
    if a < b:
        divisor = a
    elif a > b:
        divisor = b
    else:
        divisor = a

    while divisor > 1:
        if a%divisor == 0:
            if b%divisor == 0:
                return divisor
        divisor -= 1
    return 1

# Test cases calling gcdIter, remove before submitting
print "Calling gcdIter(2, 12): " + str(gcdIter(2, 12))
print "Calling gcdIter(6, 12): " + str(gcdIter(6, 12))
print "Calling gcdIter(9, 12): " + str(gcdIter(9, 12))
print "Calling gcdIter(17, 12): " + str(gcdIter(17, 12))
