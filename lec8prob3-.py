# lec8prob3-.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 8, problem 3

# This code raises a ZeroDivisionError exception for the following call:
# FancyDivide([0, 2, 4], 0)
# Your task is to change the definition of SimpleDivide so that the call does
# not raise an exception. When dividing by 0, FancyDivide should return a list
# with all 0 elements. Any other error cases should still raise exceptions.
# You should only handle the ZeroDivisionError.


def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]

# Original code for SimpleDivide
# def SimpleDivide(item, denom):
#    return item / denom

# Fixed code for SimpleDivide that handles the ZeroDivisionError
def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError, e:
        emptyList = []
        return 0

# Enclosed in print statement to see result
print (FancyDivide([0, 2, 4], 0))
