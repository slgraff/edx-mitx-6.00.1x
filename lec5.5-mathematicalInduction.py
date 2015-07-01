# lec5.5-matematicalInduction
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, video 5

# How do we know that our recursive code will work?
# When recurMul called with b = 1 has no recursive call and stops
# When called with b > 1 makes a recursive call with smaller version of b,
# eventually is called with b = 1 and will stop

# Example of mathematical induction
# To prove a statement indexed on integers is true for all values of n:
# Prove that it is true when n is smallest value (e.g. n = 0 or n = 1)
# Then prove that is true for arbitrary value of n
# Can then show that it must be true for n + 1

# Example
# 0 + 1 + 2 + 3 + ... + n = (n * (n+1))/2
# If n = 0, then left side is 0 and right side is 0*1/2 = 0
# Assume true for some value k, then need to show that:
# 0 + 1 + 2 + 3 + ... + k + (k+1) = (k+1) * (k+2)/2


def recurMul(a, b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)

# Sample calls to recurMul
print str(recurMul(1, 3))
print str(recurMul (4, 4))
