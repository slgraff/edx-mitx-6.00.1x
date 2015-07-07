# pset3.1-radiationExposure.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Problem Set 3, problem 1

# Sample function for f, remove before submitting
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''

    totalRadiation = 0

    theCount = start
    while theCount < stop:
        totalRadiation = totalRadiation + (step * f(theCount))
        theCount += step
    return totalRadiation

# Sample calls to radiationExposure()
print (radiationExposure(0, 5, 1))
# 39.10318784326239
print (radiationExposure(5, 11, 1))
# 22.94241041057671
print (radiationExposure(0, 11, 1))
# 62.0455982538
print (radiationExposure(40, 100, 1.5))
# 0.434612356115
