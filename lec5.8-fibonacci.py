# lec5.8-fibonacci.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, video 8
#
# Leonardo of Pisa (Fibonacci) wanted to calculate how many female rabbits
# would exist at the end of one year given the following assumptions:
#
# A newborn pair of rabbits (one male, one female) are put into a pen
# Rabbits mate at age of one month
# Rabbits have a one month gestation period
# Rabbits never die
# Female produces one pair (one male, one female) every month from second month
#
# How many female rabbits are there at then end of one year?

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""

    # Takes an expression and evalutes if true
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

# Examples of calling fib()
print "Calling fib(0) " + str(fib(0))
print "Calling fib(1) " + str(fib(1))
print "Calling fib(2) " + str(fib(2))
print "Calling fib(3) " + str(fib(3))
print "Calling fib(4) " + str(fib(4))
print "Calling fib(12) " + str(fib(12))
