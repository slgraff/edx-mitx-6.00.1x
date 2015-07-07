# lec6prob10-howMany.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 6, problem 10

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
# First, write a procedure, called howMany, which returns the sum of the
# number of values associated with a dictionary. For example:
#
# >>> print howMany(animals)
# 6

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    for l in aDict.values():
       for i in l: count += 1
    return count
