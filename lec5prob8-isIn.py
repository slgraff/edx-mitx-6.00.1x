# lec5prob8-IsIn.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, problem 8

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    low = 0
    high = len(aStr)
    mid = (low + high) / 2


    i = 0

    # Set limits on how many times loop will run
    while i < 50:
       i += 1
       # If string is empty return False
       if len(aStr) <= 0:
           return False
        # if  char = middle character return True
       if char == aStr[mid]:
           return True
        # if we've gone through entire string and not found match
        # return False
       if (low == mid or high == mid) and (char != aStr[mid]):
           return False
       else:
           # if char is greater than the midpoint, move selection
           # of string up
           if char > aStr[mid]:
               low = mid
               return isIn(char, aStr[low:high])
            # if char is greater than the midpoint, move selection
            # of string down
           else:
               high = mid
               return isIn(char, aStr[low:high])

theResult = isIn('a', 'abcdef')
print (str(theResult))
