# lec3.7.3-Newton-Raphson
# Lecture 3.7, slide 3

# Using Newton-Raphson to calculate root of polynomial
# Much more efficient method
# Newton-Rhapson says that given a guess g for root,
# a better guess is:
# g - (g**2 - k)/2g

# Values of y used in lecture are 24, 25.0, 12345

epsilon = 0.01
y = 24.0
guess = y/2.0

while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y)/(2*guess))
    print(guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))