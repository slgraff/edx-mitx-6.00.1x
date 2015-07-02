# lec6.5-map.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 6, video 5

# Python provides a general purpose HOP (Higher Order Procedure)
# One provided is map, a unary function and a collection of
# suitable arguments

# map applies a function to every item of an iterable object and returns
# a list of the results

# Using map to apply the abs function on each item in a list
print (map(abs, [1, -2, 3, -4]))
# prints [1, 2, 3, 4]


# Using map to apply the min function to compare each item in two lists,
# returns the minimum value of each in a new list
L1 = [1, 28, 36]
L2 = [2, 57, 9]

print (map(min, L1, L2))
# prints [1, 28, 9]
