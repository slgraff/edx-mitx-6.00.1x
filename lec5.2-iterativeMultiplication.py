# lec5.2-interativeMultiply.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, video 2

# Demonstrates how to iterate through a loop to compute the result
# of multiplication by adding the value of a to itself b times
def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

# Example of calling function iterMul
print str(iterMul(3, 5))

print str(iterMul(26, 35))
