# lec4prob7.py

# Enter the value of the expressions below.
#
# To get the most out of this problem, try to figure out the answers by
# reading the code, not running it. Run the code only after you've used
# up a few of your checks.

# Ran these in interactive Python shell to determine answers
# Included debugging print statements to see value of variables
# at each step. Wrapped function call in print to see returned value

# 1.
##def foo(x):
##    print "Inside foo. x = " + str(x)
##    def bar(x):
##        print "Inside bar. x = " + str(x)
##        return x + 1
##    print "Exited bar, back in foo. x = " + str(x)
##    return bar(x * 2)
##
##print str(foo(3))


# 2.
def foo (x):
    print "Inside foo. x = " + str(x)
    def bar (z):
        print "Inside bar. x = " + str(x) + ". z = " + str(z)
        return z + x
    print "Exited bar. back in foo. x = " + str(x)
    # Note: z does not exist outside of bar
    return bar(3)
    
print str(foo(2))
