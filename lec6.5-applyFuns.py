# lec6.5-applyFuns.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 6, video 5

# Shows functions as elements of a list
# applyFuns() applies each function in the list
# to the argument 4

def applyFuns(L, x):
  for f in L:
    print(f(x))

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

applyFuns([abs, int, fact, fib], 4)
