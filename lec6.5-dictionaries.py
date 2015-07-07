# lec6.5-dictionaries.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 6, video 5

# Demonstration of dictionaries
# Dict is a list, but now has indices, don't have to be integers
# Dict is a collection of <key, value> pairs
# Refer to indices as keys, keys must be imutable

# NOTE: Entries in dictionaries are unordered, can only be accessed
# by key, not be index

monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 1:'Jan', 2:'Feb', 3:'Mar'}

# Examples of retrieving entries in the dictionary using its key
monthNumbers['Jan']
monthNumbers[1]

# Can perform insertion. 'Apr' is the key, 4 is the value
monthNumbers ['Apr'] = 4

# Can iterate through dictionaries
collect = []
for e in monthNumbers:
    # Iterate through each item in monthNumbers, append the key to collect
    collect.append(e)
print (collect)

# Can compare value of dictionary collect with the keys in monthNumbers
print (monthNumbers.keys())
