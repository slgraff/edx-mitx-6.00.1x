# lec5prob5.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, problem 5

# The greatest common divisor of two positive integers is the largest integer
# that divides each of them without remainder. For example:
#
# gcd(2, 12) = 2
# gcd(6, 12) = 6
# gcd(9, 12) = 3
# gcd(17, 12) = 1
#
# A clever mathematical trick (due to Euclid) makes it easy to find greatest
# common divisors. Suppose that a and b are two positive integers:
#
# If b = 0, then the answer is a
#
# Otherwise, gcd(a, b) is the same as gcd(b, a % b)
#
# Write a function gcdRecur(a, b) that implements this idea recursively.
# This function takes in two positive integers and returns one integer.

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)


# Test cases calling gcdIter, remove before submitting
print "Calling gcdRecur(2, 12): " + str(gcdRecur(2, 12))
print "Calling gcdRecur(6, 12): " + str(gcdRecur(6, 12))
print "Calling gcdRecur(9, 12): " + str(gcdRecur(9, 12))
print "Calling gcdRecur(17, 12): " + str(gcdRecur(17, 12))
