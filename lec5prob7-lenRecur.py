# lec5prob7-lenRecur.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, problem 7

# For this problem, write a recursive function, lenRecur, which computes the
# length of an input argument (a string), by counting up the number of
# characters in the string.
#
# Hint: String slicing may be useful in this problem...

def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here

    # Debug print statement
    print aStr

    # Check if string is empty
    if aStr == '':
        return 0

    # Call lenRecur recursively
    # If aStr is "Hello" on first pass, below will then strip off first
    # character "H", passing "ello" as argument to lenRecur()
    # This continues until end of string
    return 1  + lenRecur(aStr[1:])

# Examples of calling lenRecur()
print 'Calling lenRecur("Hello, world!"): ' + str(lenRecur('Hello, world!'))
print 'Calling lenRecur("Shazbat!"): ' + str(lenRecur('Shazbat!'))
print 'Calling lenRecur(''): ' + str(lenRecur(''))
