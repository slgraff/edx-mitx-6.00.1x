# lec6prob2-oddTuples.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 6, problem 2

# Write a procedure called oddTuples, which takes a tuple as input, and returns
# a new tuple as output, where every other element of the input tuple is copied,
# starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test',
# 'tuple'), then evaluating oddTuples on this input would return the tuple
# ('I', 'a', 'tuple').

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    return (aTup[0::2])

# Examples calls of oddTuples()
myTuple = ('I', 'am', 'a', 'test', 'tuple')
theResult = oddTuples(myTuple)
print theResult
