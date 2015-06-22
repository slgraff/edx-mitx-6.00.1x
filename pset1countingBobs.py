# pset1countingBobs.py
# Problem Set 1 - Counting Bobs
#
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print
#
# Number of times bob occurs is: 2
# For problems such as these, do not include raw_input statements or define 
# the variable s in any way. Our automated testing will provide a value 
# of s for you - so the code you submit in the following box should assume s
# is already defined.
#
# Referred to 'String searching algorithm' Wikipedia entry
#
# NOTE: for my development and testing am including the following 
# definitions of 's'. Comment out before submitting for grading
# s = "azcbobobegghakl"
# s = "ohitsyoubobhowareyoubobnicetomeetyoubob"

# Initialize the variables numBobs and subString
numBobs = 0
subString = "bob"

for i in range (len(s)):
    if s[i:].startswith(subString):
        numBobs += 1

print "Number of times bob occurs is: " + str(numBobs)