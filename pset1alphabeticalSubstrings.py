# pset1alphabeticalSubstrings.py
# Problem Set 1 - Alphabetical Substrings
#
# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the 
# letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
# then your program should print:
#
# Longest substring in alphabetical order is: beggh
#
# In the case of ties, print the first substring. For example, if s = 'abcbcd', 
# then your program should print:
#
# Longest substring in alphabetical order is: abc
#
# For problems such as these, do not include raw_input statements or define 
# the variable s in any way. Our automated testing will provide a value of
# s for you - so the code you submit in the following box should assume s is 
# already defined.
#
# NOTE: for my development and testing am including the following 
# values for 's'. Comment out before submitting for grading
# s = "azcbobobegghakl"
# s = "abcbcd"
s = "abcbxyzlmnopqrs"

# Initialize theMatch to hold first character of s
bestMatch = s[0]

# Initialize testString to first character of s
testString = s[0]

# We are going to start at s[1] since we
# initialized value of testString to s[0]
for i in range (1, len(s)):
    
    # My troubleshooting print statements. Comment out before submitting.
    # print "s[i]: " + s[i]
    # print "bestMatch: " + bestMatch
    
    if s[i] >= s[i-1]:
        testString = testString + s[i]       
    else:
        testString = s[i]
        
    # Test to see if length of testString is greater than bestMatch
    if len(testString) > len(bestMatch):
        # if true, set bestMatch to value of testString
        bestMatch = testString
               
print "Longest substring in alphabetical order is: " + bestMatch