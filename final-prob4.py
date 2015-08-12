# final-prob4.py
#
# Final Exam, Problem 4
#
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python

"""
You are given a dictionary aDict that maps integer keys to integer values.
Write a Python function that returns a list of keys in aDict that map to
dictionary values that appear exactly once in aDict.

This function takes in a dictionary and returns a list.
Return the list of keys in increasing order.
If aDict does not contain any values appearing exactly once, return an empty list.
If aDict is empty, return an empty list.
Hint: You may want to create another dictionary as an intermediate data structure.

For example:
If aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} then your function should return [1, 3, 8]
If aDict = {1: 1, 2: 1, 3: 1} then your function should return []
"""

# Sample values for aDict
# Remove before submitting

# Program should return [1,3, 8]
# aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}

# Program should return []
# aDict = {1: 1, 2: 1, 3: 1}

# Program should Return [1, 5]
aDict = {0: 4, 9: 4, 3: 4, 5: 2, 1: 1}

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here

    # initialize a list, uniqList
    uniqList = []

    # set uniqList to all values from aDict
    for theKey, theValue in aDict.iteritems():
        uniqList.append(theValue)
    print uniqList

    # Remove duplicates from uniqList
    uniqList = list(set(uniqList))
    print uniqList

    for theKey, theValue in aDict.iteritems():
        print theValue
        if theValue in uniqList:
            print("In if")
            # if key theValue exists in countDict, increment it's value
            uniqList.remove(theValue)
            print uniqList
        else:
            print("In else")
            # Otherwise, add theValue to countDict with value of 1
            uniqList.append(theValue)
            print uniqList

    # countDict contains the values that appear only once
    print uniqList

    # create a list that contains the associated keys for the values
    # for key, value in countDict.iteritems():
    #     if value == 1:
    #         uniqList.append(key)

    # sort the list
    uniqList.sort()
    # print uniqList


    return uniqList

# Remove before submitting
uniqueValues(aDict)
