# lec7prob7-rem.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 7, problem 7

# Debug this code to determine why a call to rem(7,5) does not return
# any result
# My debugging print statements that I used in debugging are commented out


def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    print ("Top of loop:", x, a)
    if x == a:
        print ("In x == a: ", x, a)
        return 0
    elif x < a:
        print ("In x < a: ", x, a)
        return x
    elif x > a:
        print ("In else: ", x, a)
        # print(x, a)
        # This needs to be changed to:
        # return rem(x-a, a)
        rem(x-a, a)



print rem(2, 5)
# Returns 2. correct result

print rem(5, 5)
# Returns 0, correct result

print rem(7, 5)
# No result returned
