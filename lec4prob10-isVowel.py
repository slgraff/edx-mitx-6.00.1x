# lec4prob10-isVowl.py
# Lecture 4, Problem 10

##Define a function isVowel(char) that returns True if char is a
##vowel ('a', 'e', 'i', 'o', or 'u'), and False otherwise.
##You can assume that char is a single letter of any case
##(ie, 'A' and 'a' are both valid).
##
##Do not use the keyword in. Your function should take in a
##single string and return a boolean.

def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    if char == "a" or char == "A":
        return True
    if char == "e" or char == "E":
        return True
    if char == "i" or char == "I":
        return True
    if char == "o" or char == "O":
        return True
    if char == "u" or char == "U":
        return True
    else:
        return False

# Test cases
print str(isVowel("a"))
print str(isVowel("A"))
print str(isVowel("z"))
print str(isVowel("t"))

