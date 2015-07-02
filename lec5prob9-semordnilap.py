# lec5prob9-semordnilap.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, problem 9
# A semordnilap is a word or a phrase that spells a different word when backwards
# ("semordnilap" is a semordnilap of "palindromes"). Here are some examples:
#
# nametag / gateman
# dog / god
# live / evil
# desserts / stressed
#
# Write a recursive program, semordnilap, that takes in two words and says if
# they are semordnilap.

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here

    # Check to see if both strings are empty
    if not (len(str1) or len(str2)): return True

    # Check to see if only one string is empty
    if not (len(str1) and len(str2)): return False

    # Check to see if first char of str1 = last of str2
    # If not, no further comparison needed, return False
    if str1[0] != str2[-1]: return False

    return semordnilap(str1[1:], str2[:-1])
    # Performing a semordnilap comparison using slicing notation,
    # but this is not valid for this assigment
    # elif str1 == str2[::-1]:
    #     return True


# Example of calling semordnilap()
theResult = semordnilap('may', 'yam')
print (str(theResult))
