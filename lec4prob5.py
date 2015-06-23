# lec4prob5.py
# Code for Lecture 4, Problem 5
#
# Write a Python function, clip(lo, x, hi) that returns lo if x is less than lo;
# hi if x is greater than hi; and x otherwise.
# For this problem, you can assume that lo < hi.
#
# Don't use any conditional statements for this problem.
# Instead, use the built in Python functions min and max.
# You may wish to read the documentation on min and the documentation
# on max, and play around with these functions a bit in your interpreter,
# before beginning this problem.
#
# This function takes in three numbers and returns a single number.

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(max(x, lo), hi)

# Test code, comment out before pasting into grader
z = clip(5, 1, 10)
print str(z)
