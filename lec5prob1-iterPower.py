# lec5prob1-iterPower.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5,Problem 1

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    count = exp - 1

    # Debug print statement, remove before submitting
    print ('Result: ' + str(result) + ' Base: ' + str(base))
    while count >= 0:
        # Multiply result by itself
        result *= base

        # Debug print statement, remove before submitting
        print str(result)

        # Reduce the value of exp
        count -= 1
        
    return result

# Example of calling iterPower, correct result would be 3125
# Remove before submitting
print str(iterPower(5, 5))

