# lec5.9-isPalindrome.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, video 9

# Recursion on strings
# Determine if a string is a palindrome (reads the same forwards and backwards)

# Example of a divide and conquer problem
# Solve a hard problem by breaking it into sub-problems such that:
#   Sub-problems are easier to solve that original
#   Solutions of sub-problems can be combined to sold original problem

def isPalindrome(s):

    # Converts string to lower case and removes all non-alphabetic chars
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        # String of length 0 or 1 is always a palindrome
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

# Examples of calling isPalindrome()
print "Calling isPalindrome('abba'): " + str(isPalindrome('abba'))
print "Calling isPalindrome('guttag'): " + str(isPalindrome('guttag'))
print "Calling isPalindrome('guttug'): " + str(isPalindrome('guttug'))
print "Calling isPalindrome('able was I ere I saw elba'): " + str(isPalindrome('able was I ere I saw elba'))
