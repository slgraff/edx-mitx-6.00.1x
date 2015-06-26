# Lecture 3.6 slide 2
# Bisection search for a square root

# Value of x used in lecture are 25, 12345, 1234567
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0  #Choose half of value x as starting guess
while abs(ans**2 - x) >= epsilon:   #Too far apart
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans  #Change low to ans (increasing it)
    else:
        high = ans   #Change high to ans (reducing it)
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
