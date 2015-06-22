# Lecture 3.5 slide 2
# Simple Algorithms: Approximation Methods
# Use guess and check to find square root of any non-negative number
# Is an approximation, will fine an answer that is close

# Values of X used in lecture are 25 and 12345
x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0

# Have I gone far enough, am I done?
while (abs(ans**2 - x)) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses = ' + str(numGuesses))
if abs(ans**2-x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(str(ans) + ' is close to the square root of ' + str(x))