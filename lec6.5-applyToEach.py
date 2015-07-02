# lec6.5-applyToEach.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 6, video 5

# Functions as Objects
# Functions are first class objects
#   They have types
#   They can be elements of data structures
#   They can appear in expressions
#       As part of an assignment statment
#       As an argument to a function 

def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.4]

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

applyToEach(L, fact)
print(L)

# Passes in [1, 2 ,6] to fib, returns the 1st, 2nd, and 6th numbers
# in the fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
applyToEach(L, fib)
print(L)
