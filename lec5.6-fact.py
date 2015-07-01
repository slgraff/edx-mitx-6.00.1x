# lec5.6-fact.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, video 6

# The "classic" recursive problem is a factorial
# n! = n * (n-1) * ... * 1
# = n * (n - 1)! if n > 1
# = 1 if n = 1


# Iterative version of factorial
def factI(n):
    """assumes that n is an int > 0
       returns n!"""
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res

# Recursive version of factorial
def factR(n):
    """assumes that n is an int > 0
       returns n!"""
    if n == 1:
        return n
    return n*factR(n-1)

# Examples of calling both versions
print "Calling factI with 1: " + str(factI(1))
print "Calling factI with 3: " + str(factI(3))
print "Calling factI with 25: " + str(factI(25))

print "Calling factR with 1: " + str(factR(1))
print "Calling factR with 3: " + str(factR(3))
print "Calling factR with 25: " + str(factR(25))
