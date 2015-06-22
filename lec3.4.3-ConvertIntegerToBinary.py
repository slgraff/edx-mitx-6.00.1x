# Lecture 3.4 slide 3
# Simple Algorithms: Floating Point Accuracy
# Computers represent numbes in binary
# This code converts an integer to binary using Python

# We just set a number. Numbers used in lecture are 302 and 256
num = 302

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num/2
if isNeg:
    result = '-' + result

# Code show in lecture does not print result
# Can simply type 'result' in console to see result
# I'm choosing to instead print the result from the code
print result