# lab4.2 - Functions
# Lab 4 Problem 2

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
    
# This lab asks you to evaluate the value of the following function calls
# given the above function definitions. Type and value of the result are entered
# into an interactive form.
# Entered code in order to better understand the functions and results
# Surrounded each function call in print function
# and cast to str to show results

print str(a(False, 2, 3))

print str(b(3, 2))

print str(a(3>2, a, b))

print str(b(a, b))
