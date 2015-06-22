# Lecture 3.4 slide 4
# Simple Algorithms: Floating Point Accuracy
# Computers represent numbers in binary
# This code converts a fraction (decimal) to binary using Python

# Get a decimal number from user
x = float(raw_input('Enter a decimal number between 0 and 1: '))

# Loop through to look for power of 2
p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

# Convert to a whole number
num = int(x*(2**p))

# Convert to binary
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num/2

# Make sure that there are enough zeroes in front
for i in range(p - len(result)):
    result = '0' + result

# Deterine where to place the decimal point
result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))