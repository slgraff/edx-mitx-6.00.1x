# Quiz1Problem6.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Quiz 1, Problem 6
#
# Write a recursive Python function, given a non-negative integer N, to
# calculate and return the sum of its digits.
#
# Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while
# doing integer division by 10 removes the rightmost digit (126 / 10 is 12).
#
# This function has to be recursive; you may not use loops!
#
# This function takes in one integer and returns one integer.


def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here

    # If N < 9 then it has only one digit
    if N < 9:
        return N
    else:
        return ((N % 10) + sumDigits(N/10))


# Calling sumDigits, comment out before submitting
print(sumDigits(126))
print(sumDigits(123))
print(sumDigits(987))
