# lec7prob6-integerDivision.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 7, problem 6

# Debug and fix the following code to resolve the below referenced error

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    # Fixed by initializing count before the while loop
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

# When we call the following:
print integerDivision(5, 3)

# We get the following error message:
# Traceback (most recent call last):
#   File "L7_Problem_5.py", line 15, in <module>
#     print integerDivision(5, 3)
#   File "L7_Problem_5.py", line 9, in integerDivision
#     count += 1
# UnboundLocalError: local variable 'count' referenced before assignment
