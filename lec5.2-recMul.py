# lec5.3-recMul.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, video 3

# Example of a recursive algorithm

def recurMul(a, b):
    if b == 1:
        return a
    else:
        # recurMul recursively calls itself when b > 1
        # Each recursive call creates own scope of local variables
        return a + recurMul(a, b-1)
    

# Example of calling function
print str(recurMul(3, 5))
print str(recurMul(26, 35))
