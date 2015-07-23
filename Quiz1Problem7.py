# Quiz1Problem7.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Quiz 1, Problem 7
#
# Write a Python function that returns a list of keys in aDict with the
# value target. The list of keys you return should be sorted in increasing
# order. The keys and values in aDict are both integers. (If aDict does not
# contain the value target, you should return an empty list.)
#
# This function takes in a dictionary and an integer and returns a list.

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Initialize matchList
    matchList = []

    # Find all values in aDict that match, put their keys in matchList
    for theKey, theValue in aDict.iteritems():
        if theValue == target:
            # Debug print, comment out before submitting
            # print(theValue)

            matchList.append(theKey)

            # Debug print, comment out before submitting
            # print(matchList)
    # matchList = [theKey for theKey, theValue in aDict.items() if theValue == target]

    # Sort matchList and return
    matchList.sort()
    return matchList



# Calling keysWithValue(), comment out before submitting
# aDict{key : value, . . .}
aDict = {1 : 11, 2 : 22, 3 : 33, 5 : 44, 4 : 44}

print(keysWithValue(aDict, 11))
print(keysWithValue(aDict, 44))
print(keysWithValue(aDict, 77))
