# lec6prob11-biggest.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 6, problem 11

# Consider the following sequence of expressions:
#
# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# We want to write some simple procedures that work on dictionaries to
# return information.
#
# This time, write a procedure, called biggest, which returns the key
# corresponding to the entry with the largest number of values associated with
# it. If there is more than one such entry, return any one of the matching keys.
#
# Example usage:
#
# >>> biggest(animals)
# 'd'
# If there are no values in the dictionary, biggest should return None.

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here

    result = None
    theBiggest = 0
    for key in aDict.keys():
        if len(aDict[key]) >= theBiggest:
            result = key
            theBiggest = len(aDict[key])
    return result


# Example values and function call
animals = {'a': ['aardvark'], 'c': ['coati'], 'b': ['baboon'], 'd': ['donkey', 'dog', 'dingo']}
print str(biggest(animals))
